# Forma manual de inicializar un diccionario de prioridades (DEFINIDO POR EL ENUNCIADO)
def setIniDict():
    ini_dict = dict()
    vowels = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    for i, vowel in zip(range(53), vowels):
        ini_dict[vowel] = i+1
    return ini_dict


# Se obtiene la suma de una bolsa dados sus compartimentos
def getRucksackSum(compartment_1, compartment_2, prio_dict):
    both_compartments = set()
    for key in prio_dict:
        if key in compartment_1 and key in compartment_2:
            both_compartments.add(key)
    rucksack_sum = 0
    for item in both_compartments:
        rucksack_sum += prio_dict[item]
    return rucksack_sum


# Se obtiene el item que se encuentra en las mochilas de un grupo de 3 elfos
def getItemFromGroup(rucksack_1, rucksack_2, rucksack_3, prio_dict):
    for key in prio_dict:
        if key in rucksack_1 and key in rucksack_2 and key in rucksack_3:
            return key


# Solución para la parte 1
def getTotalSumPart1():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    total_score = 0
    # Se obtiene el diccionario de prioridades para los items
    prio_dict = setIniDict()
    for line in lines:
        line = line.strip()
        # Cada linea es una mochila, la mochila se divide en dos partes iguales (compartimentos)
        total_score += getRucksackSum(line[:int(len(line)/2)], line[int(len(line)/2):], prio_dict)
    # Se muestra por pantalla el resultado
    print('Resultado para parte 1:', total_score)


# Solucion para la parte 2
def getTotalSumPart2():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    total_score = 0
    prio_dict = setIniDict()
    group = list()
    while lines:
        # Se van a formar grupos de 3 en 3 mochilas
        for i in range(3):
            group.append(lines.pop(0).strip())
        # Se obtiene el elemento que se comparte cada 3 mochilas
        item = getItemFromGroup(group[0], group[1], group[2], prio_dict)
        total_score += prio_dict[item]
        # se reinicia el grupo
        group = list()
    print('Resultado para parte 2:', total_score)


getTotalSumPart1()
getTotalSumPart2()