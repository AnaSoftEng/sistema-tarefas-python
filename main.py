tarefas = []

def adicionar_tarefa():
    nome = input("Digite a tarefa: ")
    tarefas.append({"nome": nome, "concluida": False})
    print("Tarefa adicionada!\n")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return
    
    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else "✘"
        print(f"{i} - {tarefa['nome']} [{status}]")
    print()

def concluir_tarefa():
    listar_tarefas()
    try:
        i = int(input("Digite o número da tarefa: "))
        tarefas[i]["concluida"] = True
        print("Tarefa concluída!\n")
    except:
        print("Erro ao concluir tarefa.\n")

def menu():
    while True:
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Sair")
        
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            break
        else:
            print("Opção inválida\n")

menu()