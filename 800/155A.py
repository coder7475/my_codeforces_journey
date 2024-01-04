n = int(input())

ratings = list(map(int, input().split()))

low = ratings[0]
high = ratings[0]
p = 0

for i in range(1, n):
  if (ratings[i] > high):
    high = ratings[i]
    p += 1
  elif (ratings[i] < low):
    low = ratings[i]
    p += 1

print(p)