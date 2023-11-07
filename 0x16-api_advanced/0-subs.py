#!/usr/bin/python3
"""API ADV Module"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'MyRedditBot/1.0 (by leonardnzekwe)'
    }

    # Make a GET request to the Reddit API with allow_redirects=False
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers from the response
            subscribers = data['data']['subscribers']
            return subscribers
        except Exception:
            # If the subreddit is invalid or there's an issue, return 0
            return 0
    else:
        # If the subreddit is invalid or there's an issue, return 0
        return 0
