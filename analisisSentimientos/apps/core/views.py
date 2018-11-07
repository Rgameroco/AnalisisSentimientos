from django.http import HttpResponse
from django.template.loader import get_template
import tweepy
import csv
####input your credentials here
def apiT():
    access_token = "586001493-NdLPS3xAKJAbIdDY7IMtqs4jhR6iR7mTzVpqAXQC"
    access_token_secret ="5AKeeekDw1wnNSNyn4xB9K6x2H0HZiOVFGKbF0yVEo1Ur"
    consumer_key = "1r5eMVn1UZBxpdfsAO5nyWNsU"
    consumer_secret = "14EvbQM8q96zHG0uxmJyLGGdR3bcrSvS1Ski0TgrgIDeKZibqQ"
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

def index(request):
    t = get_template('index.html')
    c= {'foo':'bar'}
   # apiT()
    return HttpResponse(t.render(c,request))