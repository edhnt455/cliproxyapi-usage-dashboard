#!/usr/bin/env python3
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


def main():
    base_url = os.environ.get("CLIPROXY_DASHBOARD_URL", "http://127.0.0.1:8320").rstrip("/")
    range_name = os.environ.get("CLIPROXY_HUD_RANGE", "5h")
    timeout = float(os.environ.get("CLIPROXY_HUD_TIMEOUT", "1.5"))
    url = base_url + "/api/hud?" + urllib.parse.urlencode({"range": range_name})
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.load(response)
    except (OSError, urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, ValueError):
        print("Codex usage n/a")
        return 0
    text = payload.get("statusline_text") or payload.get("text") or "Codex usage n/a"
    print(text.replace("\n", " "))
    return 0


if __name__ == "__main__":
    sys.exit(main())
