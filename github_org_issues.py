import requests
import json

def get_org_repos(org):
    r = requests.get("https://api.github.com/orgs/%s/repos" % org)
    repos = json.loads(r.text)
    return repos

def get_org_repos_with_open_issues(org):
    repos = get_org_repos(org)
    return [repo for repo in repos if repo['open_issues']]

def main():
    org = "raspberrypilearning"
    repos = get_org_repos_with_open_issues(org)
    for repo in repos:
        repo_path = repo['full_name']
        repo_name = repo_path.split('/')[1]
        open_issues_count = repo['open_issues_count']
        print('%s - %i' % (repo_name, open_issues_count))

if __name__ == '__main__':
    main()
