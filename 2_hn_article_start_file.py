import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
#print(f"Status code: {r.status_code}")

# Explore the structure of the data.
outfile = open('hn.json', 'w')
json.dump(r.json(), outfile, indent=4)
id_list = r.json()
# ID 35457341
url = 'https://hacker-news.firebaseio.com/v0/item/35457341.json'
r = requests.get(url)
outfile = open('hn2.json', 'w')
json.dump(r.json(), outfile, indent=4)
json = json.dump(r.json(), outfile, indent=4)

articles = {}

# Grab top ten lists
for index, id in enumerate(id_list[:10]):
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json'
    r = requests.get(url)
    articles[str(id)] = r.json()
    print(f"{index + 1}: {url}")
    print(f"{articles[str(id)]['title']}")
    try:
        print(f"Number of comments: {articles[str(id)]['descendants']}\n")
        pass
    except:
        articles[str(id)]['descendants'] = '0'
        print(f"Number of comments: {articles[str(id)]['descendants']}\n")
        pass

for article in sorted(articles, key=lambda x: int(articles[x]['descendants']), reverse=True):
    print(f"Article: {articles[article]['title']} Comments: {articles[article]['descendants']}")
    print()