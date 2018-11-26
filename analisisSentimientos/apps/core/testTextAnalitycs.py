#from aylienapiclient import textapi

#client = textapi.Client("e5728c94", "568473446db3ed39da8afe632231f6a1")

#sentiment = client.Sentiment({'text': 'John is a very good football player!'})

#print(sentiment)
from repustate import Client
client = Client(api_key='59e4259067b6a7dcc03e89fa73c1c7e92c5131c5', version='v4')
var = client.categorize(text="Yo odio los hoteles", niche="hotel",lang='es')
parse = var['accommodations']
print(parse)
print(parse[0]['sentiment_text'])
