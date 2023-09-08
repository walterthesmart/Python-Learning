class Instructor:
    def __init__(self, instructor_name, address):
        self.name = instructor_name
        self.address = address

instructor_1 = Instructor("Walter", "Birhmingham")

print(instructor_1.name)