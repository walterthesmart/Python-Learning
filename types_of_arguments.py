# positional arguments
# def greet(name, dept):
#    print(f"Hi {name}")
#    print(f"Are you from {dept} department?")
# greet("Walter", "FInance")
#
# Keyword arguments
# def greet(name, dept):
#    print(f"Hi {name}")
#    print(f"Are you from {dept} department?")
# greet(name = "Walter", dept = "FInance")
#
# Default arguments
# def greets(name, subject, dept = "CS"):
#     print(f"Hi {name}")
#     print(f"Are you from {dept} department?")
#     print(f"Do you teach {subject}")
# greets("Walter", "Finance")

def add(*numbers):
    c = 0
    for i in numbers:
        c += i
    print(f"Sum is {c}")
add(5,7,4)
add(7,5,34,2,4,32132,9)
