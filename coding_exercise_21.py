from math import ceil
def paint_coverage(height, width, cover):
    area = height*width
    no_of_cans = ceil(area/cover)
    print(f"You'll need {no_of_cans} cans of paint.")
h = int(input("Enter the height of wall in meters:\n"))
w = int(input("Enter the width of wall in meters:\n"))
coverage = 7
paint_coverage(width=w, height=h, cover=coverage)
