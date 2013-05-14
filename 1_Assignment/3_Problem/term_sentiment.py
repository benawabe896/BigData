import sys, json

def getScores(sent_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	return scores

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	scores = getScores(sent_file)

	newscores = {}
	for line in tweet_file:
		tweet_total = 0
		line = json.loads(line)
		if "text" in line:
			words = line['text'].encode('utf-8').split()
			for word in words:
				if word in scores:
					tweet_total += scores[word]
			for word in words:
				if word not in scores:
					if word not in newscores:
						newscores[word] = []
					newscores[word].append(tweet_total)

	for word in newscores:
		wordscore = sum(newscores[word]) / float(len(newscores[word]))
		print " ".join([word, str(wordscore)])

if __name__ == '__main__':
	main()
