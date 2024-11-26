def entrarData():
    """Recebe uma data em formato de string

        retorno: string (data em string)
    """
    data = input("Entre com a data dd/mm/aaaa: ")
    return data

def dividirData(data):
    """Divide uma data (string) em numeros inteiros
        
        parametro: string no formato: dd/mm/aaaa

        retorno: int (dia, mes, ano)
    """
    diaMesAno = data.split("/")
    dia = int(diaMesAno[0])
    mes = int(diaMesAno[1])
    ano = int(diaMesAno[2])
    return dia, mes, ano

def exibirData():
    """Exibe a data em inteiros"""
    data = entrarData()
    dia, mes, ano = dividirData(data)
    print(f"Dia: {dia}")
    print((f"Mês: {mes}"))
    print(f"Ano: {ano}")


exibirData()