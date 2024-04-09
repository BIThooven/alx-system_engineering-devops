#!/usr/bin/python3
""" a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit"""

from requests import get
from sys import argv


def recurse(subreddit: str, hot_list=[], after="", count=0):
    request_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "minato"
    }
    query_strings = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = get(request_url, headers=headers, params=query_strings,
                   allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json()['data']
    after = results['after']
    count += results['dist']
    for child in results["children"]:
        hot_list.append(child["data"]["title"])

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list


if __name__ == "__main__":
    print(recurse(argv[1]))
