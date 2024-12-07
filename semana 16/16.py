# Abrimos el archivo 'my_notes.txt' en modo escritura ('w') para sobrescribir su contenido
with open('my_notes.txt', 'w') as archivo:  
    archivo.write('1 España\n2 México\n3 Argentina\n4 Chile\n5 Colombia')  # Escribimos los nombres de los países en el archivo

# Abrimos el archivo 'my_notes.txt' en modo lectura ('r') para leer su contenido
with open('my_notes.txt', 'r') as archivo:  
    lineas = archivo.readlines()  # Guardamos cada línea del archivo en una lista llamada 'lineas'

    # Iteramos sobre cada línea de la lista y la imprimimos sin el salto de línea '\n'
    for l in lineas:  
        print(l.replace('\n', ' '))  # Reemplazamos el salto de línea por un espacio para mostrar todo en una línea
