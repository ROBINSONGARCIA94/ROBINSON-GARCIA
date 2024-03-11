def calcular_temperatura_promedio(ciudades):
    """
    Calcula la temperatura promedio de cada ciudad.

    Args:
    - ciudades (dict): Un diccionario donde las claves son los nombres de las ciudades y los valores son listas de temperaturas.

    Returns:
    - dict: Un diccionario donde las claves son los nombres de las ciudades y los valores son las temperaturas promedio.
    """
    temperaturas_promedio = {}
    for ciudad, temperaturas in ciudades.items():
        temperatura_promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = temperatura_promedio
    return temperaturas_promedio

# Datos de ejemplo (3 ciudades durante 4 semanas)
datos_temperaturas = {
    "Ciudad A": [20, 22, 19, 18],
    "Ciudad B": [23, 24, 21, 20],
    "Ciudad C": [25, 27, 26, 24]
}

# Calcular temperaturas promedio
temperaturas_promedio = calcular_temperatura_promedio(datos_temperaturas)
print("Temperaturas promedio por ciudad:")
for ciudad, temperatura_promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {temperatura_promedio}")
