# 1. Creación de variables y asignación de valores
john = 10
mary = 5
adam = 6

# 2. Imprimir las variables en una sola línea separadas por comas
print(john, mary, adam, sep=", ")

# 3. Crear la variable total_apples con la suma de las anteriores
total_apples = john + mary + adam

# 4. Imprimir el resultado total
print("Número total de manzanas:", total_apples)

# 5. Experimentación: Operaciones adicionales
print("\n--- Sección de Experimentación ---")
# ¿Cuántas manzanas quedarían si Adán se come 2?
manzanas_restantes = total_apples - 2
print("Si Adán se come 2, quedan:", manzanas_restantes)

# Repartir las manzanas entre los 3 (División flotante)
promedio = total_apples / 3
print("Promedio de manzanas por persona:", promedio)

# División entera (manzanas completas por persona)
por_persona = total_apples // 3
print("Manzanas completas para cada uno:", por_persona)