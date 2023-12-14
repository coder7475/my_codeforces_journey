x = input()
y = input()
n = len(x)
a = ''
for i in range(n):
  if x[i] == y[i]:
    a += '0'
  else:
    a += '1'

print(a)