#!/usr/bin/python3
""" Using Reddit API """

import requests


def recurse(subreddit, hot_list=[], after=''):
    """Function that queries Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit"""

    header = {'user-agent': 'Sorec21'}
    param = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit,
        after
    )
    req = requests.get(
        url,
        headers=header,
        allow_redirects=False
    )

    if req.status_code == 200:
        hot_list += req.json().get("data", {}).get("children", [])
        after_aux = req.json().get("data", {}).get("after", None)

        if after_aux:
            return recurse(subreddit, hot_list=hot_list, after=after_aux)
        else:
            return hot_list
