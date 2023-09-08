class Instructor:
    followers = 0   #Class Object Variable
    def __init__(self, name, address):
        self.name = name
        self.address = address
        #self.followers = 0

        #THis will take subject name as string
    def display(self, subject_name):
        print(f'Hiii, I am {self.name} and i teach {subject_name}')

    def update_followers(self, follower_name):
        self.followers += 1

instructor_1 = Instructor("Taiwo", "Marina")
print(instructor_1.name)
instructor_1.display('Python')
instructor_1.update_followers('Segun')
print(instructor_1.followers)