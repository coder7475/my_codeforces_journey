n = int(input())

blocks = list(map(int, input().split()))
blocks.sort()

for block in blocks:
  print(block, end=" ")

print("")