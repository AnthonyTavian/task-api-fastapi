# 🎯 Task Management API

API REST para gerenciamento de tarefas desenvolvida com FastAPI e SQLite.

## 🚀 Tecnologias

- Python 3.11+
- FastAPI
- SQLAlchemy (ORM)
- SQLite
- Pydantic
- Uvicorn

## 📋 Funcionalidades

- ✅ Criar novas tarefas
- ✅ Listar todas as tarefas
- ✅ Buscar tarefa por ID
- ✅ Atualizar tarefas
- ✅ Deletar tarefas
- ✅ Documentação automática (Swagger/OpenAPI)
- ✅ Validação de dados com Pydantic

## 🔧 Como executar

### Pré-requisitos
- Python 3.11 ou superior
- pip

### Instalação

1. Clone o repositório
```bash
git clone https://github.com/AnthonyTavian/task-api-fastapi.git
cd task-api-fastapi
```

2. Crie e ative o ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute a aplicação
```bash
uvicorn main:app --reload
```

5. Acesse a documentação interativa
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📡 Endpoints

### Tasks

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/tasks` | Lista todas as tarefas |
| GET | `/tasks/{id}` | Busca tarefa por ID |
| POST | `/tasks` | Cria nova tarefa |
| PUT | `/tasks/{id}` | Atualiza tarefa |
| DELETE | `/tasks/{id}` | Deleta tarefa |

## 📦 Estrutura do Projeto
```
task-api-fastapi/
├── main.py           # Endpoints da API
├── models.py         # Modelos do banco de dados
├── schemas.py        # Schemas Pydantic
├── database.py       # Configuração do banco
├── requirements.txt  # Dependências
└── README.md
```

## 🎓 Aprendizados

Este projeto foi desenvolvido para aprender e demonstrar:
- Desenvolvimento de APIs REST com FastAPI
- Operações CRUD completas
- Integração com banco de dados usando SQLAlchemy
- Validação de dados com Pydantic
- Documentação automática de APIs
- Boas práticas de estruturação de projetos Python

## 📝 Licença

MIT License

## 👤 Autor

**Anthony Tavian**
- GitHub: [@AnthonyTavian](https://github.com/AnthonyTavian)
- LinkedIn: [anthonytavian](https://www.linkedin.com/in/anthonytavian/)