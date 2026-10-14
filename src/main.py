"""TaskTracker - aplicação de tarefas em Python para o Bootcamp II (Fase 2)."""

PRIORIDADES = {"alta": "Alta", "media": "Média", "média": "Média", "baixa": "Baixa"}
ORDEM_PRIORIDADE = {"Alta": 0, "Média": 1, "Baixa": 2}


def pedir_titulo():
    """Solicita novamente quando o título está em branco."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: o título não pode ficar vazio.")


def pedir_prioridade():
    """Aceita apenas Alta, Média/Media ou Baixa."""
    while True:
        resposta = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
        if resposta in PRIORIDADES:
            return PRIORIDADES[resposta]
        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas):
    """Cria uma tarefa com ID único e status inicial Pendente."""
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
    """Exibe todas as propriedades, ordenadas por status e prioridade."""
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

    concluidas = sum(tarefa["status"] == "Concluída" for tarefa in tarefas)
    print(f"\nTotal de tarefas: {len(tarefas)} | Concluídas: {concluidas}")


def concluir_tarefa(tarefas):
    """Marca uma tarefa como concluída se ela existe e está pendente."""
    pendentes = [tarefa for tarefa in tarefas if tarefa["status"] == "Pendente"]
    if not pendentes:
        print("Não há tarefas pendentes para concluir.")
        return

    while True:
        resposta = input("Deseja concluir uma tarefa? (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            break
        if resposta in ("n", "não", "nao"):
            return
        print("Resposta inválida. Digite s ou n.")

    print("IDs pendentes:", ", ".join(str(tarefa["id"]) for tarefa in pendentes))
    identificador = input("Digite o ID da tarefa para concluir: ").strip()
    if not identificador.isdecimal():
        print("Erro: informe um ID numérico válido.")
        return

    tarefa = next((t for t in tarefas if t["id"] == int(identificador)), None)
    if tarefa is None:
        print("Erro: tarefa não encontrada.")
    elif tarefa["status"] != "Pendente":
        print("Erro: esta tarefa já foi concluída.")
    else:
        tarefa["status"] = "Concluída"
        print(f"Tarefa {tarefa['id']} marcada como concluída com sucesso!")
        concluidas = sum(t["status"] == "Concluída" for t in tarefas)
        print(f"Total de tarefas: {len(tarefas)} | Concluídas: {concluidas}")


def main():
    tarefas = []
    while True:
        print("\n===== TASKTRACKER =====")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        try:
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                cadastrar_tarefa(tarefas)
            elif opcao == "2":
                exibir_tarefas(tarefas)
                if tarefas:
                    concluir_tarefa(tarefas)
            elif opcao == "3":
                print("Até logo!")
                break
            else:
                print("Opção inválida. Escolha 1, 2 ou 3.")
        except (EOFError, KeyboardInterrupt):
            print("\nAplicação encerrada.")
            break


if __name__ == "__main__":
    main()
