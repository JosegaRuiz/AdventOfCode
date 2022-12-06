# función que lee una acción, devuelve la lista [unidades que se mueven, desde donde se mueven, hacia donde]
def readAction(line):
    units = line.split(' ')[1]
    source = line.split(' ')[3]
    dest = line.split(' ')[5]
    return [units, source, dest]


# función que lee todas las acciones del fichero de entrada
def readActions(lines):
    actions = list()
    for line in lines:
        line = line.strip()
        actions.append(readAction(line))
    return actions


# Funcion que aplicará una acción a una lista de stacks y devuelve el resultado
def applyActionToStacks(action, stacks):
    for i in range(int(action[0])):
        el = stacks[int(action[1])-1].pop(-1)
        stacks[int(action[2])-1].append(el)
    return stacks


# Funcion que aplicará una accion a una lista de stacks y devuelve el resultado (para parte 2)
def applyActionToStacks2(action, stacks):
    to_move = list()
    for i in range(int(action[0])):
        el = stacks[int(action[1])-1].pop(-1)
        to_move.append(el)
    for i in range(len(to_move)):
        stacks[int(action[2])-1].append(to_move.pop(-1))
    return stacks


def craneMovementsExample():
    f = open('input_example.txt', 'r')
    lines = f.readlines()
    f.close()
    stack_lines = list()
    # definición manual de los stacks iniciales, se ha dividido el input para ir más rápido
    # se podria haber utilizado ERs para automatizar si la entrada fuera inmanejable
    stack_lines.append(['Z', 'N'])
    stack_lines.append(['M', 'C', 'D'])
    stack_lines.append(['P'])
    actions = readActions(lines)
    for action in actions:
        stack_lines = applyActionToStacks(action, stack_lines)
    for stack in stack_lines:
        print(stack[-1])
    print(stack_lines)


def craneMovements():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    stack_lines = list()
    # definición manual de los stacks iniciales, se ha dividido el input para ir más rápido
    # se podria haber utilizado ERs para automatizar si la entrada fuera inmanejable
    stack_lines.append(['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'])
    stack_lines.append(['T', 'B', 'M', 'Z', 'R'])
    stack_lines.append(['Z', 'L', 'C', 'H', 'N', 'S'])
    stack_lines.append(['S', 'C', 'F', 'J'])
    stack_lines.append(['P', 'G', 'H', 'W', 'R', 'Z', 'B'])
    stack_lines.append(['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'])
    stack_lines.append(['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'])
    stack_lines.append(['M', 'Z', 'R'])
    stack_lines.append(['M', 'C', 'L', 'G', 'V', 'R', 'T'])
    actions = readActions(lines)
    for action in actions:
        stack_lines = applyActionToStacks(action, stack_lines)
    for stack in stack_lines:
        print(stack[-1])
    print(stack_lines)


def craneMovements_2():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    stack_lines = list()
    # definición manual de los stacks iniciales, se ha dividido el input para ir más rápido
    # se podria haber utilizado ERs para automatizar si la entrada fuera inmanejable
    stack_lines.append(['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'])
    stack_lines.append(['T', 'B', 'M', 'Z', 'R'])
    stack_lines.append(['Z', 'L', 'C', 'H', 'N', 'S'])
    stack_lines.append(['S', 'C', 'F', 'J'])
    stack_lines.append(['P', 'G', 'H', 'W', 'R', 'Z', 'B'])
    stack_lines.append(['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'])
    stack_lines.append(['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'])
    stack_lines.append(['M', 'Z', 'R'])
    stack_lines.append(['M', 'C', 'L', 'G', 'V', 'R', 'T'])
    actions = readActions(lines)
    for action in actions:
        stack_lines = applyActionToStacks2(action, stack_lines)
    for stack in stack_lines:
        print(stack[-1])
    print(stack_lines)

craneMovements_2()