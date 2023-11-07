#!/usr/bin/python3
"""API ADV Module"""
import requests


def top_ten(subreddit):
    """Returns the top ten subreddit"""
    # Reddit API endpoint for hot posts in the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'MyRedditBot/2.0 (by leonardnzekwe)'
    }

    # Make a GET request to the Reddit API with allow_redirects=False
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # If the request was successful (status code 200)
            # Parse the JSON response and print post titles
            data = response.json()
            # Extract the list of posts
            posts = data['data']['children']
            if not posts:
                # No hot posts found in this subreddit
                print(None)
            else:
                # Print the titles of the first 10 hot posts
                for post in posts[:10]:
                    print(post['data']['title'])
        except Exception:
            # If the subreddit is invalid or there's an issue, print None
            print(None)
    else:
        # If the subreddit is invalid or there's an issue, print None
        print(None)
