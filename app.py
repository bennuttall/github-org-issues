from flask import Flask
import github_org_issues as goi

app = Flask(__name__)

@app.route('/')
def index():
    org = "raspberrypilearning"
    repos = goi.get_org_repos_with_open_issues(org)
    html = '<h1><a href="https://github.com/%s">%s</a></h1>' % (org, org)
    html += '<table>'
    html += '<tr><th>Repository</th><th># Issues</th></tr>'
    total_issues = 0
    for repo in repos:
        repo_name = repo['name'].replace('-', ' ')
        open_issues_count = repo['open_issues_count']
        total_issues += open_issues_count
        repo_url = repo['html_url']
        issues_url = '%s/issues' % repo_url

        html += '<tr>'
        html += '<td><a href="%s">%s</a></td>' % (repo_url, repo_name)
        html += '<td><a href="%s">%s</a></td>' % (issues_url, open_issues_count)
        html += '</tr>'
    html += '<tr><th>Total</th><th>%s</th></tr>' % total_issues
    html += '</table>'
    return html

if __name__ == '__main__':
    app.run(debug=True)
