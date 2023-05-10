#!/usr/bin/python3
"""This function prints hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """This prints the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    param = {
        "limit": 10
    }
    respons = requests.get(url, headers=headers, param=param,
                            allow_redirects=False)
    if respons.status_code == 404:
        print("None")
        return
    outcome = respons.json().get("data")
    [print(c.get("data").get("title")) for c in outcome.get("children")]
