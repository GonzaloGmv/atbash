El link al repositorio es: [github](https://github.com/GonzaloGmv/atbash)

Los que hemos hecho este trabajo somos:
- Carlos Puigserver
- Gonzalo Martínez


Concepto matemático:

Asignación de valores numéricos a las letras del alfabeto: Primero, necesitamos asignar un valor numérico a cada letra del alfabeto. Podemos hacer esto utilizando la codificación ASCII, donde cada letra tiene un valor numérico único.

Inversión de los valores numéricos: En el cifrado de Atbash, la clave está en invertir estos valores numéricos. Esto significa que la primera letra del alfabeto tendrá el valor numérico más alto, y viceversa.

Fórmula:

Para cifrar una letra p del alfabeto, seguimos estos pasos:

Obtenemos el valor numérico asociado a la letra original p
Invertimos este valor numérico para obtener el valor de la letra cifrada c
Convertimos este valor numérico nuevamente en la letra cifrada c

Para la inversión, podemos utilizar la siguiente fórmula:
c=25-(p-97)
Donde:
p es el valor numérico de la letra original (en minúscula), y 97 es el valor numérico de la letra 'a' en ASCII.

