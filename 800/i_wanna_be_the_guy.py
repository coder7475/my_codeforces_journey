level = set(range(1, int(input()) + 1))
x = list(map(int, input().split()[1:]))
y = list(map(int, input().split()[1:]))

if level - set(x + y) == set():
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
