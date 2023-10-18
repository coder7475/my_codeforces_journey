for i in range(1, 6):
	x = input().split()
	for j in range(1, 6):
		val = int(x[j-1])
		if val == 1:
			print(abs(i-3)+abs(j-3))
