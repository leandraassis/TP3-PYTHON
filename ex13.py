def inverterFrase():
    """Recebe e inverte string"""
    texto = input("Digite uma palavra ou frase: ")
    textoInvertido = texto[::-1]
    print(textoInvertido)

inverterFrase()