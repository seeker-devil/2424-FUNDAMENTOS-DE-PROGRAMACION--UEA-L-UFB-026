# Ejemplo de Apertura de Archivos en Python

# Definimos el nombre del archivo
file_name = "provincias_ecuador.txt"

# Modo de apertura: "r" para lectura (read)
# Abrimos el archivo que acabamos de crear
archivo = open(file_name, "w")

archivo.write('Pastaza')

# Cerramos el archivo después de leer
archivo.close()