t = int(input())

for x in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  l = len(a)
  ans = -1  
  for k in range(1, n+1):
    # print(n % k)
    if n % k == 0:
      mx = float('-inf')
      mn = float('inf')
      for i in range(0, n, k):
        # print(i, n, k)
        sm = sum(a[i:i+k])
        mx = max(mx, sm)
        mn = min(mn, sm)
        
    ans = max(ans, mx - mn)
  
  print(ans)
  