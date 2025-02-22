def string_2_floats(text):
	B=[];C=text.split()
	for D in range(len(C)):
		try:
			A=float(C[D])
			if A!=float('inf')and A!=float('-inf'):B.append(A)
		except ValueError:pass
	return B