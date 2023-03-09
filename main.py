# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""

import tweepy
import emoji
import csv

def get_user_tweets(username, count):

    api_key = 'JYfrYIj1Jb9KwlkTQwN34Sifg'
    api_key_secret = '8wW8EE6sdemGOK2dTK3cFbfdVkdeEO0itv4voKw2VvSmuBxSLh'
    access_token = '973565211411173377-zYi3gDCM6KxMtnD8vGJqF9s6AQ8CUWP'
    access_token_secret = 'bd7e98s7k55zIGHcR5SByLHUMRGbdfvKh0JyCuhaO5zEi'

    # authenticate with twitter api
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    # create tweepy api object
    api = tweepy.API(auth)

    # get latest tweets
    raw_tweets = api.user_timeline(screen_name=username, count=count)

    # if tweets is empty
    if not raw_tweets:
        print('No tweets found for user: ', username)
        return

    # store parsed tweets in a separate list of dictionaries
    tweets = []
    for tweet in raw_tweets:
        parsed_tweet = {}
        parsed_tweet['text'] = emoji.demojize(tweet.text.replace("'", "''")).encode('utf-8').decode('utf-8', 'ignore')
        parsed_tweet['created_at'] = tweet.created_at.strftime('%d-%m-%Y %H:%M:%S')
        parsed_tweet['username'] = tweet.user.screen_name
        tweets.append(parsed_tweet)

    # loop through tweets
    with open(f'{username}_tweets.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'created_at', 'text'])
        writer.writeheader()
        for tweet in tweets:
            writer.writerow(tweet)


def get_query_tweets(keywords, count=100):

    api_key = 'JYfrYIj1Jb9KwlkTQwN34Sifg'
    api_key_secret = '8wW8EE6sdemGOK2dTK3cFbfdVkdeEO0itv4voKw2VvSmuBxSLh'
    access_token = '973565211411173377-zYi3gDCM6KxMtnD8vGJqF9s6AQ8CUWP'
    access_token_secret = 'bd7e98s7k55zIGHcR5SByLHUMRGbdfvKh0JyCuhaO5zEi'

    # authenticate with twitter api
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    # create tweepy api object
    api = tweepy.API(auth)

    # get latest tweets
    query = ' OR '.join(keywords)
    since_date = '2022-01-01'
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang='en', since_id=since_date, tweet_mode='extended').items(count)

    # write tweets to csv
    with open(f'{keywords}_tweets.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'created_at', 'text'])
        writer.writeheader()
        for tweet in tweets:
            username = tweet.user.screen_name
            created_at = tweet.created_at.strftime('%Y-%m-%d')
            text = tweet.full_text.replace("’", "'").encode('utf-8').decode('utf-8')
            writer.writerow({'username': username, 'created_at': created_at, 'text': text})


get_query_tweets(['longanisa'], 50)