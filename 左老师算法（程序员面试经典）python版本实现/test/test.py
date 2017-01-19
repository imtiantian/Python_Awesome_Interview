def test():
    return 1 == 2 and 1 or 2
metric = [[x for x in range(5*(y-1), 5*y)] for y in range(1,6)]
for i in range(5):
    print metric[i]

print metric[3][3]
print metric[2][3]
print metric[3][2]
# print(test())