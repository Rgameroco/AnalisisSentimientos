import tweepy
import csv
####input your credentials here
def apiT():
    access_token = "2773047815-5nuQ1prxxHti09jrw7MMa5uSGjofs8YoJ1LROko"
    access_token_secret ="wCOCT3zlU8vAyCV3sD5NHMRj4EkMq7YKDkojilLqpfxeN"
    consumer_key = "rHZMCHgvciQz8neRlJvskyUHO"
    consumer_secret = "QSJpXdMdupLUTswuJKdXGn0EJfUFOX9jRZArMZ2hX5BG5egSEh"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    apis = tweepy.API(auth,wait_on_rate_limit=True)
    #####United Airlines
    # Open/Create a file to append data
    csvFile = open('ua.csv', 'a')

    #Use csv Writer
    csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(apis.search,q="#Trump",count=100,lang="en",since="2017-04-03").items():
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])