#!/usr/bin/python3
"""number of subs for a subreddit"""
from requests import get

def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    user = {'User-agent': 'Google Chrome Version 123.0.6312.106'}
    Url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(Url, headers=user)
    res = response.json()

    try:
        return res.get('data').get('subscribers')
    except Exception:
        return 0
