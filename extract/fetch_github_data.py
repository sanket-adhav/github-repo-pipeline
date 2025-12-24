import requests

def fetch_repo_data(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("GitHub API request failed")

    return response.json()
