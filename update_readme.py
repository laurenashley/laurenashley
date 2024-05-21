import json

with open('gists.json') as f:
  gists = json.load(f)

sorted_gists = sorted(gists, key=lambda x: x['created_at'], reverse=True)

# Format gists into a list
gist_md = '<ul>\n'
for gist in sorted_gists[:6]:
  for filename, fileinfo in gist['files'].items():
    gist_md += f"  <li><a href=\"{gist['html_url']}\">{filename}</a>\n"
    gist_md += f"    <p>{gist['description']}</p>\n"
    gist_md += f"  </li>\n"
gist_md += '</ul>'

with open('README.md', 'r') as f:
  readme = f.read()

# Use partition method to insert gists into readme file
marker = '<!-- gists -->'
before, marker, after = readme.partition(marker)
new_readme_content = f"{before}{marker}\n{gist_md}\n{after}"

with open('README.md', 'w') as f:
  f.write(new_readme_content)