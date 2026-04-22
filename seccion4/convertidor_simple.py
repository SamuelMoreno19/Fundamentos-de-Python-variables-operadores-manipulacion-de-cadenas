kilometers = 12.25
miles = 7.38

# Conversión: Multiplicamos las millas por 1.61
miles_to_kilometers = miles * 1.61

# Conversión: Dividimos los kilómetros por 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")



# --- CONVERTIDOR DE TEMPERATURA ---
celsius = 30
# Fórmula: (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

print(celsius, "grados Celsius son", fahrenheit, "grados Fahrenheit.")



# --- CONVERTIDOR DE ALMACENAMIENTO (TECH) ---
gigabytes = 2.5
# 1 GB son 1024 MB (base binaria)
megabytes = gigabytes * 1024

print(gigabytes, "GB equivalen a", megabytes, "MB.")

# --- CONVERTIDOR DE MONEDA (ACTUALIZADO) ---
usd = 15.75
tasa_cop = 3950.50 # Valor hipotético del dólar
total_cop = usd * tasa_cop

print(usd, "USD son", round(total_cop, 0), "pesos colombianos (COP).")

