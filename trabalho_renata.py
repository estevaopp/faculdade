#candidatos a emprego
def criar_vetores():
    candidatos = ["Matheus", "Weverton", "Mayra", "Estêvão"]
    idade = [20,21,22,23]
    return candidatos, idade


def cadastrar_dados(candidatos, idade):
    print("Cadastro")
    novo_candidato = input("Nome: ")
    nova_idade = int(input("Idade: "))
    while novo_candidato.isdigit() or not(nova_idade >= 18 and nova_idade < 70):
        print("Cadastro Invalido")
        print("")
        print("Cadastro")
        novo_candidato = input("Nome: ")
        nova_idade = int(input("Idade: "))
    candidatos.append(novo_candidato)
    idade.append(nova_idade)
    print("Cadastro concluido!")


def pesquisar_indice_candidato(candidatos):
    pesquisa = input("Nome: ")
    for indice, nome in enumerate(candidatos):
        if pesquisa.lower() == nome.lower():
            return indice
    print("Não encontrado.")


def alterar_cadastro(indice, candidatos, idade):
    nome_alterado = input("Nome alterado: ")
    idade_alterada = int(input("Idade alterada: "))
    while nome_alterado.isdigit() or not(idade_alterada >= 18 and idade_alterada < 70):
        print("Alteração Invalida")
        print("")
        nome_alterado = input("Nome alterado: ")
        idade_alterada = int(input("Idade alterada: "))
    candidatos[indice] = nome_alterado
    idade[indice] = idade_alterada
    print("Candidato alterado com sucesso!")


candidatos, idade = criar_vetores()


abrir_novo_cadastro = input("Deseja criar um cadastro (s ou n): ")
print("")
while abrir_novo_cadastro == "s":
    cadastrar_dados(candidatos, idade)
    print("")
    abrir_novo_cadastro = input("Deseja criar novo cadastro (s ou n): ")
    print("")


abrir_procura = input("Deseja procurar um candidato (s ou n): ")
print("")
while abrir_procura == "s":
    indice = pesquisar_indice_candidato(candidatos)
    if type(indice) == int:
        print(f"Nome: {candidatos[indice]} | Idade: {idade[indice]}")
    print("")
    abrir_procura = input("Deseja procurar um outro candidato (s ou n): ")
    print("")


abrir_alteracao = input("Deseja alterar um cadastro (s ou n): ")
print("")
while abrir_alteracao == "s":
    indice = pesquisar_indice_candidato(candidatos)
    if type(indice) == int:
        alterar_cadastro(indice, candidatos, idade)
    print("")
    abrir_alteracao = input("Deseja procurar um outro cadastro (s ou n): ")
    print("")

for indice, nome in enumerate(candidatos):
    print(f"Nome: {candidatos[indice]} | Idade: {idade[indice]}")
print("")





