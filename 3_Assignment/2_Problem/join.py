import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
	order_id = record[1]
	mr.emit_intermediate(order_id, record)

def reducer(key, records):
	order = []
	for record in records:
		if record[0] == 'order':
			order = record
			break
	for record in records:
		if record[0] != 'order':
			mr.emit(order + record)

if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
