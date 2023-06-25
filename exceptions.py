# try:
#     raise MemoryError('memory error')
# except MemoryError as e:
#     print(e)

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def handle(self):
        print("User defined exception: ", self.msg)
try:
    raise Accident("Crash between two cars")
except Accident as e:
    e.handle()