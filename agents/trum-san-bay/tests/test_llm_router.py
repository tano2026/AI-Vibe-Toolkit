"""Test llm_router.py — mock hoàn toàn: patch llm_router._http_post_json, không mạng, không khoá thật.
Chạy: python -m unittest discover -s agents/trum-san-bay/tests"""
import os
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import llm_router as lr  # noqa: E402


def omni_resp(text="ok", pin=1000, pout=500):
    return {"choices": [{"message": {"content": text}}],
            "usage": {"prompt_tokens": pin, "completion_tokens": pout}}


def claude_resp(text="ok", tin=1000, tout=500):
    return {"content": [{"type": "text", "text": text}],
            "usage": {"input_tokens": tin, "output_tokens": tout}}


ENV = {"OMNIROUTE_URL": "http://omni.test/v1/chat/completions",
       "OMNIROUTE_API_KEY": "test-omni", "ANTHROPIC_API_KEY": "test-anth"}


class LLMRouterTest(unittest.TestCase):
    def setUp(self):
        lr.reset_tracker()
        p = mock.patch.dict(os.environ, ENV)
        p.start()
        self.addCleanup(p.stop)
        os.environ.pop("TSB_COST_FILE", None)
        os.environ.pop("TSB_BUDGET_MONTHLY_USD", None)

    def test_orchestrator_importable(self):
        # lỗi gốc: ImportError cannot import name 'llm_call' from 'agent'
        sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
        import orchestrator
        self.assertTrue(callable(orchestrator.llm_call))

    def test_cheap_tier_goes_to_omniroute_with_mapped_model(self):
        with mock.patch.object(lr, "_http_post_json", return_value=omni_resp("xin chao")) as m:
            out = lr.llm_call("hi", tier="cheap", max_tokens=50, temperature=0.2)
        self.assertEqual(out, "xin chao")
        url, payload, headers = m.call_args[0][:3]
        self.assertEqual(url, ENV["OMNIROUTE_URL"])
        self.assertEqual(payload["model"], "deepseek-v3")
        self.assertEqual(payload["max_tokens"], 50)
        self.assertEqual(payload["temperature"], 0.2)
        self.assertEqual(headers["Authorization"], "Bearer test-omni")

    def test_creative_tier_goes_to_anthropic(self):
        with mock.patch.object(lr, "_http_post_json", return_value=claude_resp("caption")) as m:
            out = lr.llm_call("viet", tier="creative")
        self.assertEqual(out, "caption")
        url, payload, headers = m.call_args[0][:3]
        self.assertIn("anthropic.com", url)
        self.assertEqual(payload["model"], "claude-sonnet-4-6")
        self.assertEqual(headers["x-api-key"], "test-anth")

    def test_cost_is_actually_recorded(self):
        with mock.patch.object(lr, "_http_post_json", return_value=claude_resp(tin=1_000_000, tout=100_000)):
            lr.llm_call("x", tier="creative", agent="writer")
        t = lr.get_tracker()
        self.assertEqual(len(t.records), 1)
        # 1M in * $3 + 0.1M out * $15 = $4.5
        self.assertAlmostEqual(t.total_cost, 4.5, places=6)
        self.assertEqual(t.by_agent(), {"writer": t.total_cost})

    def test_budget_blocks_after_exceeding(self):
        os.environ["TSB_BUDGET_MONTHLY_USD"] = "1.00"
        with mock.patch.object(lr, "_http_post_json",
                               return_value=claude_resp(tin=1_000_000, tout=0)) as m:
            lr.llm_call("x", tier="creative")  # tốn $3 > $1, lần này vẫn qua
            self.assertTrue(lr.get_tracker().over_budget)
            with self.assertRaises(lr.BudgetExceededError) as cm:
                lr.llm_call("y", tier="creative")
            self.assertEqual(m.call_count, 1)  # lần 2 bị chặn TRƯỚC khi gọi mạng
        self.assertAlmostEqual(cm.exception.limit, 1.0)

    def test_budget_error_is_same_class_agent_catches(self):
        import agent
        self.assertIs(agent.BudgetExceededError, lr.BudgetExceededError)

    def test_guarded_call_alerts_then_raises(self):
        os.environ["TSB_BUDGET_MONTHLY_USD"] = "0.0001"
        alerts = []
        with mock.patch.object(lr, "_http_post_json", return_value=omni_resp(pin=10**6, pout=10**6)):
            lr.llm_call("x", tier="cheap")
            with self.assertRaises(lr.BudgetExceededError):
                lr.guarded_llm_call("y", "cheap", "research", alerts.append)
        self.assertEqual(len(alerts), 1)

    def test_missing_keys_raise_config_error_without_network(self):
        with mock.patch.dict(os.environ, {}, clear=True), \
                mock.patch.object(lr, "_http_post_json") as m:
            with self.assertRaises(lr.LLMConfigError):
                lr.llm_call("x", tier="cheap")
            with self.assertRaises(lr.LLMConfigError):
                lr.llm_call("x", tier="creative")
            m.assert_not_called()

    def test_tokens_estimated_when_usage_missing(self):
        with mock.patch.object(lr, "_http_post_json",
                               return_value={"choices": [{"message": {"content": "abcdefgh"}}]}):
            lr.llm_call("a" * 400, tier="cheap")
        r = lr.get_tracker().records[0]
        self.assertEqual((r.input_tokens, r.output_tokens), (100, 2))

    def test_malformed_response_raises_call_error(self):
        with mock.patch.object(lr, "_http_post_json", return_value={"oops": 1}):
            with self.assertRaises(lr.LLMCallError):
                lr.llm_call("x", tier="cheap")
        self.assertEqual(len(lr.get_tracker().records), 0)  # lỗi không ghi chi phí

    def test_fallback_goes_to_claude_but_not_on_budget(self):
        calls = []

        def fake(url, payload, headers, timeout=60):
            calls.append(payload["model"])
            if payload["model"] == "deepseek-v3":
                raise lr.LLMCallError("boom")
            return claude_resp("fb")

        with mock.patch.object(lr, "_http_post_json", side_effect=fake):
            self.assertEqual(lr.llm_call_with_fallback("x", tier="cheap"), "fb")
        self.assertEqual(calls, ["deepseek-v3", "claude-sonnet-4-6"])

    def test_cost_file_persists_and_reloads(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            os.environ["TSB_COST_FILE"] = os.path.join(d, "c", "costs.json")
            with mock.patch.object(lr, "_http_post_json", return_value=omni_resp()):
                lr.llm_call("x", tier="cheap", agent="a")
            first = lr.get_tracker().total_cost
            lr.reset_tracker()
            self.assertAlmostEqual(lr.get_tracker().total_cost, first)
            os.environ.pop("TSB_COST_FILE")


if __name__ == "__main__":
    unittest.main()
