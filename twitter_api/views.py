import json
import oauth2 as oauth
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def get_tweet(request):
	return render(request, 'twitter.html')

@csrf_exempt
def tweets(request):
    consumer_key = "CcScncvrzNDqtQC1lkDxjbMwP"
    consumer_secret = "5wT2WIJ6kmjAktON9vTTK20QYcEOHy1JJNnTWRlJA9T80SHBZR"

    access_token = "785324212865163264-awsWJiVYsc6z7MamJLiPiadOUcnvvUm"
    access_token_secret ="FcaZzoolbHdwdZWp8ppWpR5kzGUvZhlOLCe0zsdhkAhFj"

    consumer = oauth.Consumer(key = consumer_key, secret = consumer_secret)
    access_token = oauth.Token(key = access_token, secret = access_token_secret)
    client = oauth.Client(consumer, access_token)
    
    username = request.POST.get('user_name')
    print username

    endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count=20"
    response, data = client.request(endpoint)
    tweets = json.loads(data)
    tweet_list = []
    for tweet in tweets:
        tweet_dict = { 'text':tweet['text'], }
        tweet_list.append(tweet_dict)
    print tweet_dict
    return HttpResponse(json.dumps(tweet_list))
    



