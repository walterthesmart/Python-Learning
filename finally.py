def process_file():
    try:
        f = open("/home/walter/Python-Learning/data.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside except")

    finally:
        print("cleaning of file")
        f.close()

process_file()