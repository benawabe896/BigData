import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	key = "|".join(sorted(record))
	mr.emit_intermediate(key, record)

def reducer(key, records):
	if len(records) == 1:
		mr.emit((records[0][0], records[0][1]))
		mr.emit((records[0][1], records[0][0]))

if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
