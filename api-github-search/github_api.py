import requests

url="https://api.github.com/search/repositories"
params={
    "q":"python",
    "per_page":5,
    "sort":"stars",
    "order":"desc"
}

res=requests.get(url, params=params)

data=res.json()

for repo in data["items"]:
    name=repo["full_name"]
    stars=repo["stargazers_count"]
    print(f"repo_name={name},star_count={stars}")

