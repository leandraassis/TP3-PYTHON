def validarData(dia, mes, ano):
    """Valida uma data"""
    match(mes):
        case 4 | 6 | 9 | 11:
            if((dia >= 1) and (dia <= 30)):
                print("Data válida!")
            else:
                print("Dia inválido!")
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if((dia >= 1) and (dia <= 31)):
                print("Data válida!")
            else: 
                print("Dia inválido!")
        case 2:
            if((ano % 4) == 0):
                if((dia >= 1) and (dia <= 29)):
                    print("Data válida!")
                else:
                    print("Dia inválido!")
            else:
                if((dia >= 1) and (dia <= 28)):
                    print("Data válida!")
                else:
                    print("Dia inválido!")
        case _: 
            print("Mês inválido!")
            
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
    validarData(dia, mes, ano)

exibirData()