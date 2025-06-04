from typing import Dict, List

import requests
from cachetools import cached, TTLCache
from packaging.version import parse as vparse

MANIFEST_URL = (
    "https://wizarrrr.github.io/wizarr/manifest.json")
TIMEOUT_SECS = 2
CACHE_HOURS = 6



@cached(cache=TTLCache(maxsize=1, ttl=CACHE_HOURS * 3600))
def _fetch_manifest() -> Dict:
    resp = requests.get(
        MANIFEST_URL,
        timeout=TIMEOUT_SECS,
        headers={"Accept": "application/json"},
    )
    resp.raise_for_status()
    print(f"Fetched manifest from {MANIFEST_URL} with status {resp.status_code}")
    print("Content:", resp.text[:100])  # Log first 100 chars for debugging
    return resp.json()


def _manifest() -> Dict:
    try:
        return _fetch_manifest()
    except Exception:
        # on failure, return empty or last good state if you choose to store it elsewhere
        return {}


def check_update_available(current_version: str) -> bool:
    """True if a newer semantic version exists in the manifest."""
    latest = _manifest().get("latest_version")
    if not latest:
        return False  # can't compare
    return vparse(latest) > vparse(current_version) if current_version != "dev" else False


def get_sponsors() -> List[Dict]:
    """Returns list like [{'login': 'alice', 'url': '…', 'avatarUrl': '…'}, …]."""
    return _manifest().get("sponsors", [])