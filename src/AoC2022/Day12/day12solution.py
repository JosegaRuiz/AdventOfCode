# Funcion utilizada para comprobar el caracter posterior a uno dado
def get_next_letter(letter):
    num = ord(letter)
    num += 1
    return chr(num)


# Funcion utilizada para obtener el caracter anterior a uno dado
def get_previous_letter(letter):
    num = ord(letter)
    num -= 1
    return chr(num)


# Funcion para comprobar si se puede mover desde un caracter a otro
def comprueba_movimiento(caracter_s, caracter_d):
    if caracter_s == caracter_d:
        return True
    elif caracter_s == 'S' and caracter_d == 'a':
        return True
    if caracter_s == 'z':
        if caracter_d == 'S':
            return True
        else:
            return False
    else:
        if caracter_d == get_previous_letter(caracter_s) or caracter_d == get_next_letter(caracter_s):
            return True
    return False


# función recursiva para comprobar el mínimo número de pasos para llegar al destino
def minimo_pasos(actual_position, destination, grid, visiteds, steps):
    # Se comprueba si se ha llegado al destino
    left, right, up, down = False, False, False, False
    i, j = actual_position
    i_d, j_d = destination
    if i == i_d and j == j_d:
        return steps
    # Se comprueban las posibles acciones a realizar dentro del grid
    # Para cada movimiento primero comprobamos que esté dentro de los límites del grid
    if i>0:
        # Se comprueba si se puede mover a la izquierda:
        if comprueba_movimiento(grid[i][j], grid[i-1][j]) and not visiteds[i-1][j]:
            left = True
    if i<len(grid)-1:
        # Se comprueba si se puede mover a la derecha:
        if comprueba_movimiento(grid[i][j], grid[i+1][j]) and not visiteds[i+1][j]:
            right = True
    if j>0:
        # Se comprueba si se puede mover hacia arriba:
        if comprueba_movimiento(grid[i][j], grid[i][j-1]) and not visiteds[i][j-1]:
            up = True
    if j<len(grid[0])-1:
        # Se comprueba si se puede mover hacia abajo:
        if comprueba_movimiento(grid[i][j], grid[i][j+1]) and not visiteds[i][j+1]:
            down = True

    # Si no hay camino se devuelve un infinito ya que no queremos continuar con esa rama
    if not left and not down and not right and not up:
        return float('inf')
    # Ahora se hace la llamada recursiva con los posibles movimientos
    if left:
        visiteds[i-1][j] = True
        steps_left = minimo_pasos((i-1, j), destination, grid, visiteds, steps+1)
        visiteds[i-1][j] = False
    if right:
        visiteds[i+1][j] = True
        steps_right = minimo_pasos((i+1, j), destination, grid, visiteds, steps+1)
        visiteds[i+1][j] = False
    if up:
        visiteds[i][j-1] = True
        steps_up = minimo_pasos((i, j-1), destination, grid, visiteds, steps+1)
        visiteds[i][j-1] = False
    if down:
        visiteds[i][j+1] = True
        steps_down = minimo_pasos((i, j+1), destination, grid, visiteds, steps+1)
        visiteds[i][j+1] = False
    # Se devuelve el mínimo de los pasos obtenidos
    return min(steps_left, steps_right, steps_up, steps_down)


def part1():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    grid = list()
    visiteds = list()
    for line in lines:
        line = line.strip()
        grid.append(line)
        visiteds.append([False] * len(line))
    for line in len(grid):
        for letter in len(grid[line]):
            if grid[line][letter] == 'E':
                start = (line, letter)
                visiteds[line][letter] = True
            elif grid[line][letter] == 'S':
                destination = (line, letter)
    # Se realiza la llamada inicial a la funcion recursiva
    print(minimo_pasos(start, destination, grid, visiteds, 0))


part1()