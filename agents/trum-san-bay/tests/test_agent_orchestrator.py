"""Test agent.py + orchestrator.py bằng mock (Airtable/Postiz/LLM giả, state trong thư mục tạm).
Không mạng, không credential. Chạy: python -m unittest discover -s agents/trum-san-bay/tests"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import agent  # noqa: E402
import orchestrator  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        d = self.tmp.name
        for name, val in [("STATE_FILE", os.path.join(d, "progress.json")),
                          ("STATE_LOCK", os.path.join(d, "progress.lock")),
                          ("TOKEN_CACHE_FILE", os.path.join(d, "tokens.json"))]:
            p = mock.patch.object(agent, name, val)
            p.start()
            self.addCleanup(p.stop)
        self.sleeps = []
        p = mock.patch.object(agent._time, "sleep", side_effect=self.sleeps.append)
        p.start()
        self.addCleanup(p.stop)


class PublishFlow(Base):
    def setUp(self):
        super().setUp()
        self.fields = {"status": "APPROVED", "caption_fb": "Xin chào ✈️"}
        self.updates = []
        for name, val in [("POSTIZ_API_KEY", "test-key"), ("POSTIZ_FB_INTEGRATION_ID", "int-1"),
                          ("AIRTABLE_BASE_ID", "base"), ("AIRTABLE_API_KEY", "k")]:
            p = mock.patch.object(agent, name, val)
            p.start()
            self.addCleanup(p.stop)
        os.environ.pop("POSTIZ_POST_TYPE", None)
        self.postiz_payloads = []
        self.postiz_reply = {"id": "post-1"}
        p = mock.patch.object(agent, "api_call", side_effect=self._api)
        p.start()
        self.addCleanup(p.stop)
        p = mock.patch.object(agent, "airtable_update",
                              side_effect=lambda t, r, f: self.updates.append((r, f)))
        p.start()
        self.addCleanup(p.stop)

    def _api(self, url, method="GET", data=None, headers=None):
        if "airtable.com" in url:
            return {"fields": dict(self.fields)}
        if "postiz.com" in url:
            self.postiz_payloads.append(data)
            r = self.postiz_reply
            return r(len(self.postiz_payloads)) if callable(r) else r
        raise AssertionError(url)

    # --- phần vốn đúng, phải giữ nguyên ---
    def test_gate_blocks_non_approved_without_any_request(self):
        for st in ["PENDING_REVIEW", "DRAFT_BRIEF", "POSTED"]:
            self.fields["status"] = st
            self.postiz_payloads.clear()
            with self.assertRaises(agent.PipelineGateError):
                agent.publish_post_safe("rec1")
            self.assertEqual(self.postiz_payloads, [])

    def test_approved_live_post_is_success_and_posted(self):
        os.environ["POSTIZ_POST_TYPE"] = "now"
        self.addCleanup(os.environ.pop, "POSTIZ_POST_TYPE", None)
        alerts = []
        res = agent.publish_post_safe("rec1", alerts.append)
        self.assertEqual(res["status"], "success")
        self.assertEqual(self.postiz_payloads[0]["type"], "now")
        self.assertEqual(self.updates[-1][1]["status"], "POSTED")
        self.assertTrue(alerts[-1].startswith("✅"))

    def test_idempotency_skips_already_posted_platform(self):
        os.environ["POSTIZ_POST_TYPE"] = "now"
        self.addCleanup(os.environ.pop, "POSTIZ_POST_TYPE", None)
        agent.publish_post_safe("rec1")
        agent.publish_post_safe("rec1")
        self.assertEqual(len(self.postiz_payloads), 1)

    # --- lỗi đã sửa ---
    def test_no_platform_configured_is_config_error_not_success(self):
        with mock.patch.object(agent, "POSTIZ_API_KEY", None):
            alerts = []
            res = agent.publish_post_safe("rec1", alerts.append)
        self.assertEqual(res["status"], "config_error")
        self.assertEqual(self.updates, [])  # không ghi POSTED (hay gì) vào Airtable
        self.assertEqual(self.postiz_payloads, [])
        self.assertFalse(any("đã đăng" in a for a in alerts))
        self.assertEqual(agent._load_state()["rec1"]["status"], "config_error")

    def test_approve_command_reports_config_error(self):
        with mock.patch.object(agent, "POSTIZ_FB_INTEGRATION_ID", None):
            msg = agent.handle_command("approve", "rec1")
        self.assertNotIn("Đã đăng lên 0", msg)
        self.assertIn("Chưa đăng được", msg)

    def test_draft_payload_is_never_recorded_as_posted(self):
        alerts = []
        res = agent.publish_post_safe("rec1", alerts.append)  # mặc định type=draft
        self.assertEqual(self.postiz_payloads[0]["type"], "draft")
        self.assertEqual(res["status"], "draft_only")
        self.assertEqual(res["posted_platforms"], [])
        self.assertNotEqual(self.updates[-1][1]["status"], "POSTED")
        self.assertFalse(any(a.startswith("✅") for a in alerts))

    def test_retry_backoff_no_sleep_after_last_attempt(self):
        calls = []

        def fn():
            calls.append(1)
            return False, {}, 4  # facebook code 4 = retryable
        res = agent._retry_call("facebook", fn)
        self.assertEqual(res["status"], "failed_after_retries")
        self.assertEqual(len(calls), 3)
        self.assertEqual(self.sleeps, [5, 25])  # trước đây 5, 25, 125 = 155s

    def test_retry_succeeds_on_third_attempt(self):
        seq = iter([(False, {}, 4), (False, {}, 4), (True, {"id": "x"}, None)])
        res = agent._retry_call("facebook", lambda: next(seq))
        self.assertEqual(res["status"], "success")
        self.assertEqual(self.sleeps, [5, 25])

    def test_non_retryable_fails_immediately(self):
        res = agent._retry_call("facebook", lambda: (False, {}, 190))
        self.assertEqual(res["status"], "failed")
        self.assertEqual(self.sleeps, [])

    def test_max_retries_zero_no_unbound_local(self):
        calls = []
        res = agent._retry_call("facebook", lambda: (calls.append(1), (False, {}, 4))[1], max_retries=0)
        self.assertEqual(res["status"], "failed_after_retries")
        self.assertEqual(len(calls), 1)
        self.assertEqual(self.sleeps, [])

    def test_401_message_names_the_right_platform(self):
        self.postiz_reply = {"error": "unauth", "status": 401, "error_code": 401}
        alerts = []
        res = agent.publish_post_safe("rec1", alerts.append)
        msg = res["failed_platforms"]["facebook"]
        self.assertNotIn("YouTube", msg)
        self.assertIn("Postiz", msg)
        self.assertIn("YouTube", agent.error_message("youtube", 401))
        self.assertIn("TikTok", agent.error_message("tiktok", 401))
        self.assertEqual(self.updates[-1][1]["status"], "PARTIAL_FAIL")

    def test_save_state_writes_utf8_under_cp1252_default(self):
        # mô phỏng Windows: open() không khai báo encoding sẽ dùng cp1252
        import builtins
        real_open = builtins.open

        def cp1252_open(file, mode="r", *a, **kw):
            if "b" not in mode and "encoding" not in kw and len(a) < 2:
                kw["encoding"] = "cp1252"
            return real_open(file, mode, *a, **kw)
        with mock.patch("builtins.open", cp1252_open):
            agent.save_state("rec-vn", "publish", "in_progress", {"note": "Đã đăng ✈️ tiếng Việt"})
            self.assertEqual(agent._load_state()["rec-vn"]["extra"]["note"], "Đã đăng ✈️ tiếng Việt")
        raw = Path(agent.STATE_FILE).read_bytes().decode("utf-8")
        self.assertIn("Đã đăng", raw)

    def test_resume_incomplete_only_in_progress(self):
        agent.save_state("a", "publish", "in_progress")
        agent.save_state("b", "publish", "success")
        self.assertEqual(list(agent.resume_incomplete()), ["a"])


class LockPortability(unittest.TestCase):
    def test_import_agent_without_fcntl(self):
        """import agent không được chết khi không có fcntl (Windows)."""
        code = (
            "import sys; sys.modules['fcntl'] = None; sys.path.insert(0, r'%s');"
            "import agent; print('fcntl', agent.fcntl, 'ok')" % HERE
        )
        out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True,
                             encoding="utf-8")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("fcntl None ok", out.stdout)

    def test_lock_wrapper_runs_without_fcntl(self):
        with tempfile.TemporaryDirectory() as d, \
                mock.patch.object(agent, "fcntl", None), \
                mock.patch.object(agent, "STATE_LOCK", os.path.join(d, "l.lock")):
            f = agent._with_state_lock(lambda: 42)
            self.assertEqual(f(), 42)
            self.assertEqual(f(), 42)  # mở khoá xong khoá lại được

    def test_no_lock_backend_warns(self):
        with tempfile.TemporaryDirectory() as d, \
                mock.patch.object(agent, "fcntl", None), mock.patch.object(agent, "msvcrt", None, create=True), \
                mock.patch.object(agent, "STATE_LOCK", os.path.join(d, "l.lock")):
            with self.assertWarns(RuntimeWarning):
                self.assertEqual(agent._with_state_lock(lambda: 1)(), 1)


class OrchestratorFixes(Base):
    def test_comment_missing_label_does_not_kill_batch(self):
        comments = [
            {"id": "1", "platform": "facebook", "text": "bay có tốt không"},
            {"id": "2", "platform": "facebook", "text": "tệ quá, mất hành lý!"},
            {"id": "3", "platform": "facebook", "text": "mua ở đâu?"},
        ]
        classify = iter([{"priority": "P2"},  # thiếu label
                         {"label": "URGENT_COMPLAINT", "priority": "P1"},
                         {"label": "PURCHASE_INTENT", "priority": "P2"}])

        def fake_json(prompt, tier="cheap", max_tokens=1500):
            if "Phân loại" in prompt:
                return next(classify)
            return {"reply_text": "ok", "needs_human_review": False}
        created, alerts = [], []
        with mock.patch.object(orchestrator, "llm_call_json", side_effect=fake_json), \
                mock.patch.object(orchestrator, "airtable_create",
                                  side_effect=lambda t, f: created.append(f)):
            res = orchestrator.run_comment_pipeline(lambda: comments, alerts.append)
        self.assertEqual(res, {"processed": 3, "urgent": 1})
        self.assertEqual(len(created), 3)
        self.assertEqual(created[0]["label"], orchestrator.UNCLASSIFIED_LABEL)
        self.assertTrue(created[0]["needs_human_review"])
        self.assertTrue(created[1]["needs_human_review"])  # urgent luôn cần người
        self.assertEqual(len(alerts), 1)

    def test_comment_classification_unchanged_for_valid_labels(self):
        comments = [{"id": "s", "platform": "facebook", "text": "mua vé giá rẻ http://x"}]

        def fake_json(prompt, tier="cheap", max_tokens=1500):
            return {"label": "SPAM", "priority": "P4"}
        created = []
        with mock.patch.object(orchestrator, "llm_call_json", side_effect=fake_json), \
                mock.patch.object(orchestrator, "airtable_create",
                                  side_effect=lambda t, f: created.append(f)):
            orchestrator.run_comment_pipeline(lambda: comments)
        self.assertEqual(created[0]["draft_reply"], "")  # SPAM không trả lời
        self.assertFalse(created[0]["needs_human_review"])

    def test_comment_unparseable_json_does_not_kill_batch(self):
        def fake_json(prompt, tier="cheap", max_tokens=1500):
            raise json.JSONDecodeError("bad", "x", 0)
        created = []
        with mock.patch.object(orchestrator, "llm_call_json", side_effect=fake_json), \
                mock.patch.object(orchestrator, "airtable_create",
                                  side_effect=lambda t, f: created.append(f)):
            orchestrator.run_comment_pipeline(
                lambda: [{"id": "1", "platform": "x", "text": "a"}, {"id": "2", "platform": "x", "text": "b"}])
        self.assertEqual(len(created), 2)

    def test_stable_id_is_deterministic_across_processes(self):
        code = ("import sys; sys.path.insert(0, r'%s'); import orchestrator;"
                "print(orchestrator._stable_id('tiktok','v1','xin chào'))" % HERE)
        outs = {subprocess.run([sys.executable, "-c", code], capture_output=True, text=True,
                               encoding="utf-8", env={**os.environ, "PYTHONHASHSEED": seed}).stdout
                for seed in ("1", "2", "random")}
        self.assertEqual(len(outs), 1)

    def test_tiktok_comment_id_uses_stable_hash(self):
        src = (HERE / "orchestrator.py").read_text(encoding="utf-8")
        self.assertNotIn("str(hash(", src)

    def test_brand_check_not_hardcoded_failing(self):
        ok = orchestrator.run_brand_check({
            "colors_used": ["#0a1628"], "font": "Inter", "has_logo": True,
            "logo_position": "bottom-right"})
        self.assertTrue(ok["passed"])
        self.assertTrue(ok["fully_checked"])
        bad = orchestrator.run_brand_check({
            "colors_used": ["#123456"], "font": "Comic Sans", "has_logo": False})
        self.assertFalse(bad["passed"])
        self.assertEqual(len(bad["issues"]), 3)

    def test_brand_check_unknown_values_are_flagged_unchecked(self):
        r = orchestrator.run_brand_check({"colors_used": None, "font": "Inter", "has_logo": None})
        self.assertTrue(r["passed"])  # không có vi phạm trong phần đã kiểm
        self.assertFalse(r["fully_checked"])
        self.assertEqual(r["unchecked"], ["colors", "logo"])
        self.assertEqual(r["issues"], [])

    def test_pipeline_brand_check_reads_visual_result_not_constants(self):
        seen = {}
        real = orchestrator.run_brand_check

        def spy(meta):
            seen.update(meta)
            return real(meta)
        with mock.patch.object(orchestrator, "run_brand_check", side_effect=spy), \
                mock.patch.object(orchestrator, "run_visual_agent_image",
                                  return_value={"prompt": "p", "image_path": "/x.png",
                                                "has_logo": True, "logo_position": "bottom-right",
                                                "colors_used": ["#FFFFFF"]}):
            self._run_pipeline_one_post()
        self.assertIs(seen["has_logo"], True)
        self.assertEqual(seen["colors_used"], ["#FFFFFF"])

    def test_pipeline_without_visual_metadata_marks_unchecked(self):
        updates = []
        with mock.patch.object(orchestrator, "run_visual_agent_image",
                               return_value={"prompt": "p", "image_path": "/x.png"}):
            self._run_pipeline_one_post(updates)
        flagged = [f for f in updates if "brand_check_issues" in f]
        self.assertEqual(len(flagged), 1)
        self.assertIn("CHƯA KIỂM", flagged[0]["brand_check_issues"])

    def _run_pipeline_one_post(self, updates=None):
        updates = updates if updates is not None else []
        with mock.patch.object(orchestrator, "run_research_agent", return_value={"topics_found": 1}), \
                mock.patch.object(orchestrator, "run_ideation_agent",
                                  return_value={"briefs_created": 1}), \
                mock.patch.object(orchestrator, "run_writer_agent",
                                  return_value={"caption_fb": "c", "self_check": {}}), \
                mock.patch.object(orchestrator, "airtable_list",
                                  return_value={"records": [{"id": "rec1", "fields": {
                                      "status": "DRAFT_BRIEF", "topic": "t", "pillar": "TOFU",
                                      "brief": "b"}}]}), \
                mock.patch.object(orchestrator, "airtable_create", return_value={"id": "rec1"}), \
                mock.patch.object(orchestrator, "airtable_update",
                                  side_effect=lambda t, r, f: updates.append(f)), \
                mock.patch.object(orchestrator, "save_state"), \
                mock.patch.object(orchestrator.time, "sleep"):
            try:
                orchestrator.run_weekly_content_pipeline()
            except Exception as e:  # pipeline dài: chỉ cần tới được bước brand check
                self.fail(f"pipeline mock lỗi: {e!r}")


if __name__ == "__main__":
    unittest.main()
