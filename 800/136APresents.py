n = int(input())

gifts = list(map(int, input().split()))
ans = [0]*n

for index in range(n):
  gift_to = gifts[index] - 1
  ans[gift_to] = index + 1

print(*ans, sep=' ')