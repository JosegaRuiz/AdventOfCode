# Función que transforma los inputs a listas de rango
def getRangeToList(pair):
    ini, fin = pair.split('-')
    ini = int(ini)
    fin = int(fin)
    range_result = list()
    for i in range(ini, fin+1):
        range_result.append(i)
    return range_result


# Función para comprobar si un rango está totalmente contenido en otro
def checkFullyContained(range1, range2):
    is_contained = True
    for i in range1:
        if i not in range2:
            is_contained = False
    return is_contained


# Función que comprueba si hay algún solape entre dos rangos
def checkOverlaped(range1, range2):
    overlaped = False
    for i in range1:
        if i in range2:
            overlaped = True
    return overlaped


# Solución a la parte 1, se cuentan los solapes completos entre todas las listas
def totalFullyContains():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    total_fully_containeds = 0
    for line in lines:
        line = line.strip()
        pair1, pair2 = line.split(',')[0], line.split(',')[1]
        range1 = getRangeToList(pair1)
        range2 = getRangeToList(pair2)
        if checkFullyContained(range1, range2):
            total_fully_containeds += 1
        elif checkFullyContained(range2, range1):
            total_fully_containeds += 1
    print(total_fully_containeds)


# Solución a la parte 2, se cuentan todos los solapes que aparecen, de cualquier tipo
def totalOverlaps():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    total_overlapeds = 0
    for line in lines:
        line = line.strip()
        pair1, pair2 = line.split(',')[0], line.split(',')[1]
        range1 = getRangeToList(pair1)
        range2 = getRangeToList(pair2)
        if checkOverlaped(range1, range2):
            total_overlapeds += 1
        elif checkOverlaped(range2, range1):
            total_overlapeds += 1
    print(total_overlapeds)


totalFullyContains()
totalOverlaps()