import time
import requests
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://reqres.in/api/login"


def send_request():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    start = time.time()
    response = requests.post(BASE_URL, json=payload)
    duration = time.time() - start

    return response.status_code, duration


def test_sustained_concurrent_load():

    users = 20
    duration_seconds = 30
    results = []

    start_time = time.time()

    while time.time() - start_time < duration_seconds:
        with ThreadPoolExecutor(max_workers=users) as executor:
            batch = list(executor.map(lambda _: send_request(), range(users)))
            results.extend(batch)

    status_codes = [r[0] for r in results]
    durations = [r[1] for r in results]

    avg_response = sum(durations) / len(durations)

    assert all(code == 200 for code in status_codes)
    assert avg_response < 2