def atbash_cifrado(mensaje):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mensaje_cifrado = ''

    for letra in mensaje:
        if letra.isalpha():  # Verifica si es una letra
            indice = alfabeto.index(letra.upper())  # Obtiene el índice de la letra en el alfabeto
            letra_cifrada = alfabeto[25 - indice]  # Aplica la fórmula Atbash
            if letra.islower():
                letra_cifrada = letra_cifrada.lower()  # Mantiene la capitalización original
            mensaje_cifrado += letra_cifrada
        else:
            mensaje_cifrado += letra  # Conserva caracteres no alfabéticos

    return mensaje_cifrado

# Ejemplo de uso:
mensaje_original = "gsvuoztrhhzbdvzivxizab"
mensaje_cifrado = atbash_cifrado(mensaje_original)
print("Mensaje original:", mensaje_original)
print("Mensaje cifrado:", mensaje_cifrado)
