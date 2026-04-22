# --- Nuevas pruebas para la expresión: 3x^3 - 2x^2 + 3x - 1 ---

# Caso A: x = 2 (Número entero positivo)
x = 2.0
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
# Explicación: 3(8) - 2(4) + 3(2) - 1 = 24 - 8 + 6 - 1 = 21
print("Caso A -> Si x =", x, "entonces y =", y)

# Caso B: x = 0.5 (Número decimal/flotante)
x = 0.5
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
# Explicación: 3(0.125) - 2(0.25) + 3(0.5) - 1 = 0.375 - 0.5 + 1.5 - 1 = 0.375
print("Caso B -> Si x =", x, "entonces y =", y)

# Caso C: x = -2 (Número negativo)
x = -2.0
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
# Explicación: 3(-8) - 2(4) + 3(-2) - 1 = -24 - 8 - 6 - 1 = -39
print("Caso C -> Si x =", x, "entonces y =", y)