# Automate this scipt on Pythonanywhere for free to tweet automatically

import tweepy
import requests

# Get these credentials for free from twitter developer's account
api_key = "Your API KEY"
api_secret = "Your API Secret"
bearer_token = r"Your Bearer Token"
access_token = "Your Access Token"
access_token_secret = "Your Access Token Secret"

client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key,api_secret,access_token,access_token_secret)
api = tweepy.API(auth)



# Function to get a random quote from They Said So API
def get_random_quote():
    url = f'https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&category=inspire'
    response = requests.get(url)
    data = response.json()
    return data["quoteText"]


# This is to Tweet the quote 
client.create_tweet(text=f"{get_random_quote()} \n#Xmoon #Quotes #Happiness") 