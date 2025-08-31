import requests
import sys

try:
    url = "http://flask_app:5000/add"   # שים לב: שם הקונטיינר, לא localhost
    data = {"title": "Hello from test!"}

    r = requests.post(url, data=data, allow_redirects=False)

    if r.status_code in (200, 302):
        print("✅ TEST PASSED: Flask app responded correctly")
        sys.exit(0)
    else:
        print(f"❌ TEST FAILED: Unexpected status code {r.status_code}")
        sys.exit(1)

except Exception as e:
    print(f"❌ TEST FAILED: Exception occurred - {e}")
    sys.exit(1)

