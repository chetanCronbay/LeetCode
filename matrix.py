matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
temp = 0

for row in range(len(matrix)):
    # print(matrix[row])
    # print("-----------")
    for col in range(len(matrix[0])):
        # print(matrix[row][col])
        if col > row :
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp
            # change = True
        # print(matrix)
        # print("-------------------")
        # break

for row in range(len(matrix)):
    # print(row)
    for col in range(len(matrix[0])):
        if col < (round(len(matrix) / 2)):
            # print(col)
            temp = matrix[row][col]
            matrix[row][col] = matrix[row][-(col + 1)]
            matrix[row][-(col + 1)] = temp
            # print(matrix)
            # print("------------------")
        
# print(matrix)
# print(round(len(matrix) / 2)-1)