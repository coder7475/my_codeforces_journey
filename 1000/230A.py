s, n = map(int, input().split())
val = {}

for i in range(n):
  xi, yi = map(int, input().split())
  if val.get(xi):
    val[xi] += yi
  else:
    val[xi] = yi

# print(val)
arr = dict(sorted(val.items()))
# print(arr)
ans = True
for v in arr:
  if (s <= v):
    ans = False
    break
  else:
    s += val[v]

# print(ans)
if (ans):
  print("YES")
else:
  print("NO")