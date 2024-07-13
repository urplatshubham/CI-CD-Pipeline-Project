import requests

# GitHub repository information
username = 'urplatshubham'
repo_name = 'CI-CD-Pipeline-Project'
access_token = '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'  # Generate a personal access token from GitHub

# API endpoint for getting repository stats
api_url = f'https://api.github.com/repos/{username}/{repo_name}/stats/participation'

# Headers with Authorization using access token
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3+json'
}

try:
    # Fetch repository stats from GitHub
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad responses

    stats = response.json()

    # Calculate total commits
    total_commits = sum(stats['all'])

    print(f"Total commits in {repo_name}: {total_commits}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching repository stats: {e}")
