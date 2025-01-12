class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f'Ingrese la temperatura del día {i + 1} en grados Centigrados: '))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Crear una instancia de la clase ClimaSemanal
clima = ClimaSemanal()

# Ingresar las temperaturas
clima.ingresar_temperaturas()

# Calcular y mostrar el promedio semanal
promedio = clima.calcular_promedio()
print(f'La temperatura semanal de Quito es: {promedio:.2f}°C')
