# TaskTracker

Projeto da **Fase 2 do Bootcamp II** — aplicação simples de gerenciamento de tarefas em Python.

## Objetivo

O TaskTracker permite organizar atividades em uma lista. Cada tarefa possui um identificador,
título, descrição, prioridade, data limite e status.

## Funcionalidades

- Cadastrar tarefas com título obrigatório e prioridade válida (Alta, Média/Media ou Baixa).
- Impedir o cadastro de tarefas com título vazio ou somente espaços.
- Listar tarefas, mostrando todas as informações, com pendentes primeiro e por prioridade.
- Exibir os totais de tarefas cadastradas e concluídas.
- Marcar como concluída uma tarefa pendente a partir da opção de listagem.
- Informar quando a lista estiver vazia e avisar sobre entradas inválidas.

## Tecnologias

- Python 3.9 ou superior (biblioteca padrão; sem pacotes externos).
- Git e GitHub para controle de versões.

## Organização do projeto

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Como executar

1. Instale Python 3.
2. Abra um terminal na pasta `tasktracker-projeto`.
3. Execute:

   **Windows:**
   ```powershell
   py src/main.py
   ```

   **macOS/Linux:**
   ```bash
   python3 src/main.py
   ```

## Menu principal

```text
===== TASKTRACKER =====
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação
```

Na opção **2**, após listar as tarefas, é possível informar o ID de uma tarefa para
marcá-la como concluída. Dessa forma, o menu principal permanece com as três opções
exigidas no documento da Fase 2 e também contempla a conclusão de tarefas prevista na Fase 1.

## Regras

- **Título:** obrigatório; campos vazios e espaços são rejeitados.
- **Prioridade:** somente Alta, Média (ou Media) e Baixa, sem distinguir letras maiúsculas/minúsculas.
- **Data limite:** texto livre conforme o requisito da Fase 2; recomenda-se DD/MM/AAAA.
- **Status inicial:** Pendente.
- **ID:** numérico, único durante a execução.
- **Conclusão:** só pode acontecer se o ID existir e a tarefa estiver pendente.

**Observação:** nesta etapa, as tarefas são mantidas apenas na memória enquanto o programa está aberto.
Ao encerrar, elas não são salvas em um banco de dados ou arquivo. A persistência não foi exigida para a Fase 2.

## Planejamento original

O documento entregue na Fase 1 está em `docs/planejamento_logico.pdf`.

## Próxima etapa

A Fase 3 prevê empacotamento, testes, Docker e deploy.
