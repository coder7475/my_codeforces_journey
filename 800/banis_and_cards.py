t = int(input())

for i in range(t):
  n, m = map(int, input().split())

  k = n // m
  ans = (k * (k+1) * m) // 2

  print(ans)