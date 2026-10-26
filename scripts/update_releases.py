import json, os, re, urllib.request

USER = "somoore"
FEATURED = {"sir", "hellbox", "steampipe-plugin-turbopuffer", "powerpipe-turbopuffer-security-benchmark", "terraform-provider-tpuf", "pairputer-on-aws"}
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "Authorization": f"Bearer {TOKEN}"} if TOKEN else {"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)

repos = get(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner")
found = []
for r in repos:
    if r["name"] not in FEATURED:
        continue
    rel = get(f"https://api.github.com/repos/{USER}/{r['name']}/releases?per_page=10")
    rel = [x for x in rel if not x["draft"]]
    if rel:
        x = rel[0]
        found.append((x["published_at"] or x["created_at"], r["name"], x["tag_name"], x["html_url"]))

found.sort(reverse=True)
lines = [f"- [{name} {tag}]({url}) on {date[:10]}" for date, name, tag, url in found[:5]]
block = "\n".join(lines) if lines else "- Nothing yet."

text = open("README.md").read()
new = re.sub(r"(<!-- releases:start -->).*?(<!-- releases:end -->)", lambda m: f"{m.group(1)}\n{block}\n{m.group(2)}", text, flags=re.S)
if new != text:
    open("README.md", "w").write(new)
