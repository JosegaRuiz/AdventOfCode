# solucion 1:
f = open('input.txt')
lines = f.readlines()
# Se utilizan dos contadores, el que almacenará el valor máximo histórico y el que almacenará el valor que se está
# almacenando por cada elfo y se irá reseteando en cada vuelta
max_count = 0
actual_count = 0
for line in lines:
    line = line.strip()
    # Cuando se encuentra la línea vacía 'patrón' se compara con el máximo que hay almacenado y si es mayor se
    # actualiza el valor y por último se resetea el contador SIEMPRE
    if line == '':
        if actual_count > max_count:
            max_count = actual_count
        actual_count = 0
    else:
        actual_count += int(line)
# Ya tenemos el valor máximo en el contador de máximo histórico
print('SOLUCION PARTE 1: ')
print(max_count)
print('\n\n\n')

# solucion 2:
f = open('input.txt')
lines = f.readlines()
# se crea un contador que almacenará el valor de cada elfo mientras se recorre la entrada
# y una lista que almacenará los valores de cada elfo
cal_vector = list()
actual_count = 0
for line in lines:
    line = line.strip()
    if line == '':
        cal_vector.append(actual_count)
        actual_count = 0
    else:
        actual_count += int(line)
# Se ordena la lista de valores calorias totales de los elfos de mayor a menor y se cogen los 3 primeros valores
# (Top 3) requerido por el enunciado, se suman y esta es la solución
cal_vector.sort(reverse=True)
sol = 0
for i in range(3):
    sol += cal_vector[i]
print('\nSOLUCION PARTE 2: ')
print(cal_vector)
print(sol)
