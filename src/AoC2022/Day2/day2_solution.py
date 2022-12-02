
# Funcion para obtener el valor devuelto al tomar una acción recomendada
# A, X ROCK
# B, Y PAPER
# C, Z SCISSORS
def getScoreOfAction(elf, you):
    score = 0
    if you == 'X':
        if elf == 'A':
            return 1+3
        elif elf == 'B':
            return 1+0
        elif elf == 'C':
            return 1+6
    elif you == 'Y':
        if elf == 'A':
            return 2+6
        elif elf == 'B':
            return 2+3
        elif elf == 'C':
            return 2+0
    elif you == 'Z':
        if elf == 'A':
            return 3+0
        elif elf == 'B':
            return 3+6
        elif elf == 'C':
            return 3+3

def getTotalScoreOfPlan():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    totalScore = 0
    for line in lines:
        line = line.strip()
        elf = line.split(' ')[0]
        you = line.split(' ')[1]
        totalScore += getScoreOfAction(elf, you)
    return totalScore


# Dada una accion y un resultado tenemos que devolver la accion a tomar
# A ROCK
# B PAPER
# C SCISSORS
# X Lose
# Y Draw
# Z Win
def getActionToTake(elf, result):
    if elf == 'A':
        if result == 'X':
            return 'Z'
        elif result == 'Y':
            return 'X'
        elif result == 'Z':
            return 'Y'
    elif elf == 'B':
        if result == 'X':
            return 'X'
        elif result == 'Y':
            return 'Y'
        elif result == 'Z':
            return 'Z'
    elif elf == 'C':
        if result == 'X':
            return 'Y'
        elif result == 'Y':
            return 'Z'
        elif result == 'Z':
            return 'X'


def getTotalScoreOfPlan2():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    totalScore = 0
    for line in lines:
        line = line.strip()
        elf = line.split(' ')[0]
        you = line.split(' ')[1]
        action = getActionToTake(elf, you)
        totalScore += getScoreOfAction(elf, action)
    return totalScore


print(getTotalScoreOfPlan())
print(getTotalScoreOfPlan2())