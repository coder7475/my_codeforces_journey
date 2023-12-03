given = input()


if given.isupper() or given[1:].isupper() or len(given) == 1 :
  print(given.swapcase())
else:
  print(given)