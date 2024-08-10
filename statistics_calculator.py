def calcular_promedio(datos):
    # Implementar lógica para calcular el promedio
    pass

def calcular_mediana(datos):
    # Implementar lógica para calcular la mediana
    if len(datos) % 2 == 0:
        mediana1 = datos[(len(datos) // 2) - 1]
        mediana2 = datos[(len(datos) // 2)]
        return (mediana1 + mediana2) / 2
    else:
        return datos[len(datos) // 2]

def calcular_moda(datos):
    # Implementar lógica para calcular la moda
    pass

# Agrega más funciones según sea necesario

if __name__ == "__main__":
    # Puedes agregar código de ejemplo aquí para probar las funciones
    
    # Leer datos con un input y verificar que sean enteros
    cadena_datos = input("Ingrese un conjunto de valores separados por coma: ")
    datos = cadena_datos.split(",")
    for i in range (0, len(datos)):
        datos[i] = datos[i].strip()
        assert datos[i].isnumeric(), f"ERROR: '{datos[i]}' no es un número"
        try:
            datos[i] = int(datos[i])
        except:
            print(f"ERROR: {datos[i]} no se puede convertir a entero")




    promedio = calcular_promedio(datos)
    print(f"El promedio de los datos es: {promedio}")

    mediana = calcular_mediana(datos)
    print(f"La mediana de los datos es: {mediana}")

    moda = calcular_moda(datos)
    print(f"La moda de los datos es: {moda}")


