list1= ["hi", "hello","Welcome"]
names= ["Krishn", "Ram", "Madhav"]
for i in list1:
    for name in names:
        print(i, name)
        if i == "hello" and name == "Ram":
            break
    print("out of inner loop")
print("in outer loop")
