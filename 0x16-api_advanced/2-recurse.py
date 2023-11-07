#!/usr/bin/python3
"""API ADV Module"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Returns a list containing the titles
    of all hot articles for a given subreddit
    """
    # Initialize hot_list on the first call
    if hot_list is None:
        hot_list = []

    # Reddit API endpoint for hot posts in the given subreddit
    url = (
        f"https://www.reddit.com/r/{subreddit}"
        f"/hot.json?limit=100&after={after}"
    )

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'MyRedditBot/3.0 (by leonardnzekwe)'
    }

    # Make a GET request to the Reddit API with allow_redirects=False
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            posts = data['data']['children']

            # Append the titles of the current page's posts to hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # Check if there are more pages of results
            if data['data']['after'] is not None:
                # Recursively call the function with the 'after' parameter
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                # No more pages, return the complete hot_list
                return hot_list
        except Exception:
            # Handle other potential error cases
            return None
    else:
        # Handle other potential error cases or
        # If the subreddit is invalid, return None
        return None
