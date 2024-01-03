n, l = map(int, input().split())

a = list(map(int, input().split()))

a.sort()
r = max(a[0], l - a[-1]) * 2;

for i in range(n-1):
  r = max(r, a[i+1] - a[i])

print(r/2)