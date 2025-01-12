
class operaciones_matematicas:
    def __init__(self, resultado=0, acumilativo = 0, promedio = 0):
        self.resultado = resultado
        self.acumilativo = acumilativo
        self.promedio = promedio

    def suma(self, n1, n2):
        self.resultado = n1 + n2
        self.acumilativo += self.resultado
    
    def resta(self, n1, n2):
        self.resultado = n1 - n2
        self.acumilativo += self.resultado
    
    def multiplicacion(self, n1, n2):
        self.resultado = n1*n2
        self.acumilativo += self.resultado
  
    def division(self, n1, n2):
        self.resultado = n1/n2
        self.acumilativo += self.resultado
        #promedio
        #suma todos los valores / divido para el numero de valores
    def funcionpromedio(self):
        self.promedio = self.acumilativo / 5

opracion = operaciones_matematicas()
opracion.suma(10,15)
opracion.multiplicacion(10,15)
opracion.division(15,5)
opracion.resta(15,5)
opracion.funcionpromedio()
print (f'{opracion.acumilativo}')
print (f'{opracion.promedio}')