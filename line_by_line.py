# filepath toma el valor en string del nombre de nuestro archivo
# Si el archivo se encuentra en un directorio diferente al de nuestro programa, debemos
# incluir el directorio también.
filepath = 'ejemplo2.txt'
# Utilizamos la sentencia with que nos facilita el manejo de excepciones y aparte
# cierra el archivo automáticamente una vez hemos terminado de usarlo
# nuestro objeto archivo recibe el nombre de fp
with open(filepath) as fp:
    # line recibe un string de fp.readline() que lee una línea del archivo
    line = fp.readline()
    # cnt para llevar track de las líneas en la impresión
    cnt = 1
    # Minetras no se acabe de leer el archivo
    while line:
         # Imprime el archivo leyendo línea por línan usando la función
         # .format() que nos ayuda a insertar la variable cnt en el string así como la línea que
         # sigue en el archivo
        print("Line {}: {}".format(cnt, line.strip()))
        # Lee una nueva línea del archivo
        line = fp.readline()
        # aumenta el contado + 1
        cnt += 1
