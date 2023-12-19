for i in range(int(input())):
  found = True
  n = input()
  l = len(n)

  for x in range(1, l):
    if n[x+1] != '0' or (int(n[x]) < int(n[x-1])):
      found = False
      print(n[0:x], n[x:])
      break
  
  if found:
    print('-1')

