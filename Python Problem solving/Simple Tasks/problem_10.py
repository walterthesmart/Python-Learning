#write a python prompt to get 6 subject marks from the user and calculate total and average of that mark, then display to user
marks = input('Enter the marks separated by a comma: ')
marks = marks.split(',')
scores = []
for mark in marks:
    scores.append(int(mark))
total = 0
for i in scores:
    total += i
average = total/len(marks)
print(total)
print(average)
