import urllib
import json, sys

base = "http://search.twitter.com/search.json";
maxPages = 10

for i in range(1,maxPages+1):
	params = {"q":"microsoft", "page":i}
	response = urllib.urlopen("http://search.twitter.com/search.json?" + urllib.urlencode(params))
	jsonResult = json.load(response)
	results = jsonResult['results']
	for tweet in results:
		print tweet['text']
