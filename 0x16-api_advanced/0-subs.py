#!/usr/bin/python3
""" Using Reddit API """

import requests


def number_of_subscribers(subreddit):
    """ Function that returns the number of subscribers """

    header = {'user-agent': 'Sorec21'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(url, headers=header, allow_redirects=False)

    if req.status_code == 200:
        return req.json().get('data').get('subscribers')
    else:
        return 0
