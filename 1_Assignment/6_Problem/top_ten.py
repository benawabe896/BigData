import sys, json, operator

def main():
	tweet_file = open(sys.argv[1])

	scores = {} # initialize an empty dictionary

	for line in tweet_file:
		line = json.loads(line)
		if "entities" in line:
			entities = line['entities']
			if "hashtags" in entities:
				hashtags = line['entities']['hashtags'] 
				for hashtag in hashtags:
					text = hashtag['text']	
					if text not in scores:
						scores[text] = 0
					scores[text] += len(hashtag['indices']) / 2
	sorted_x = sorted(scores.iteritems(), key=operator.itemgetter(1), reverse=True)
	top = len(sorted_x) if len(sorted_x) < 10 else 10
	for x in range(0,top):
		print " ".join([sorted_x[x][0], str(float(sorted_x[x][1]))])

if __name__ == '__main__':
	main()
