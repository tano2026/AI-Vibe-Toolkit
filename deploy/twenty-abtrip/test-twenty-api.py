#!/usr/bin/env python3
"""Test PASS/FAIL cho Twenty: tạo 1 Company -> đọc lại -> xoá.
Chạy trên VPS (hoặc nơi vào được Twenty):
  TWENTY_URL="http://127.0.0.1:3000" TWENTY_API_KEY="..." python3 test-twenty-api.py
API key tạo trong giao diện Twenty: Settings -> APIs & Webhooks (tên mục có thể khác theo bản).
Chỉ dùng urllib (đúng quy ước Hermes). Không in API key.
"""
import json, os, sys, urllib.request, urllib.error

URL = os.environ.get("TWENTY_URL", "http://127.0.0.1:3000").rstrip("/")
KEY = os.environ.get("TWENTY_API_KEY", "")
if not KEY:
    print("FAIL: thiếu biến TWENTY_API_KEY"); sys.exit(2)

def call(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{URL}/rest/{path}", data=data, method=method, headers={
        "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:300]}

def find_id(o):
    if isinstance(o, dict):
        if isinstance(o.get("id"), str): return o["id"]
        for v in o.values():
            r = find_id(v)
            if r: return r
    if isinstance(o, list):
        for v in o:
            r = find_id(v)
            if r: return r

NAME = "TEST-PASS-FAIL-XOA-DI"
st, res = call("POST", "companies", {"name": NAME})
rid = find_id(res)
if st not in (200, 201) or not rid:
    print(f"FAIL ở bước TẠO: HTTP {st} {res}"); sys.exit(1)
st, res = call("GET", f"companies/{rid}")
if st != 200 or NAME not in json.dumps(res, ensure_ascii=False):
    print(f"FAIL ở bước ĐỌC LẠI: HTTP {st} {res}"); sys.exit(1)
st, res = call("DELETE", f"companies/{rid}")
print("PASS: tạo -> đọc lại -> xoá thành công" if st in (200, 204) else f"PASS (tạo/đọc OK) nhưng xoá lỗi HTTP {st}: xoá tay record '{NAME}'")
sys.exit(0)
