import json, os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import smoke_merge

class T(unittest.TestCase):
    def test_gop_va_loai_loi(self):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(d + "/catalog/smoke")
            json.dump({"items": [{"id": "a"}, {"id": "b"}]}, open(d + "/catalog/catalog.json", "w"))
            json.dump({"lo": "x", "ket_qua": [
                {"id": "a", "verdict": "pass", "van_de": []},
                {"id": "b", "verdict": "partial", "van_de": [{"ma": "MO_HO"}, {"ma": "MO_HO"}]},
                {"id": "zzz", "verdict": "pass"}, {"id": "a", "verdict": "fail"}, {"id": "b", "verdict": "ok-lạ"}]},
                open(d + "/catalog/smoke/skill-x.json", "w"))
            out, errs = smoke_merge.merge(d)
        self.assertEqual(set(out["items"]), {"a", "b"})
        self.assertEqual(out["items"]["b"]["ma_van_de"], ["MO_HO"])
        self.assertEqual(len(errs), 3)
        self.assertEqual(out["tong_ket"]["verdict"], {"pass": 1, "partial": 1})

if __name__ == "__main__":
    unittest.main()
