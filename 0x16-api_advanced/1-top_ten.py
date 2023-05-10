#!/usr/bin/python3
"""This function queries a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """This returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parameters = {
        "after": after,
        "count": count,
        "limit": 100
    }
    respons = requests.get(url, headers=headers, parameters=parameters,
                            allow_redirects=False)
    if respons.status_code == 404:
        return None

    outcome = respons.json().get("data")
    after = outcome.get("after")
    count += outcome.get("dist")
    for c in outcome.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
