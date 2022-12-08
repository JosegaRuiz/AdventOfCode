# Funcion que comprueba si un arbol es visible desde alguno de los limites de la matriz
def compruebaVisibilidad(i, j, trees_matrix):
    # Se comienza como arbol visible desde todos los puntos
    visible_up = True
    visible_down = True
    visible_left = True
    visible_right = True
    # Se comprueba lado por lado si el arbol es visible
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
    # Si al menos es visible desde algún punto se va a contabilizar
    if visible_up or visible_down or visible_left or visible_right:
        return 1
    else:
        return 0


# Funcion que comprueba el número de árboles visibles desde un arbol de la matriz dado
def conteoVisibles(i, j, trees_matrix):
    # Se inicializan a 0 los arboles visibles desde cada lado
    visibles_up = 0
    visibles_down = 0
    visibles_left = 0
    visibles_right = 0
    # Se cuenta por cada lado cuantos arboles son visibles
    for n in range(i, 0, -1):
        if trees_matrix[n-1][j] >= trees_matrix[i][j]:
            visibles_left += 1
            break
        else:
            visibles_left += 1
    for n in range(i, 98):
        if trees_matrix[n+1][j] >= trees_matrix[i][j]:
            visibles_right += 1
            break
        else:
            visibles_right += 1
    for n in range(j, 0, -1):
        if trees_matrix[i][n-1] >= trees_matrix[i][j]:
            visibles_up += 1
            break
        else:
            visibles_up += 1
    for n in range(j, 98):
        if trees_matrix[i][n+1] >= trees_matrix[i][j]:
            visibles_down += 1
            break
        else:
            visibles_down += 1
    # Se devuelve la formula definida en el enunciado
    return visibles_up * visibles_down * visibles_left * visibles_right

def treelab():
    f = open('input.txt', 'r')
    lines = f.readlines()
    trees_matrix = list()
    count = 0
    count2 = 0

    # Se construye el input como una matriz (lista de listas)
    for line in lines:
        line = line.strip()
        trees_row = list()
        for tree in line:
            trees_row.append(int(tree))
        trees_matrix.append(trees_row)
    for i in range(len(trees_matrix)):
        for j in range(len(trees_matrix[i])):
            count += compruebaVisibilidad(i, j, trees_matrix)
            if conteoVisibles(i, j, trees_matrix) > count2:
                count2 = conteoVisibles(i, j, trees_matrix)
    print('Solución parte 1:', count)
    print('Solución parte 2:', count2)

treelab()