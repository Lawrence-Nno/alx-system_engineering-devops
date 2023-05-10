#!/usr/bin/python3
"""This function queries subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """This returns the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    respons = requests.get(url, headers=headers, allow_redirects=False)
    if respons.status_code == 404:
        return 0
    outcome = respons.json().get("data")
    return outcome.get("subscribers")
