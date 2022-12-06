# Función que resuelve el problema
def subroutine_def(part):
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    # Solo vamos a tener una línea realmente como entrada
    for line in lines:
        # Se crea una estructura set donde se irán almacenando las ocurrencias
        different_els = set()
        # Iteramos por elemento de la línea
        for i in range(len(line)):
            # Se cogen los J elementos seguidos, lo único que cambia entre parte 1 y parte 2 es ésto, 4 o 14
            for j in range(part):
                # Se van añadiendo al set cada elemento contiguo
                different_els.add(line[i+j])
            # Al acabar de añadir comprobamos que no hayan repetidos
            if len(different_els) == part:
                print(i+part)
                break
            # Reiniciamos la estructura si no se han encontrado
            different_four = set()

subroutine_def(4)
subroutine_def(14)