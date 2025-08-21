def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

# Programa principal en bucle
while True:
    frase = input("Escribe una palabra o frase (o escribe 'salir' para terminar): ")

    if frase.lower() == "salir":
        print("¡Programa terminado!")
        break 

    if es_palindromo(frase):
        print(True)
    else:
        print(False)
