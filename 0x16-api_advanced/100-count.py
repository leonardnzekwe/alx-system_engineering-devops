#!/usr/bin/python3
"""API ADV Module"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    To implement a recursive function that queries the Reddit API,
    parses the titles of all hot articles,
    and prints a sorted count of given keywords
    """
    # Initialize word_count and hot_list on the first call
    if word_count is None:
        word_count = {}
    if after is None:
        after = ""

    # Reddit API endpoint for hot posts in the given subreddit
    url = (
        f"https://www.reddit.com/r/{subreddit}"
        f"/hot.json?limit=100&after={after}"
    )

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'MyRedditBot/4.0 (by leonardnzekwe)'
    }

    # Make a GET request to the Reddit API with allow_redirects=False
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            posts = data['data']['children']

            # Parse titles of the current page's posts and update word_count
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word in title:
                        word_count[word] = (
                            word_count.get(word, 0) + title.count(word)
                        )

            # Check if there are more pages of results
            if data['data']['after'] is not None:
                # Recursively call the function with the 'after' parameter
                return count_words(
                    subreddit, word_list, data['data']['after'], word_count
                )
            else:
                # No more pages, print the sorted word_count
                print_results(word_count)
        except Exception:
            # Handle other potential error cases
            pass
    else:
        # If the subreddit is invalid, print nothing
        # Handle other potential error cases
        pass


def print_results(word_count):
    """
    Sort the word_count dictionary by count (descending)
    and then alphabetically (ascending)
    """
    sorted_word_count = sorted(
        word_count.items(), key=lambda item: (-item[1], item[0])
    )

    # Print the results
    for word, count in sorted_word_count:
        print(f"{word}: {count}")
