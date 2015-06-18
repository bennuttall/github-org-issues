from flask import Flask
import github_org_issues as goi

app = Flask(__name__)

@app.route('/')
def index():
    org = "raspberrypilearning"
    repos = goi.get_org_repos_with_open_issues(org)
    html = '<ul>'
    for repo in repos:
        repo_name = repo['name'].replace('-', ' ')
        open_issues_count = repo['open_issues_count']
        repo_url = repo['html_url']
        issues_url = '%s/issues' % repo_url
        html += '<li><a href="%s">%s - %i</a></li>' % (issues_url, repo_name, open_issues_count)
    html += '</ul>'
    return html

if __name__ == '__main__':
    app.run(debug=True)
