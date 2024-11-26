def recebeNome():
    """Recebe duas strings - nome e sobrenome

        retorno: string 
    """
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    return nome + " " + sobrenome

def exibeNome(nome):
    """Exibe uma string

        parametros: nome (string)
    """
    print(f"Olá, {nome}!")

exibeNome(recebeNome())


