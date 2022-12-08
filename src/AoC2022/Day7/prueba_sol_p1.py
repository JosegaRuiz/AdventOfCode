# Funcion para obtener el tamaño que tienen los archivos de un directorio, sin contar con subdirectorios
def dir_size(dir_list):
    sum = 0
    for el in dir_list:
        sum += int(el[0])
    return sum

# Funcion para comprobar el tamaño del directorio y subdirectorios total
def checkDirSize(dir, dirs_dict):
    sum = 0
    for key in dirs_dict:
        if key.startswith(dir):
            sum += dir_size(dirs_dict[key])
    if sum <= 100000:
        return sum
    else:
        return 0



def subroutine_def():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    dir = ''
    dirs_dict = dict()
    sum = 0
    # Solo se va a tener una línea realmente como entrada
    for line in lines:
        line = line.strip()
        line = line.split(' ')
        # Caso para comandos
        if line[0] == '$':
            # Cuando el comando sea un cd se moverá el directorio
            if line[1] == 'cd':
                # Si se introduce '/' va al home
                if line[2] == '/':
                    dir = '/'
                # Si se introduce '..' va al directorio previo
                elif line[2] == '..':
                    dir = '/'.join(dir.split('/')[0:-2])
                    if dir == '':
                        dir = '/'
                # Si se introduce un directorio cualquiera simplemente cambiará el directorio a más profundidad
                else:
                    dir += line[2] + '/'
            # Con el comando ls no se va a hacer nada directamente, ya que lo importante serán las siguientes líneas
            if line[1] == 'ls':
                pass
        # cuando se encuentre un directorio se inicializará a vacío, posteriormente se va a rellenar
        elif line[0] == 'dir':
            dirs_dict[dir + line[1] + '/'] = list()
        else:
            # Si el directorio aun no se ha inicializado se hará como vacío
            if dir not in dirs_dict.keys():
                dirs_dict[dir] = list()
            # Cada elemento de la lista será un par (size, filename)
            dirs_dict[dir].append((line[0], line[1]))
    for key in dirs_dict.keys():
        sum += checkDirSize(key, dirs_dict)
    print(sum)

subroutine_def()