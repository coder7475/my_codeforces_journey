hash = {}

for i in range(int(input())):
  s = input()

  if s in hash:
    print(s + str(hash[s]))
    hash[s] += 1
  else:
    hash[s] = 1
    print("OK")