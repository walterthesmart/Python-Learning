# def add(*numbers):
#     c = 0
#     for i in numbers:
#         c += i
#     print(f"Sum is {c}")
# add(5,42,24,53,44,122,4)
# add(434,3453,3531,343,232,23242,44,34,35)

# def info_person(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# info_person(name = "Ram", age=30, dept="CSE")
# info_person(name="Shyam", dept="CSE")


#Multiply a set of numbers
def multi(*numbers):
    c = 1
    for i in numbers:
        c *= i
    print(f"The answer is {c}")
multi(2,2)
multi(4,7)
multi(9,440,334,13)
multi(9,4)
