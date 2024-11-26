def verificadorPalindromo(texto):
    """Verifica se uma string é um palíndromo

        parametro: texto (string)

        retorno: boolean
    """
    textoFormatado = ''.join(texto.split()).lower()
    return textoFormatado == textoFormatado[::-1]

def mostrarResultados():
    texto = input("Digite uma palavra ou frase: ")
    if(verificadorPalindromo(texto)):
        print(f"A palavra/frase digitada é um palíndromo.")
    else:
        print(f"A palavra/frase digitada não é um palíndromo.")

mostrarResultados()