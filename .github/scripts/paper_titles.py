# Print the sorted list of paper titles shown in the Papers table.
# Used by the weekly workflow to tell whether the list of papers changed,
# ignoring parts of the page that differ on every build (word clouds,
# network layout, widget ids).
import json
import re
import sys

html = open(sys.argv[1], encoding="utf-8").read()
for block in re.findall(r'<script type="application/json" data-for="[^"]+">(.*?)</script>', html, re.S):
    data = json.loads(block).get("x", {}).get("tag", {}).get("attribs", {}).get("data")
    if data and "Title" in data:
        for title in sorted(data["Title"]):
            print(title)
        break
else:
    sys.exit("Papers table not found in " + sys.argv[1])
