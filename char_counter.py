# Lectura de caracter a caracter
# Pedimos nombre del archivo que leeremos
nombre = input("Dame el nombre del txt a procesar:")+".txt"
# Abrimos el archivo que le solicitamos al usuario
archivo = open(nombre,"r")
contador = 0 #Establecemos un contador
caracter = archivo.read(1)
while(caracter != ""):
    contador +=1
    caracter = archivo.read(1)
archivo.close()
#Imprimimos el numero de caracteres de nuestro archivo
print(contador)