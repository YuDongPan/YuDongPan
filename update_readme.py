import requests
import os

# 获取 GitHub 用户名和 Token
username = 'YuDongPan'
token = os.getenv('GITHUB_TOKEN')

# 获取用户的所有仓库
response = requests.get(f'https://api.github.com/users/{username}/repos?per_page=100', auth=(username, token))
repos = response.json()

# 按 Star 数排序，获取前四个仓库
top_repos = sorted(repos, key=lambda repo: repo['stargazers_count'], reverse=True)[:4]

# 生成 2×2 表格的 Markdown
table = '<table>\n'
for i, repo in enumerate(top_repos):
    if i % 2 == 0:
        table += '  <tr>\n'
    table += f'    <td>\n      <a href="{repo["html_url"]}">\n        <img src="https://github-readme-stats.vercel.app/api/pin/?username={username}&repo={repo["name"]}" />\n      </a>\n    </td>\n'
    if i % 2 == 1:
        table += '  </tr>\n'
table += '</table>'

# 读取当前的 README.md 内容
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 替换特定标记之间的内容
start_marker = '<!-- START_TOP_REPOS -->'
end_marker = '<!-- END_TOP_REPOS -->'
start_index = readme.find(start_marker) + len(start_marker)
end_index = readme.find(end_marker)
new_readme = readme[:start_index] + '\n' + table + '\n' + readme[end_index:]

# 将更新后的内容写回 README.md
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme)
