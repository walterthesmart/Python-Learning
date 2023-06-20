class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "play tennis")
        elif self.occupation == "actor":
            print(self.name, "shoot films")

    def speaks(self):
        print(self.name, "says how are you?")

tom = Human("Roger Federera", "tennis player")
tom.do_work()
tom.speaks()