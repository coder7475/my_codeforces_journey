n = int(input())

for i in range(n):
  n, m = map(int, input().split())
  k = n / m
  output = ((k * (k + 1)) / 2) * m 
  print(int(output))