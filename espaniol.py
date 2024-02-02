def cifrado_atbash(texto):
    alfabeto_original = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_clave = 'zyxwvutsrqponmlkjihgfedcba'
    texto_cifrado = ''

    for caracter in texto:
        if caracter.lower() in alfabeto_original:
            indice = alfabeto_original.index(caracter.lower())
            if caracter.isupper():
                texto_cifrado += alfabeto_clave[indice].upper()
            else:
                texto_cifrado += alfabeto_clave[indice]
        else:
            texto_cifrado += caracter

    return texto_cifrado

# Solucion
texto_original = "gsvuoztrhhzbdvzivxizab"
texto_cifrado = cifrado_atbash(texto_original)
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)
