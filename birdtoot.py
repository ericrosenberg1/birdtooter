# Import the necessary libraries
import tweepy
from mastodon import Mastodon
import sqlite3
from constants import *

# Import the API keys from the constants file
import constants
TWITTER_CONSUMER_KEY = constants.TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET = constants.TWITTER_CONSUMER_SECRET
TWITTER_ACCESS_TOKEN = constants.TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET = constants.TWITTER_ACCESS_SECRET
MASTODON_CLIENT_ID = constants.mastodon_client_id
MASTODON_CLIENT_SECRET = constants.mastodon_client_secret
MASTODON_ACCESS_TOKEN = constants.mastodon_access_token
MASTODON_BASE_URL = constants.mastodon_base_url

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Authenticate with the Mastodon API
mastodon = Mastodon(client_id=MASTODON_CLIENT_ID, client_secret=MASTODON_CLIENT_SECRET, access_token=MASTODON_ACCESS_TOKEN, api_base_url=MASTODON_BASE_URL)

# Connect to the SQLite database
conn = sqlite3.connect('tweet_ids.db')
cursor = conn.cursor()

# Create the table to store tweet IDs if it doesn't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tweet_ids (
            id INTEGER PRIMARY KEY,
                    tweet_id TEXT NOT NULL
                        )
                        ''')
conn.commit()

# Find the 10 latest tweets in the specified Twitter account
username = constants.twitter_handle
tweets = api.user_timeline(screen_name=username, count=10, tweet_mode='extended')

# Post each tweet to Mastodon and save it to the database
for tweet in tweets:
    # Check if the tweet has already been posted
    cursor.execute('''
        SELECT * FROM tweet_ids WHERE tweet_id=?
    ''', (tweet.id,))
    result = cursor.fetchone()
    if result is None:
        # Tweet has not been posted, so post it to Mastodon
        mastodon.status_post(tweet.full_text, visibility='public')

        # Optionally, attach any media from the tweet to the Mastodon post
        if 'media' in tweet.entities:
            media_ids = []
            for media in tweet.entities['media']:
                media_response = requests.get(media['media_url'], stream=True)
                media_ids.append(mastodon.media_post(media_response.raw))
            mastodon.status_post(tweet.full_text, media_ids=media_ids, visibility='public')

        # Save the tweet to the database
        cursor.execute('''
            INSERT INTO tweet_ids (tweet_id) VALUES (?)
        ''', (tweet.id,))
        conn.commit()

# Close the database connection
conn.close()

print ('Successfully Tooted!')
