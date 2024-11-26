def recebeTexto():
    """Recebe string
    
        retorno: string
    """
    texto = input("Digite uma frase/palavra: ")
    return texto

def inverteTexto(texto):
    """Inverte uma string

        parametros: texto (string)

        retorno: string (invertida)
    """
    textoInvertido = ""
    #tbm dava pra fazer com for + reversed
    for i in range(len(texto) - 1, -1, -1):
        textoInvertido += texto[i]
    return textoInvertido
 
def exibeResultado():
    """Exibe texto invertido"""
    textoFim = recebeTexto()
    print(f"Texto invertido: {inverteTexto(textoFim)}")

exibeResultado()