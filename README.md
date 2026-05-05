# 🤖 Projeto de Automação de Testes

Projeto desenvolvido para a disciplina de **Testes** do curso de Engenharia de Software — ICEV.

Automatização de testes de **API REST** e **Web E2E**, com integração contínua via GitHub Actions.

---

## 📁 Estrutura do Projeto

```
projeto-teste/
├── .github/
│   └── workflows/
│       └── main.yml        # Pipeline de CI/CD
├── web-tests/
│   ├── pages/                   # Page Objects (Selenium)
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── tests/
│   │   ├── conftest.py
│   │   └── test_checkout.py     # Testes E2E
│   ├── requirements.txt
│   └── pytest.ini
├── petstore-collection.json     # Coleção Postman
├── petstore-environment.json    # Environment Postman
├── test.png                     # Imagem usada nos testes de upload
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Postman | Criação e execução dos testes de API |
| Newman | Execução da coleção Postman via linha de comando |
| Python 3.12 | Linguagem dos testes Web |
| Selenium | Automação do navegador |
| pytest | Framework de testes Web |
| GitHub Actions | Pipeline de CI/CD |

---

## 🔌 Automação de API — Petstore Swagger

**Base URL:** `https://petstore.swagger.io/v2`

### Endpoints cobertos

**Pet**
- `POST /pet` — Criar pet
- `GET /pet/{petId}` — Buscar pet por ID
- `GET /pet/findByStatus` — Buscar pets por status
- `PUT /pet` — Atualizar pet
- `POST /pet/{petId}` — Atualizar pet via form data
- `POST /pet/{petId}/uploadImage` — Upload de imagem
- `DELETE /pet/{petId}` — Deletar pet

**Store**
- `GET /store/inventory` — Consultar inventário
- `POST /store/order` — Criar pedido
- `GET /store/order/{orderId}` — Buscar pedido por ID
- `DELETE /store/order/{orderId}` — Deletar pedido

**User**
- `POST /user` — Criar usuário
- `POST /user/createWithArray` — Criar usuários com array
- `POST /user/createWithList` — Criar usuários com lista
- `GET /user/login` — Login
- `GET /user/{username}` — Buscar usuário por username
- `PUT /user/{username}` — Atualizar usuário
- `GET /user/logout` — Logout
- `DELETE /user/{username}` — Deletar usuário

### ▶️ Como executar localmente

**1. Instale o Node.js:** [nodejs.org](https://nodejs.org)

**2. Instale o Newman:**
```bash
npm install -g newman newman-reporter-htmlextra
```

**3. Execute os testes:**
```bash
newman run petstore-collection.json \
  --environment petstore-environment.json \
  --reporters cli,htmlextra \
  --reporter-htmlextra-export report.html
```

---

## 🌐 Automação Web — SauceDemo

**URL:** `https://www.saucedemo.com`

### Fluxo E2E testado

1. ✅ Login com usuário válido
2. ✅ Adicionar produto ao carrinho
3. ✅ Finalizar compra (checkout completo)

### Design Pattern utilizado

O projeto utiliza o padrão **Page Object Model (POM)** — cada página da aplicação é representada por uma classe Python, separando a lógica de navegação dos testes.

### ▶️ Como executar localmente

**1. Crie o arquivo `.env` dentro de `web-tests/`:**
```
LOGIN_USER=standard_user
LOGIN_PASSWORD=secret_sauce
```

**2. Instale as dependências:**
```bash
cd web-tests
pip install -r requirements.txt
```

**3. Execute os testes:**
```bash
pytest
```

---

## ⚙️ CI/CD — GitHub Actions

O projeto está integrado ao **GitHub Actions**. A pipeline roda automaticamente a cada `push` ou `Pull Request` na branch `main`.

### Jobs executados

| Job | Descrição |
|---|---|
| `run-api-tests` | Roda os testes de API com Newman |
| `run-web-tests` | Roda os testes Web com Selenium |

### Branch Protection

A branch `main` está protegida — nenhum código pode ser mergeado sem que todos os testes passem no CI.

### 📊 Relatórios de Execução

Os relatórios detalhados de cada execução estão disponíveis na aba **Actions** do GitHub, na seção **Artifacts** de cada run. O relatório da API é gerado em formato HTML pelo `newman-reporter-htmlextra`, contendo detalhes de cada requisição, asserção e tempo de resposta.

---

## 👨‍💻 Autor

**Gustavo** — Disciplina de Testes — ICEV 2026