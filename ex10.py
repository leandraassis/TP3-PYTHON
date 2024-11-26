def validaNumero(numero):
    """Valida se é um número entre 1 e 7"""
    return (numero.isdigit() and int(numero) >= 1 and int(numero) <= 7)

def exibeResultados():
    """Recebe o numero e exibe dia da semana"""
    diaSemana = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado"
    }
    numero = input("Digite um número de 1 a 7 que representa um dia da semana: ")
    if(validaNumero(numero)):
        numero = int(numero)
        print(f"{diaSemana[numero]}")
    else:
        print("Erro: Digite um NÚMERO de 1 (um) a 7 (sete).")

exibeResultados()