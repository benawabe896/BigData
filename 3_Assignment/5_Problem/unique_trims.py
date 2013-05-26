import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	mr.emit_intermediate(record[1][:-10], 1)

def reducer(key, records):
	mr.emit(key)

if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
