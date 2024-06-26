#!/usr/bin/python3
"""queries to the Reddit API and print the titles of
the first 10 hot posts listed for a given subreddit."""
from requests import get
from sys import argv


def top_ten(subreddit: str):
    headers = {
        "User-Agent": "Just a bunch of crap",
        "X-Forwared-For": "Amaterasu"
    }

    request_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        response = get(request_url, headers=headers,
                       allow_redirects=False).json()
        data = response['data']['children']
        [print(post['data']['title']) for post in data[:10]]
    except Exception:
        print("None")


if __name__ == "__main__":
    (top_ten(argv[1]))
