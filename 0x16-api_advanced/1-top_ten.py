#!/usr/bin/python3
""" Using Reddit API """

import requests


def top_ten(subreddit):
    """Function that queries Reddit API and prints the title of the first
    10 hot posts listed for a given  subreddit"""

    header = {'user-agent': 'Sorec21'}
    param = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(
        url,
        headers=header,
        allow_redirects=False,
        params=param
    )

    if req.status_code == 200:
        children = req.json().get('data').get('children')
        for i in children:
            print(i.get('data').get('title'))
    else:
        print('None')