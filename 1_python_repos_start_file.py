import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

outfile = open('output.json', 'w')

response_dict = r.json()

json.dump(response_dict, outfile, indent=4)

list_of_repos = response_dict['items']
print(f"Number of repos: {len(list_of_repos)}")

def print_all_repos(list_of_repos):
    for i, repo in enumerate(list_of_repos):
        print(f"{i + 1}: {repo['name']}")
        print('    ' + repo['owner']['login'])
        print('    ' + str(repo['stargazers_count']))
        print('    ' + repo['html_url'])
        print('    ' + repo['created_at'])
        print('    ' + repo['updated_at'])
        print('    ' + repo['description'] if repo['description'] else None)

def print_repo(repo):
    print(repo['name'])
    print('    ' + repo['owner']['login'])
    print('    Stars: ' + str(repo['stargazers_count']))
    print('    ' + repo['html_url'])
    print('    Created: ' + repo['created_at'])
    print('    Updated: ' + repo['updated_at'])
    print('    ' + repo['description'] if repo['description'] else None)

print_repo(list_of_repos[0])

repos, stars = [], []

for repo in list_of_repos[:10]:
    repos.append(repo['name'])
    stars.append(repo['stargazers_count'])

from plotly.graph_objs import Bar
from plotly import offline

data = [
    {
        'type': 'bar',
        'x': repos,
        'y': stars,
        'marker': {
            'color': 'rgb(200, 0, 0)',
            'line': {'width': 1.5, 'color': 'rgb(0, 0, 200)'},
        },
        'opacity': 0.6
    }
]

my_layout = {
    'title': "Most-Starred Python Repos on GitHub",
    'xaxis': {'title': "Repository Name"},
    'yaxis': {'title': "Star Count"}
}

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename="python_repos.html")