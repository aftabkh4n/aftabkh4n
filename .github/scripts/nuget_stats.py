"""Write the owner's NuGet package count and total downloads between the README's NUGET-STATS markers."""
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

OWNER = os.environ.get("NUGET_OWNER", "aftabkh4n")
README = Path(os.environ.get("README_PATH", "README.md"))
SEARCH = "https://azuresearch-usnc.nuget.org/query"
MARKERS = re.compile(r"(<!-- NUGET-STATS:START -->\n).*?(\n<!-- NUGET-STATS:END -->)", re.S)


def fetch(owner):
    query = urlencode({"q": f"owner:{owner}", "take": 1000, "prerelease": "true", "semVerLevel": "2.0.0"})
    request = Request(f"{SEARCH}?{query}", headers={"User-Agent": f"{owner}-profile-readme"})
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def summarize(result, owner):
    # Keep only packages this account owns; the owner: filter is exact, this guards against a looser match.
    packages = [p for p in result.get("data", []) if owner.lower() in (o.lower() for o in p.get("owners", [owner]))]
    return len(packages), sum(int(p.get("totalDownloads", 0)) for p in packages)


def render(count, downloads):
    return f"`total packages: {count}` · `total downloads: {downloads:,}`"


def main():
    source = os.environ.get("NUGET_RESPONSE")  # local JSON file, for testing without network
    result = json.loads(Path(source).read_text()) if source else fetch(OWNER)
    count, downloads = summarize(result, OWNER)
    if count == 0:
        sys.exit(f"No NuGet packages found for owner {OWNER}; leaving the README unchanged.")
    text = README.read_text(encoding="utf-8")
    if not MARKERS.search(text):
        sys.exit("NUGET-STATS markers not found in the README.")
    updated = MARKERS.sub(lambda m: m.group(1) + render(count, downloads) + m.group(2), text, count=1)
    README.write_text(updated, encoding="utf-8")
    print(render(count, downloads))


if __name__ == "__main__":
    main()
