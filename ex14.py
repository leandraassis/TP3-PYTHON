def receberTexto():
    """Recebe uma string
    
    retorno: string
    """
    texto = input("Digite uma frase: ")
    return texto

def separarTexto(texto):
    """Separa as primeiras e ultimas 5 letras de uma string e as exibe

    parametros: texto (string) 
    """
    parteUm = texto[:5]
    parteDois = texto[-5:]
    print(f"Cinco primeiras letras: {parteUm}")
    print(f"Cinco últimas letras: {parteDois}")


separarTexto(receberTexto())