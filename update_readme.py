import json

with open('gists.json') as f:
  gists = json.load(f)

sorted_gists = sorted(gists, key=lambda x: x['created_at'], reverse=True)
filtered_gists = sorted_gists[:6]

for gist in gists:
  filtered_gists.append(gist)

# Format gists into a list
gist_md = '<ul>\n'
for gist in filtered_gists:
  for filename, fileinfo in gist['files'].items():
    gist_md += f"  <li><a href=\"{gist['html_url']}\">{filename}</a>\n"
    gist_md += f"    <p>{gist['description']}</p>\n"
    gist_md += f"  </li>\n"
gist_md += '</ul>'

gists_url = '\n'.join([f"- [{gist['description']}]({gist['url']})" for gist in gists])

with open('README.md', 'r') as f:
  readme = f.read()

# Use partition method to insert gists into readme file
marker = '<!-- gists -->'
before, marker, after = readme.partition(marker)
new_readme_content = f"{before}{marker}\n{gist_md}\n{after}"

with open('README.md', 'w') as f:
  f.write(new_readme_content)