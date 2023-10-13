num = int(input())
words = []
for i in range(num):
  word = input()
  l = len(word)
  if l > 10:
    ans = ""
  
    count = 0
    for i in range(l):
      if i != 0 and i != l - 1:
        count+=1

    words.append(word[0] + str(count) + word[l-1])
  else:
    words.append(word)

for word in words:
  print(word)