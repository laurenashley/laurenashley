import json

with open('gists.json') as f:
    gists = json.load(f)

gists_url = '\n'.join([f"- [{gist['description']}]({gist['url']})" for gist in gists])

with open('README.md', 'r') as f:
    readme = f.read()

marker = '<!-- gists -->'
before, marker, after = readme.partition(marker)
new_readme = f"{before}{marker}\n{gists_url}\n{after}"

with open('README.md', 'w') as f:
    f.write(new_readme)