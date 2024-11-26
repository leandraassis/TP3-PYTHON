def validarData(dia, mes, ano):
    """Valida uma data
        
        parametros: dia (int), mes (int), ano (int)

        returno: boolean
    """
    match(mes):
        case 4 | 6 | 9 | 11:
            if((dia >= 1) and (dia <= 30)):
                return True
            else:
                return False
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if((dia >= 1) and (dia <= 31)):
                return True
            else: 
                return False
        case 2:
            if((ano % 4) == 0):
                if((dia >= 1) and (dia <= 29)):
                    return True
                else:
                    return False
            else:
                if((dia >= 1) and (dia <= 28)):
                    return True
                else:
                    return False
        case _: 
            return False
            
def entrarData():
    """Recebe uma data em formato de string

        retorno: string (data em string)
    """
    data = input("Entre com a data dd/mm/aaaa: ")
    return data

def dividirData(data):
    """Divide uma data (string) em numeros inteiros
        
        parametro: string no formato: dd/mm/aaaa

        retorno: int (dia, mes, ano) ou None
    """
    try:
        diaMesAno = data.split("/")
        dia = int(diaMesAno[0])
        mes = int(diaMesAno[1])
        ano = int(diaMesAno[2])
        return dia, mes, ano
    except:
        print("Erro: formato de data inválido. Use dd/mm/aaaa.")
        return None, None, None

def formatarData():
    """Formata uma data"""
    data = entrarData()
    dia, mes, ano = dividirData(data)

    meses = {
        1: "Janeiro", 
        2: "Fevereiro", 
        3: "Março", 
        4: "Abril", 
        5: "Maio", 
        6: "Junho", 
        7: "Julho", 
        8: "Agosto", 
        9: "Setembro", 
        10: "Outubro", 
        11: "Novembro", 
        12: "Dezembro"
    }
    
    if(validarData(dia, mes, ano)):
        print(f"{dia} de {meses[mes]} de {ano}")
    else:
        print("Erro: data inválida.")

formatarData()