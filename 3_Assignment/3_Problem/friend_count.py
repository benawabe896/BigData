import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	key = record[0]
	mr.emit_intermediate(key, 1)

def reducer(key, counts):
	mr.emit((key, sum(counts)))

if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
