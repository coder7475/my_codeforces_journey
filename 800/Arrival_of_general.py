n = int(input())
a = list(map(int, input().split()))

min_val = a[0]
max_val = a[0]
min_ind = 0
max_ind = 0

for i in range(n):
  if (a[i] > max_val):
    max_ind = i
    max_val = a[i]
  if (a[i] <= min_val):
    min_ind = i
    min_val = a[i]

if (max_ind > min_ind):
  print((max_ind-1)+(n-min_ind)-1)
else:
  print(max_ind-1+n-min_ind)