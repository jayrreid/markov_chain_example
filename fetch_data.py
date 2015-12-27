__author__ = 'jrreid'
import urllib2
from bs4 import BeautifulSoup
from twitter import *
import re

def fetch(url):
    # connect to url
    response = urllib2.urlopen(url)

    # read contents of html website
    html = response.read()

    # remove html tags
    soup = BeautifulSoup(html, 'html.parser')

    # always return the html head title of the website
    return soup.html.head.title.string

def fetch_tweets(handle):
    t = Twitter(
    auth=OAuth( '840045282-riS7ga6dS08SCc1sB40ww9qgqxqdivXQHCgV6BvJ','QkUYC6v4akwEAhlkOsE0cfYZYyiTpdrZsCYwnZRNfZqVh', 'bZYrtptA6oPUCAvVPo5PI0xdS','W5d2wunmph5mZyXhuT5Fupgu4YkQv8R0gol4JVlb3Gg9pQbVUW'))
    results = t.search.tweets(q="from:" +handle,count=50)
    statuses = results['statuses']

    tweets=[]
    for item in statuses:
        text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', item['text'])
        tweets.append(text)
    return tweets