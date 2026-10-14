"""TaskTracker - Bootcamp II, Fase 2."""


def main():
    while True:
        print("\n===== TASKTRACKER =====")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            print("Cadastro em desenvolvimento.")
        elif opcao == "2":
            print("Listagem em desenvolvimento.")
        elif opcao == "3":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
