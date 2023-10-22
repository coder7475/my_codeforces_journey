# Time Complexity: O(n)
n = int(input())
colors = input()
l = len(colors)
# print(l)
prev = 0
ans = 0
# print(prev)
for cur in range(1, l):
  if colors[prev] == colors[cur]:
    ans += 1
  prev += 1

print(ans)