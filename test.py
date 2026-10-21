
import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

key = os.getenv("AVIATIONSTACK_API_KEY")
base = "http://api.aviationstack.com/v1"

for endpoint in ("flights", "airports", "airlines"):
    try:
        response = requests.get(
            f"{base}/{endpoint}",
            params={"access_key": key, "limit": 1},
            timeout=20,
        )

        data = response.json()
        error = data.get("error")

        print(f"\n--- {endpoint} ---")
        print("HTTP:", response.status_code)

        if error:
            print("API error:", error)
        else:
            print("Records:", len(data.get("data", [])))
            print("Sample:", data.get("data", [])[:1])

    except Exception as exc:
        print(f"{endpoint} failed: {exc}")
