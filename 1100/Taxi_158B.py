n = int(input())
members = list(map(int, input().split()))

count = {
  1: 0,
  2: 0,
  3: 0,
  4: 0
}

for num in members:
  count[num] += 1

# print(count)
total = count[4] + count[3] + count[2] // 2

count[1] -= count[3]
if ( count[2] % 2 == 1):
  total += 1
  count[1] -= 2

if (count[1] > 0 ):
  total += (count[1] + 3) // 4

print(total)