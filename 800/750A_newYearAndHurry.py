n, k = map(int, input().split())

leaveTime = (4 * 60) - k
time = 0
solvedProb = 0

for i in range(1, n+1):
  time += i * 5;
  if (time <= leaveTime):
    solvedProb += 1

print(solvedProb)