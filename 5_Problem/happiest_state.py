import sys, json

states = {
	'AK': 'Alaska',
	'AL': 'Alabama',
	'AR': 'Arkansas',
	'AS': 'American Samoa',
	'AZ': 'Arizona',
	'CA': 'California',
	'CO': 'Colorado',
	'CT': 'Connecticut',
	'DC': 'District of Columbia',
	'DE': 'Delaware',
	'FL': 'Florida',
	'GA': 'Georgia',
	'GU': 'Guam',
	'HI': 'Hawaii',
	'IA': 'Iowa',
	'ID': 'Idaho',
	'IL': 'Illinois',
	'IN': 'Indiana',
	'KS': 'Kansas',
	'KY': 'Kentucky',
	'LA': 'Louisiana',
	'MA': 'Massachusetts',
	'MD': 'Maryland',
	'ME': 'Maine',
	'MI': 'Michigan',
	'MN': 'Minnesota',
	'MO': 'Missouri',
	'MP': 'Northern Mariana Islands',
	'MS': 'Mississippi',
	'MT': 'Montana',
	'NA': 'National',
	'NC': 'North Carolina',
	'ND': 'North Dakota',
	'NE': 'Nebraska',
	'NH': 'New Hampshire',
	'NJ': 'New Jersey',
	'NM': 'New Mexico',
	'NV': 'Nevada',
	'NY': 'New York',
	'OH': 'Ohio',
	'OK': 'Oklahoma',
	'OR': 'Oregon',
	'PA': 'Pennsylvania',
	'PR': 'Puerto Rico',
	'RI': 'Rhode Island',
	'SC': 'South Carolina',
	'SD': 'South Dakota',
	'TN': 'Tennessee',
	'TX': 'Texas',
	'UT': 'Utah',
	'VA': 'Virginia',
	'VI': 'Virgin Islands',
	'VT': 'Vermont',
	'WA': 'Washington',
	'WI': 'Wisconsin',
	'WV': 'West Virginia',
	'WY': 'Wyoming'
}

states = dict((k.lower(),v.lower()) for k,v in states.items())
states2 = dict((v,k) for k,v in states.items())

def getState(location):
	for word in location.split():
		if word.lower() in states2:
			return states2[word.lower()].upper()
		if word.lower() in states:
			return word.upper()
	return ''

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	state_sentiments = {}

	scores = {} # initialize an empty dictionary
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	for line in tweet_file:
		line = json.loads(line)
		if "text" in line:
			sent_total = 0
			state = getState(line['user']['location'])
			if len(state):
				for word in line['text'].encode('utf-8').split():
					if word in scores:
						sent_total += scores[word]
				if state not in state_sentiments:
					state_sentiments[state] = 0
				state_sentiments[state] += sent_total
	for state in state_sentiments:
		print state, " ", state_sentiments[state]

if __name__ == '__main__':
	main()
