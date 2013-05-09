import sys, json

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	scores = {} # initialize an empty dictionary
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	for line in tweet_file:
		sent_total = 0
		line = json.loads(line)
		if "text" in line:
			notFound = []
			for word in line['text'].encode('utf-8').split():
				if word in scores:
					sent_total += scores[word]
				else:
					notFound.append(word)
			for word in notFound:
				scores[word] = sent_total

	for word in scores:
		print word, " ", scores[word]

if __name__ == '__main__':
	main()
