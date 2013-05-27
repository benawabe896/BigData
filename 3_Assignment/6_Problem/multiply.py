import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(mx):
	for i in range(0,5):
		key = (mx[1], i) if mx[0] == "a" else (i, mx[2])
		mr.emit_intermediate( key, mx )

def reducer(key, mxs):
	A = {}
	B = {}
	for mx in mxs:
		if mx[0] == "a":
			A[mx[2]] = mx[3]
		else:
			B[mx[1]] = mx[3]
	
	total = 0
	for i in range(0,5):
		if i not in A:
			A[i] = 0
		if i not in B:
			B[i] = 0
		total += A[i] * B[i]

	mr.emit((key[0], key[1], total))

if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
