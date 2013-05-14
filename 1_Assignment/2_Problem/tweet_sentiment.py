import sys, json

def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	#hw()
	#lines(sent_file)
	#lines(tweet_file)

	scores = {} # initialize an empty dictionary
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items() # Print every (term, score) pair in the dictionary

	for line in tweet_file:
		sent_total = 0
		line = json.loads(line)
		if "text" in line:
			for word in line['text'].split(' '):
				if word in scores:
					sent_total += scores[word]
		print sent_total

if __name__ == '__main__':
	main()
