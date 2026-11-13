# ListaFácil — Gerenciador de Tarefas

Aplicação web de gerenciamento de tarefas desenvolvida como projeto de estudo de operações CRUD (Create, Read, Update e Delete), utilizando Python, Flask, SQLAlchemy e SQLite.

## Funcionalidades

- **Create:** cadastrar tarefas com título e descrição.
- **Read:** listar as tarefas cadastradas.
- **Update:** editar título e descrição.
- **Delete:** excluir tarefas.
- Alterar o status entre pendente e concluída.
- Armazenar os dados localmente em um banco SQLite.

## Tecnologias

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML5
- CSS3

## Como executar o projeto

### 1. Pré-requisitos

Instale o [Python](https://www.python.org/downloads/) e o [Visual Studio Code](https://code.visualstudio.com/).

Durante a instalação do Python no Windows, marque a opção **Add Python to PATH**.

### 2. Abra o projeto no VS Code

Extraia a pasta do projeto. No VS Code, acesse **File > Open Folder** e selecione a pasta `gerenciador_tarefas_crud`.

### 3. Crie um ambiente virtual

Abra o terminal integrado do VS Code (**Terminal > New Terminal**) e execute:

```bash
python -m venv .venv
```

No Windows, ative o ambiente:

```powershell
.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação, você pode usar o Prompt de Comando:

```bat
.venv\Scripts\activate.bat
```

### 4. Instale as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
python app.py
```

Abra o navegador no endereço:

http://127.0.0.1:5000

O banco de dados SQLite será criado automaticamente na primeira execução.

Para encerrar o servidor, pressione `Ctrl + C` no terminal.

## Estrutura do projeto

```text
gerenciador_tarefas_crud/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    ├── base.html
    ├── index.html
    └── editar.html
```

## Conceitos praticados

- Rotas e métodos HTTP (`GET` e `POST`).
- Operações CRUD.
- Modelagem de dados com SQLAlchemy.
- Persistência de dados com SQLite.
- Formulários HTML.
- Templates com Jinja.
- Organização de arquivos em uma aplicação Flask.
- Controle de versão com Git e publicação no GitHub.


## Autor

Desenvolvido como projeto de estudo de desenvolvimento web e operações CRUD.
