tarefas = []

while True:
    print("\n1. Adicionar  2. Listar  3. Sair")
    op = input("Escolha: ")

    if op == "1":
        tarefas.append(input("Tarefa: "))
    elif op == "2":
        for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t}")
    elif op == "3":
        break
    else:
        print("Opção inválida!")
