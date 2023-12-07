n, m = map(int, input().split())

f = list(map(int, input().split()))

f.sort()

output = float('inf')

for i in range(m - n + 1):
  output = min(output, f[i+n-1] - f[i])

print(output)