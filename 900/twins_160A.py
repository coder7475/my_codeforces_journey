# Input: Number of Coins
n = int(input())

# Inputs: Value of each coins
coins = list(map(int, input().split()))
coins.sort(reverse=True)
total = sum(coins)
half = total / 2

count = 0
money = 0

for coin in coins:
  money += coin
  count += 1
  if (money > half):
    break
  

print(count)