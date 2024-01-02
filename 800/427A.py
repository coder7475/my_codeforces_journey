n = int(input())
events = list(map(int, input().split()))

hired = 0
untreated = 0

for event in events:
  if (event >= 1):
    hired += event
    continue
  
  if (event == -1):
    if (hired > 0):
      hired -= 1
    else:
      untreated += 1

print(untreated)