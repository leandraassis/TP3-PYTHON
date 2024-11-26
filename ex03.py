def verificadorNome():
    """Recebe e foormata uma string"""
    while(True):
        nomeDigitado = input("Digite seu primero e último nome: ")
        nomeSobrenome = nomeDigitado.split(" ")
        if(len(nomeSobrenome) < 2):
            print("Erro: digite seu PRIMEIRO E ÚLTIMO nome.")
        else: 
            nomeSobrenome[0] = nomeSobrenome[0].capitalize()
            nomeSobrenome[1] = nomeSobrenome[1].upper()
            print(f"{nomeSobrenome[1]}, {nomeSobrenome[0]}")
            break

verificadorNome()