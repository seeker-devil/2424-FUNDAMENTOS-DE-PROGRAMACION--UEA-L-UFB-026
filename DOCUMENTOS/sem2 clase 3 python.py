class operaciones_matematicas:
    def __init__(self, resultados=0, acumulativo=0):
        self.resultado=resultados
        self.acumulativo=acumulativo

    def suma(self, n1,n2):
        self.resultado=n1+n2
        self.acumulativo +=self.resultado

    def resta(self, n1, n2):
        self.resultado=n1-n2
        self.acumulativo +=self.resultado

    def multiplicacion(self,n1,n2):
        self.resultado=n1*n2
        self.acumulativo +=self.resultado

    def division(self,n1,n2):
        self.resultado=n1/n2
        self.acumulativo +=self.resultado

operacion=operaciones_matematicas()
operacion.suma(20,5)
print(f'el resultado de la suma es: {operacion.resultado}')
        

operacion.resta(20,5)
print(f'el resultado de la resta es: {operacion.resultado}')


operacion.multiplicacion(20,5)
print(f'el resultado de la multiplicacion es: {operacion.resultado}')

operacion.division(20,5)
print(f'el resultado de la division es: {operacion.resultado}')

print(f'el resultado del acumulado es: {operacion.acumulativo}')