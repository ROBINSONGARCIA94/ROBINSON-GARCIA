def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicando el porcentaje de descuento al monto total de la compra.

    Args:
    monto_total (float): Monto total de la compra.
    porcentaje_descuento (float, opcional): Porcentaje de descuento a aplicar. Por defecto es 10%.

    Returns:
    float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función calcular_descuento
monto_compra_1 = 100
monto_compra_2 = 200
porcentaje_descuento_2 = 15

descuento_1 = calcular_descuento(monto_compra_1)
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)

# Resultados
print("Resultados de las llamadas a la función calcular_descuento:")
print("----------------------------------------------------------")
print(f"Para una compra de ${monto_compra_1} con un 10% de descuento, el descuento es: ${descuento_1}")
print(f"Por lo tanto, el monto final a pagar es: ${monto_compra_1 - descuento_1}")

print()

print(f"Para una compra de ${monto_compra_2} con un {porcentaje_descuento_2}% de descuento, el descuento es: ${descuento_2}")
print(f"Por lo tanto, el monto final a pagar es: ${monto_compra_2 - descuento_2}")
