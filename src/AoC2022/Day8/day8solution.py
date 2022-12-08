def compruebaVisibilidad(i, j, trees_matrix):
    if i== 0:
        return 1
    elif i == 99:
        return 1
    elif j == 0:
        return 1
    elif j == 99:
        return 1
    visible_up = True
    visible_down = True
    visible_left = True
    visible_right = True
    for n in range(0, i):
        if trees_matrix[n][j] >= trees_matrix[i][j]:
            visible_left = False
    for n in range(i+1, len(trees_matrix[i])):
        if trees_matrix[n][j] >= trees_matrix[i][j]:
            visible_right = False
    for n in range(0, j):
        if trees_matrix[i][n] >= trees_matrix[i][j]:
            visible_up = False
    for n in range(j+1, len(trees_matrix)):
        if trees_matrix[i][n] >= trees_matrix[i][j]:
            visible_down = False
    if visible_up or visible_down or visible_left or visible_right:
        return 1
    else:
        return 0


def treelab():
    f = open('input.txt', 'r')
    lines = f.readlines()
    trees_matrix = list()
    count = 0

    for line in lines:
        line = line.strip()
        trees_row = list()
        for tree in line:
            trees_row.append(int(tree))
        trees_matrix.append(trees_row)
    for i in range(len(trees_matrix)):
        for j in range(len(trees_matrix[i])):
            count += compruebaVisibilidad(i, j, trees_matrix)
    print(count)
treelab()