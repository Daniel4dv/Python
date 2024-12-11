from itertools import count

c1 = count(10,8)
r1 = range(10,100,8)

print('COUNT:')
for i in r1:
    if i<100:
        print(i)
print()
print('RANGE:')
for i in r1:
    if i<100:
        print(i)
# print(next(c1))