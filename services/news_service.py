import os
import requests

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

def get_latest_news():
    url = f"https://newsapi.org/v2/top-headlines?category=business&apiKey={NEWSAPI_KEY}"
    r = requests.get(url)
    return r.json()
