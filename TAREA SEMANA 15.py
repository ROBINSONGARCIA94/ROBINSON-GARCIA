# Crear el diccionario inicial con información personal ficticia
informacion_personal = {
    "nombre": "Juan Perez",
    "edad": 30,
    "ciudad": "Ciudad A",
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Ciudad B"

# Agregar la profesión al diccionario
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)
