def receberTexto():
    """Recebe uma string via input

        retorno: string
    """
    texto = input("Digite uma palavra ou texto: ")
    return texto

def verificaVogais(texto):
    """Verifica quantas vogais um texto tem

        parametro: texto (string)
        
        retorno: int
    """
    vogais = ["a", "e", "i", "o", "u"]
    texto = texto.lower()
    vogaisEncontradas = 0
    for letra in texto:
        if(letra in vogais):
            vogaisEncontradas += 1
    return vogaisEncontradas

def exibirResultado():
    """Exibe texto e quantidadae de vogais presentes no texto

        parametros: vogaisEncontradas (int)
    """
    texto = receberTexto()
    qtdVogais = verificaVogais(texto)
    print(f"A palavra/frase '{texto}' tem {qtdVogais} vogais.")


exibirResultado()