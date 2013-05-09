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
			notFound = []
			for word in line['text'].encode('utf-8').split():
				if word not in scores and word not in newscores:
					newscores[word] = 0
					notFound.append(word)
				else:
					if word in scores:
						tweet_total += scores[word]
			for word in notFound:
				newscores[word] += tweet_total

	for word in newscores:
		print word, " ", newscores[word]

if __name__ == '__main__':
	main()


