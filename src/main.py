"""TaskTracker - cadastro e listagem de tarefas (Bootcamp II - Fase 2)."""

PRIORIDADES = {"alta": "Alta", "media": "Média", "média": "Média", "baixa": "Baixa"}
ORDEM_PRIORIDADE = {"Alta": 0, "Média": 1, "Baixa": 2}


def pedir_titulo():
    """Repete a pergunta até receber um título não vazio."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: o título não pode ficar vazio.")


def pedir_prioridade():
    """Aceita apenas Alta, Média (ou Media) e Baixa."""
    while True:
        prioridade = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
        if prioridade in PRIORIDADES:
            return PRIORIDADES[prioridade]
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas):
    print("\n--- Nova tarefa ---")
    titulo = pedir_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = pedir_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA ou texto livre): ").strip()
    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f"Tarefa {tarefa['id']} cadastrada com sucesso!")


def exibir_tarefas(tarefas):
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    ordenadas = sorted(
        tarefas,
        key=lambda tarefa: (
            tarefa["status"] == "Concluída",
            ORDEM_PRIORIDADE[tarefa["prioridade"]],
            tarefa["id"],
        ),
    )
    for tarefa in ordenadas:
        print(f"\nID: {tarefa['id']}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao'] or '(sem descrição)'}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite'] or '(não informada)'}")
        print(f"Status: {tarefa['status']}")

    total_concluidas = sum(tarefa["status"] == "Concluída" for tarefa in tarefas)
    print(f"\nTotal de tarefas: {len(tarefas)} | Concluídas: {total_concluidas}")


def main():
    tarefas = []
    while True:
        print("\n===== TASKTRACKER =====")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            exibir_tarefas(tarefas)
        elif opcao == "3":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
