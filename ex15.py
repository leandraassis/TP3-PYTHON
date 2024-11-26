def receberString():
    """Recebe uma string

        retorno: string
    """
    texto = input("Digite sua idade, nome e salário conforme o exemplo - 12;Maria;1000: ")
    return texto

def substituir(texto):
    """Substitui ; por , de uma string e exibe

    parametros: texto (string)
    """
    textoSubs = texto.replace(";", ",")
    print(f"Texto formatado: {textoSubs}")

substituir(receberString())