import numpy as np

def solucion1():
    with open('In.txt') as input_file:
        content = input_file.read().replace('\n', '').split(', ')
        coordenadas = [0, 0, 0, 0]
        marcador = 0
        for move in content:
            if move[0] == 'R':
                if marcador == 3:
                    marcador = 0
                else:
                    marcador += 1
                coordenadas[marcador] += int(move[1])
            else:
                if marcador == 0:
                    marcador = 3
                else:
                    marcador -= 1
                coordenadas[marcador] += int(move[1])
        print(coordenadas)
        res = abs(coordenadas[0] - coordenadas[2]) + abs(coordenadas[1] - coordenadas[3])
        print('El resultado es:', res)

solucion1()