row1 = [1,1,1]
row2 = [2,2,2]
row3 = [3,3,3]
matrix = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Enter the position where you want to hidde your money:")

row_num = int(position[0])
col_num = int(position[1])
row_selected = matrix[row_num-1]
row_selected[col_num-1] = "X"
print(f"{row1}\n{row2}\n{row3}")