""" 
Caesar Cipher

Este programa toma un archivo y cifra su contenido utilizando el cifrado de desplazamiento.
después muestra en pantalla el texto cifrado.
Nuestro cifrado únicamente considera caracteres en minúsculas, como fue especificado en la
actividad.

"""
import os

# Función que encripta nuestro mensaje, recibe un archivo y la llave o secuancia para el cifrado.
def encrypt(my_file, key):
    # Variable de tipo string para almacenar nuestro resultado
    result = ""
    # Traversamos el archivo de texto caracter por caracter
    while ((char := my_file.read(1)) != ""):
        # Exceptuamos del cifrado mayúsculas y espacios.
        if (char == " " or char.isupper() or not char.isalpha()):
            result += char
        else:
            # Aplicamos simple aritmética modular transformando las letras en números, de acuerdo
            # al esquema, A = 0... Z = 25. Descrito matemáticamente como En(x) = (x + n) mod 26
            # Tomamos en cuenta el número en el que comienza la primer letra minúscula.
            ciphered_char = chr((ord(char) + key - 97) % 26 + 97)
            result += ciphered_char

    return result

# Pedimos el nombre del archivo al usuario y agregamos la extensión .txt
file_name = input("Enter the name of the file you want to cipher: ") + ".txt"
# Comprobamos que el archivo existe antes de abrirlo
if (os.path.exists(file_name)):
    my_file = open(file_name, 'r')
else:
    print("File does not exist!")

# Key es la llave o secuencia de desplazamineto que sigue nuestro cifrado
key = 1
print(encrypt(my_file, key))
# Cerramos el archivo
my_file.close()
