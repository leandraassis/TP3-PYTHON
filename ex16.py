def validaNumero(numero):
    """Valida se é um número"""
    return numero.isdigit() 

def mediaNumeros():
    """Recebe e calcula a media de dois numeros

        retorno: float ou None
    """
    n1 = input("Digite o primeiro número: ")
    if(validaNumero(n1)): 
        n1 = int(n1)
        n2 = input("Digite o segundo número: ")
        if(validaNumero(n2)):
            n2 = int(n2)
            media = (n1 + n2)/2
            return media
        else:
            return None
    else:
        return None
    
def exibeResultado(media):
    """Exibe uma média

        parametros: media (float)
    """
    if(media):
        print(f"A média entre os números é {media}")
    else:
        print("Você não digitou um número válido, tente novamente.")

exibeResultado(mediaNumeros())