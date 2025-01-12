# Crear una lista vacía para almacenar las temperaturas
temperaturas = []

# Ingresar las temperaturas para los 7 días de la semana
for i in range(7):
    temp = float(input(f'Ingrese la temperatura del día {i + 1} en Celsius: '))
    temperaturas.append(temp)

# Calcular el promedio de las temperaturas
promedio = sum(temperaturas) / len(temperaturas)

# Mostrar el resultado
print(f'La temperatura semanal de Quito es: {promedio:.2f}°C')