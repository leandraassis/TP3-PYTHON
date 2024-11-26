def verificadorNome():
    """Recebe e verifica uma string"""
    while(True):
        nomeDigitado = input("Digite seu primero e último nome: ")
        nomeSobrenome = nomeDigitado.split(" ")
        if(len(nomeSobrenome) < 2):
            print("Erro: digite seu PRIMEIRO E ÚLTIMO nome.")
        elif(len(nomeSobrenome[0]) < 2 or len(nomeSobrenome[1]) < 2):
            print("Primeiro e último nome precisam ter mais de duas letras")
        else: 
            print(f"Olá, {nomeSobrenome[0]} {nomeSobrenome[1]}!")
            break

verificadorNome()
