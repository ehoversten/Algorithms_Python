import requests

url = "https://news.ycombinator.com/"
res = requests.get(url)

print(f"your request for {url} came back w/ status code {res.status_code}")
