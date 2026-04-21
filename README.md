# Fundamentos de Python
# Seccion1 - LAB  Trabajando con la función print()
El archivo hola.py contiene la instrucción básica para imprimir en consola:
print("Hola, Mundo!")

print(): Es una función integrada de Python que envía información a la salida estándar (la terminal) - 
"Hola, Mundo!": Es una cadena de texto (string). Debe ir entre comillas para que Python la reconozca como texto y no como una variable - Propósito: Validar que el intérprete de Python 3.12 está correctamente configurado y ejecutando código.

# Seccion1 - LAB  La función print() y sus argumentos
sep="***": Por defecto, print pone un espacio entre cada palabra. Al usar sep (separador), le ordenamos que meta tres asteriscos entre "Programming", "Essentials" e "in".

end="...": Por defecto, print salta a la siguiente línea al terminar (un \n invisible). Al cambiar el end, le decimos: "No saltes de línea, mejor pon tres puntos y quédate ahí mismo".

Segunda línea: Como la primera no saltó de línea, el texto "Python" se pega justo después de los tres puntos.

# Seccion1 - LAB Dando formato a la salida
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


