import sys, json

def main():
	#sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[1])

	allCount = 0.0
	terms = {}
	for line in tweet_file:
		line = json.loads(line)
		if "text" in line:
			for word in line['text'].encode('utf-8').split():
				if word not in terms:
					terms[word] = 0
				terms[word] += 1
				allCount += 1
	for word in terms:
		print word, " ", terms[word] / allCount

if __name__ == '__main__':
	main()
