""" 
Caesar CODEC

Este programa toma un archivo y cifra su contenido utilizando el cifrado de desplazamiento.
después guarda el contenido en un nuevo archivo y lo podemos decodificar si deseamos
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
    my_file.close()
    return result

def decrypt(my_file, key):
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
            ciphered_char = chr((ord(char) - key - 97) % 26 + 97)
            result += ciphered_char
    my_file.close()
    return result    

def get_name_from_user():
    # Pedimos el nombre del archivo al usuario y agregamos la extensión .txt
    file_name = input("Enter the name of the file you want to cipher: ") + ".txt"
    return file_name

def write_to_file(file_name, content):
    # El modo 'w' creará el archivo, si el especificado no existe
    my_file = open(file_name, 'w')
    my_file.write(content)
    my_file.close()

def read_from_file(file_name):
    # Comprobamos que el archivo existe antes de abrirlo
    if (os.path.exists(file_name)):
        my_file = open(file_name, 'r')
        return my_file
    
if __name__ == '__main__':
    key = 1                                                 # Llave de cifrado
    original_file_name = get_name_from_user()               # Nombre del archivo obtenido del usuario
    original_file = read_from_file(original_file_name)      # instancia de archivo de el mensaje original
    encode_message = encrypt(original_file, key)            # Obtenemos el mensaje codificado
    write_to_file("code.txt", encode_message)               # Escribimos el mensaje codificado en un nuevo archivo
    coded_file = read_from_file("code.txt")                 # Abrimos el archivo codificado
    decode_message = decrypt(coded_file, key)               # Decodificamos el mensaje
    write_to_file("decode.txt", decode_message)             # Escribimos el mensaje decodificado en un nuevo archivo    