tuple1 = (12,6, -8, 'Jenny', True)
#print(tuple1[4])
#print(type(tuple1))

tuple2 = (24, 56, 34, 89)
tuple3 = (tuple1, tuple2)
print(tuple3)

print(tuple3[1])

tuple4 = tuple3 + tuple2

print(tuple4)

list1 = [1, 2, 3, 4, 7]

print(tuple(list1))