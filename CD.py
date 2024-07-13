import requests

def get_commit_count(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        return len(commits)
    else:
        print(f"Error: Unable to fetch commits (Status Code: {response.status_code})")
        return None

if __name__ == "__main__":
    owner = "urplatshubham"  
    repo = "CI-CD-Pipeline-Project"  

    commit_count = get_commit_count(owner, repo)
    
    if commit_count is not None:
        print(f"The number of commits in the repository '{repo}' is: {commit_count}")

