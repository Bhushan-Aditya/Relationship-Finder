import requests
from test_cases import test_cases

API_URL = "http://0.0.0.0:8000/analyze"

passed = 0
for i, case in enumerate(test_cases, 1):
    payload = {"text": case['text'], "question": case['question']}
    try:
        resp = requests.post(API_URL, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        answer = data.get('answer', '').strip()
        expected = case['expected'].strip()
        if answer == expected:
            print(f"Test {i}: PASS ✅ | Q: {case['question']} | A: {answer}")
            passed += 1
        else:
            print(f"Test {i}: FAIL ❌ | Q: {case['question']} | Got: {answer} | Expected: {expected}")
    except Exception as e:
        print(f"Test {i}: ERROR ❌ | Q: {case['question']} | Error: {e}")

print(f"\nSummary: {passed}/{len(test_cases)} tests passed.") 