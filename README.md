El link al repositorio es: [github](https://github.com/GonzaloGmv/atbash)  

Los que hemos hecho este trabajo somos:
- Carlos Puigserver
- Gonzalo Martínez


Concepto matemático:

El cifrado de Atbash es un tipo de cifrado por sustitución en el que cada letra del alfabeto se reemplaza por su letra opuesta en el mismo alfabeto. Es decir, la primera letra se reemplaza por la última, la segunda por la penúltima, y así sucesivamente.

Fórmula:
Dada una letra p  del alfabeto original, la fórmula para calcular su correspondiente letra cifrada c en el cifrado de Atbash es:

c=(25-p)

Donde la letra p es el índice de la letra en el alfabeto.

Esto es viendo que A en el índice es el número 0, es decir, empezamos a contar desde 0. Si por el contrario empezásemos en uno, sería la misma fórmula +1, o cambiando el 25 por un 26:

c=(25-p)+1
c=(26-p)

El código que hemos realizado es el siguiente:

![bb](https://github.com/GonzaloGmv/atbash/assets/91721643/54ce4d72-b586-456c-8b6d-8e3f0cafbf3b)





