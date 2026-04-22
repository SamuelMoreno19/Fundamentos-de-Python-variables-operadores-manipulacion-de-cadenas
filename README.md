# Fundamentos de Python

# Seccion 1 y sus laboratorios

# LAB  Trabajando con la función print()
El archivo hola.py contiene la instrucción básica para imprimir en consola:
print("Hola, Mundo!")

print(): Es una función integrada de Python que envía información a la salida estándar (la terminal) - 
"Hola, Mundo!": Es una cadena de texto (string). Debe ir entre comillas para que Python la reconozca como texto y no como una variable - Propósito: Validar que el intérprete de Python 3.12 está correctamente configurado y ejecutando código.

# LAB  La función print() y sus argumentos
sep="***": Por defecto, print pone un espacio entre cada palabra. Al usar sep (separador), le ordenamos que meta tres asteriscos entre "Programming", "Essentials" e "in".

end="...": Por defecto, print salta a la siguiente línea al terminar (un \n invisible). Al cambiar el end, le decimos: "No saltes de línea, mejor pon tres puntos y quédate ahí mismo".

Segunda línea: Como la primera no saltó de línea, el texto "Python" se pega justo después de los tres puntos.

# LAB Dando formato a la salida
Optimización con \n
Se redujeron múltiples llamadas a print() utilizando el carácter de escape \n (newline). Esto permite que una sola cadena de texto se distribuya en varias líneas físicas en la terminal.

Ejemplo: print(" *\n* *") genera un salto de línea sin necesidad de un segundo comando.

Multiplicación de Strings (* 2)
Se utilizó el operador aritmético * aplicado a cadenas para duplicar elementos visuales. Esto demostró que en Python, multiplicar un string por un entero concatena el texto consigo mismo esa cantidad de veces.

Uso: print(" * " * 2) imprime dos puntas de flecha una al lado de la otra.

Análisis de Errores (Depuración)
Localización del Error: Al eliminar una comilla, Python a veces marca el error en la línea siguiente. Esto sucede porque el intérprete sigue buscando el cierre de la cadena hasta que encuentra algo que "rompe" la lógica del programa más adelante.

Comillas vs Apóstrofes: Se confirmó que ' y " son intercambiables, pero no se pueden mezclar (ej. 'Hola" causará error).

Case Sensitivity: Se reafirmó que print es la instrucción correcta y cualquier variación como Print o PRINT resultará en un NameError.



# Seccion 2 - LAB  Literales de Python - Cadenas
\": Esto le dice a Python: "No cierres el comando, simplemente dibuja una comilla doble en la pantalla".

\n: Es el salto de línea para que cada palabra aparezca debajo de la anterior.

La lógica: Para obtener tres comillas juntas en el output ("""), necesitas escribir \"\"\" en el código.


# La seccion3 tiene su propio MD llamando operadores.md, en donde esta el paso a paso de los 15 ejercicios propuestos por el instructor


# Seccion 4 y sus laboratorios

# LAB Variables

 Se utilizaron los identificadores (john, mary, adam) para almacenar los valores enteros.

Operaciones con Variables: Se demostró que las variables pueden sumarse entre sí y el resultado puede ser almacenado en una nueva variable (total_apples).

Concatenación implícita: En Python, al usar la función print() y separar elementos con comas, podemos mostrar texto (String) y números (Integer) en la misma línea sin errores, ya que la función añade un espacio automáticamente.


# LAB  Variables: un convertidor simple
En este ejercicio se desarrolló un programa que realiza conversiones entre millas y kilómetros, utilizando variables flotantes y funciones de redondeo.
Lógica de Conversión Aplicada: 
Para la implementación se utilizó el factor de conversión estándar: 1 milla ≈ 1.61 km. De Millas a Kilómetros: Se multiplica el valor de las millas por el factor (millas \times 1.61).
De Kilómetros a Millas: Se realiza la operación inversa, dividiendo los kilómetros por el factor (km / 1.61).
Conceptos Clave Utilizados: La Función round(): Se implementó para limitar el número de decimales a 2 (round(valor, 2)). Esto es fundamental al trabajar con divisiones que generan decimales infinitos, mejorando la legibilidad del output.
Múltiples Argumentos en print(): El programa demuestra cómo concatenar variables (números) y literales (cadenas de texto) en una sola línea de consola separándolos por comas.
Precisión de Datos: Se asignaron valores iniciales como 7.38 y 12.25, que Python identifica automáticamente como tipos float (punto flotante).


# LAB  Operadores y expresiones
Operador de Potencia (**): En álgebra escribimos x^3, pero en Python debemos usar x **3.
Multiplicación Explícita: Python no entiende 3x; es obligatorio poner el asterisco 3*x.
Jerarquía de Operaciones: Python resolverá primero las potencias (**), luego las multiplicaciones (*) y finalmente las sumas y restas. 

Esto coincide perfectamente con la prioridad matemática que se debe tener.

Y la prioridad de ejecucion es la siguiente
Orden - Operador - Descripción
1°        ()        Paréntesis
2°        **        Exponenciación
3°   *, /, %, //    Multiplicación y Divisiones
4°      +, -         Suma y Resta

