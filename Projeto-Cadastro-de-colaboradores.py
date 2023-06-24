lista_colaboradores = []  # Lista vazia para armazenar os colaboradores
id_global = 0  # Variável para controlar o ID dos colaboradores

# Função para cadastrar um colaborador
def cadastrar_colaborador(id):
    global id_global
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    pagamento = float(input("Digite o pagamento do colaborador: "))

    # Cria um dicionário com os dados do colaborador
    colaborador = {"ID": id, "Nome": nome, "Setor": setor, "Pagamento": pagamento}

    # Adiciona o dicionário à lista de colaboradores
    lista_colaboradores.append(colaborador)

    id_global += 1  # Incrementa o ID global

# Função para consultar colaboradores
def consultar_colaborador():
    opcao = input("Digite a opção desejada (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu): ")

    if opcao == "1":
        print("Consulta de Todos os Colaboradores:")
        for colaborador in lista_colaboradores:
            print(colaborador)

    elif opcao == "2":
        id_consulta = int(input("Digite o ID do colaborador a ser consultado: "))
        encontrado = False
        for colaborador in lista_colaboradores:
            if colaborador["ID"] == id_consulta:
                print("Colaborador encontrado:")
                print(colaborador)
                encontrado = True
                break
        if not encontrado:
            print("Colaborador não encontrado.")

    elif opcao == "3":
        setor_consulta = input("Digite o setor dos colaboradores a serem consultados: ")
        encontrados = []
        for colaborador in lista_colaboradores:
            if colaborador["Setor"] == setor_consulta:
                encontrados.append(colaborador)
        if encontrados:
            print("Colaboradores encontrados:")
            for colaborador in encontrados:
                print(colaborador)
        else:
            print("Nenhum colaborador encontrado para o setor informado.")

    elif opcao == "4":
        return  # Retorna ao menu principal

    else:
        print("Opção inválida.")

# Função para remover um colaborador
def remover_colaborador():
    id_remocao = int(input("Digite o ID do colaborador a ser removido: "))
    encontrado = False
    for colaborador in lista_colaboradores:
        if colaborador["ID"] == id_remocao:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso.")
            encontrado = True
            break
    if not encontrado:
        print("Colaborador não encontrado.")

# Função principal para o menu
def main():
    print("Bem-vindo Raniff Barroncas Silva!")

    while True:
        print("\nMenu:")
        print("1. Cadastrar Colaborador")
        print("2. Consultar Colaborador")
        print("3. Remover Colaborador")
        print("4. Encerrar Programa")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar_colaborador(id_global)
        elif opcao == "2":
            consultar_colaborador()
        elif opcao == "3":
            remover_colaborador()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

# Executa a função principal
main()