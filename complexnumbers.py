## OOP 
# Declaramos la clase
class ComplexNumber:
    # Atributos de la clase, nótese que los atributos no reciben el valor por default de esta
    # manera, comentarle a Luque
    real = 0     
    imag = 0
    # Aqui declaramos el constructor, dentro de la clase. Objetos en Python no requieren destructor.
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    #Este método imprime el número complejo
    def print_notation(self):
        if(self.imag < 0):
            print(str(self.real) + " " + str(self.imag) + "i")
        else:
            print(str(self.real) + "+" + str(self.imag) + "i")

    #Sobrecarga del operador binario +
    def __add__(self, complex_num):
      #Instancia de la misma clase que servirá como auxiliar.
      result = ComplexNumber(0,0)
      # Efectuamos las operaciones
      result.real = self.real + complex_num.real
      result.imag = self.imag + complex_num.imag
      # Regresamos la suma de dos números imaginarios
      return result

    # Misma sobrecarga de operador pero ahora para restar
    def __sub__(self, complex_num):
      result = ComplexNumber(0,0)
      result.real = self.real - complex_num.real
      result.imag = self.imag - complex_num.imag
      return result



# Instancias de la clase ComplexNumber
num_1 = ComplexNumber(3, 9)
num_2 = ComplexNumber(3, -9)
num_3 = num_1 + num_2
num_4 = num_3 - num_1


# Llamamos los métodos para cada instancia.
num_1.print_notation()
num_2.print_notation()
num_3.print_notation()
num_4.print_notation()
