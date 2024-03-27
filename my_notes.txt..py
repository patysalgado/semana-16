# Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    # Escribir notas personales en el archivo
    file.write("Estoy aprendiendo Python.\n")  # Escribir la primera línea
    file.write("Necesito practicar más con archivos de texto.\n")  # Escribir la segunda línea
    file.write("Quiero mejorar mis habilidades de programación.\n")  # Escribir la tercera línea

# Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    # Leer el contenido línea por línea
    for line in file.readlines():
        # Mostrar cada línea en la consola
        print(line.strip())  # strip() para eliminar los caracteres de nueva línea

# Cierre de Archivos
# No es necesario cerrar explícitamente los archivos al utilizar 'with open'