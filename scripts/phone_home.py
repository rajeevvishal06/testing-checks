"""Simulates a compromised dependency trying to send data to an outside host."""
import urllib.request

TARGET = "https://example.com"
try:
    urllib.request.urlopen(TARGET, timeout=10)
    print(f"::warning::phone_home reached {TARGET}: exfiltration would have succeeded")
except Exception as exc:  # noqa: BLE001
    print(f"::notice::phone_home was BLOCKED from {TARGET} ({type(exc).__name__})")
