def validaCpf(cpf):
    """Valida se o número de cpf tem 11 dígitos e se esses digitos são numeros

        parametros: cpf (int)

        retorno: boolean
    """
    return (len(cpf) == 11 and cpf.isdigit())

def formataCpf(cpf):
    """Formata o número de cpf no formato 999.999.999-99.

        parametros: cpf (int)

        retorno: string
    """
    cpfFormatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpfFormatado

def exibeResultados():
    """Recebe o cpf e o exibe formatado"""
    while(True):
        cpf = input("Digite um número de cpf (11 digitos): ")
        if(validaCpf(cpf)):
            cpfFormatado = formataCpf(cpf)
            print(f"CPF formatado: {cpfFormatado}")
            break
        else:
            print("Erro: O CPF precisa ter 11 digitos NUMÉRICOS.")

exibeResultados()