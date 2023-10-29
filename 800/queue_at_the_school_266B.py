n, t = map(int, input().split())
s = list(input())

while t:
  l = len(s)
  t -= 1
  i = 1
  while i < l:
    if s[i] == 'G' and s[i - 1] == 'B':
      s[i] = 'B'
      s[i - 1] = 'G'
      i += 1
    i += 1
  
print("".join(s))