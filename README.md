# Birdtooter
A simple Python app to copy new tweets from a specified Twitter user to a single Mastodon account. Created by @ericrosenberg1 to automate posting from [@VenturaCityNews](https://twitter.com/venturacitynews) on Twitter to [venturacitynews@mas.to](https://venturacitynews@mas.to/@VenturaCityNews) on Mastodon. You can update to copy any Twitter account to Mastodon for your 10 latest tweets with no duplicates.

## How it works
Birtdtooter uses the Twitter API and Mastodon API to find new tweets and add them to Mastodon. Tweets IDs are stored using a SQLite database to prevent duplicates. The Python3 app requires tweepy, Mastodon.py, and sqlite3.

I created this to run on my Raspberry Pi, though it would work in any environment supporting Python3 and other necessary dependencies. It should work on any server, AWS, Heroku, or your favorite app hosting platform.

## Is it for you?
If you know how to download and run a simple Python app using the command line and how to schedule a CRON job on your server, you can probably figure out the setup. If you don't know what **SUDO apt-get** means or don't understand the instruction "use cd to navigagte to the birdtooter folder in your chosen directory," you may want to hire a developer to set this up for you.

## Installation and setup
1. Use Git Clone or download the .zip version of the app from Github. If you download the .zip version, extract to the directory where you want to host the app. Before cloning, navigate to the directory you want to use with the cd command.

    '''$ git clone https://github.com/ericrosenberg1/birdtooter'''

2. Install tweepy, Mastodon.py, and squlite3.

    '''pip install tweepy mastodon.py sqlite3'''

3. Prepare the constants.py file

  1. Generate or find your Twitter V2 API credentials following these [instructions](https://developer.twitter.com/en/support/twitter-api/v2).
  1. Generate or find your Mastodon API credentials following these [instructions](https://shkspr.mobi/blog/2018/08/easy-guide-to-building-mastodon-bots/).
  1. Copy constants_example.py and rename the new version constants.py.
  1. Add the Twitter API and Mastodon API credentials to the constants.py file. Update the Twitter account username, without the @ sign.

4. Test in your favorite IDE or command line

Use cd to navigate to the directory where you downloaded and run birdtoot.py.

'''$ Python3 birdtoot.py'''
  
If everything is working, you should see a success message. If there are any failures, you may need to troubleshoot. Common issues are not using the wrong Python version, not having the correct dependencies installed, using the wrong API credentials or version, or attempting to run the file from the wrong directory.

5. Schedule a CRON job to run the bot

I like running the job every five minutes, but you can use your own schedule. Follow these instructions to [set up a CRON job](https://bc-robotics.com/tutorials/setting-cron-job-raspberry-pi/) on a Rasbperry Pi or similar Linux systems. Here is an example to get you started, but it will need editing.

I set this up using crontab in the default command line editor, but you can use something fancier if you want.

From the command line, enter:

'''$ crontab -e'''
    
Add this line to the bottom of your CRON jobs section. Update the bold text with your installation directory.

'''#TwitterToMastodonBot
*/5 * * * * python3 **/home/username/code**/birdtooter/birdtoot.py'''

Wait five minutes. If there are new Tweets, they should automatically copy to your linked Mastodon account. That's it! You're up and running.

## Support, contributions, and improvements
v1.0 developed by Eric Rosenberg @ericrosenberg1. I relied heavily on ChatGPTv3 to cobble this together, and plundered code from other projects I've built.

I would be thrilled to merge in new improvements and give you credit as a contributor. Ideas include changing the maximum number of posts via the constants file for anyone looking to move their full account history, support for multiple Twitter or Mastodon accounts, improvements to the Mastodon posting, expanding t.co and other shortlinks for transparency, improved media handling, better installation and setup scripts, tweet filters by hashtag or keyword, and anything else you think may make this better.

## About me
Eric Rosenberg is a hobbiest developer and mostly a writer about financial topics. Connect and learn more at [EricRosenberg.com](https://ericrosenberg.com).
