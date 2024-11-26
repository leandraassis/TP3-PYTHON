def validaTelefone(telefone):
    """Valida se o número de telefone tem 11 dígitos e se esses digitos são numeros

        parametros: telefone (int)

        retorno: boolean
    """
    return (len(telefone) == 11 and telefone.isdigit())

def formataTelefone(telefone):
    """Formata o número de telefone no formato (99) 99999-9999

        parametros: telefone (int)

        retorno: string
    """
    telefoneFormatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    return telefoneFormatado

def exibeResultados():
    """Recebe o telefone e o exibe formatado"""
    while(True):
        telefone = input("Digite um número de telefone (11 digitos): ")
        if(validaTelefone(telefone)):
            telefoneFormatado = formataTelefone(telefone)
            print(f"Telefone formatado: {telefoneFormatado}")
            break
        else:
            print("Erro: O numero de telefone precisa ter 11 digitos NUMÉRICOS.")

exibeResultados()


