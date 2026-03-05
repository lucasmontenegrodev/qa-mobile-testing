import os

README = """# 📱 QA Mobile Testing — Responsividade & API

> Portfólio de testes mobile manuais cobrindo responsividade em múltiplos dispositivos e testes de API REST. Ferramentas utilizadas: Chrome DevTools (emulação mobile) e Postman.

---

## 📁 Estrutura do Repositório

```
qa-mobile-testing/
│
├── README.md
│
├── responsividade/
│   ├── TCM-001-layout-mobile-checkout.md
│   ├── TCM-002-navegacao-mobile.md
│   └── TCM-003-formulario-mobile.md
│
├── api/
│   ├── TCM-004-api-login.md
│   ├── TCM-005-api-produtos.md
│   └── bug-report/
│       └── BUG-301-api-produtos-sem-paginacao.md
│
└── evidencias/
    └── README.md
```

---

## 🔁 Fluxo de Teste Utilizado

```
User Story (Jira)
      ↓
  Escrita do Test Case Mobile
      ↓
  Execução: Chrome DevTools (responsividade) / Postman (API)
      ↓
  Resultado: PASS ou FAIL
      ↓
  [se FAIL] Bug Report aberto e linkado
```

---

## 📋 Índice de Testes

| ID | Tipo | Funcionalidade | Dispositivo / Ferramenta | Status | Bug |
|---|---|---|---|---|---|
| [TCM-001](./responsividade/TCM-001-layout-mobile-checkout.md) | Responsividade | Layout do Checkout | iPhone 14 / Chrome DevTools | ❌ FAIL | [BUG-298](./responsividade/TCM-001-layout-mobile-checkout.md#bug-298) |
| [TCM-002](./responsividade/TCM-002-navegacao-mobile.md) | Responsividade | Navegação mobile | Galaxy S21 / Chrome DevTools | ✅ PASS | — |
| [TCM-003](./responsividade/TCM-003-formulario-mobile.md) | Responsividade | Formulário de cadastro | iPad Pro / Chrome DevTools | ✅ PASS | — |
| [TCM-004](./api/TCM-004-api-login.md) | API REST | Endpoint de Login | Postman | ✅ PASS | — |
| [TCM-005](./api/TCM-005-api-produtos.md) | API REST | Endpoint de Produtos | Postman | ❌ FAIL | [BUG-301](./api/bug-report/BUG-301-api-produtos-sem-paginacao.md) |

---

## 📊 Resumo Geral

| Total de TCs | ✅ PASS | ❌ FAIL | Bugs Abertos |
|---|---|---|---|
| 5 | 3 | 2 | 2 |

---

## 🛠️ Ferramentas Utilizadas

| Ferramenta | Uso |
|---|---|
| **Chrome DevTools** | Emulação de dispositivos mobile (responsividade, layout, zoom) |
| **Postman** | Execução e validação de requisições REST (GET, POST, status codes, body) |
| **Jira** | Gestão de Test Cases e Bug Reports no Sprint Board |

---

## 📌 Dispositivos Testados

| Dispositivo | Resolução | Sistema |
|---|---|---|
| iPhone 14 | 390 x 844px | iOS (simulado) |
| Samsung Galaxy S21 | 360 x 800px | Android (simulado) |
| iPad Pro | 1024 x 1366px | iPadOS (simulado) |
"""

TCM001 = """# TCM-001 — Layout do Checkout em Mobile (iPhone 14)

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TCM-001 |
| **Tipo** | Teste de Responsividade |
| **User Story relacionada** | SHOP-185 |
| **Sprint** | Sprint 9 |
| **Dispositivo simulado** | iPhone 14 — 390 x 844px |
| **Ferramenta** | Chrome DevTools (Device Emulation) |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 06/03/2026 |
| **Status final** | ❌ FAIL (5/6 passos OK — 1 falhou) |

---

## 🎯 Objetivo

Verificar se a página de Checkout se adapta corretamente à resolução mobile de 390px, mantendo usabilidade e legibilidade sem scroll horizontal.

---

## 🔧 Como configurar o ambiente

1. Abrir Chrome → F12 (DevTools)
2. Clicar no ícone de dispositivo (Toggle Device Toolbar)
3. Selecionar **iPhone 14** no seletor de dispositivos
4. Resolução deve mostrar **390 x 844**
5. Acessar o ambiente de Staging

---

## ✅ Pré-condições

- [ ] Chrome DevTools aberto com emulação iPhone 14 (390x844px)
- [ ] Usuário logado com produto no carrinho

---

## 🔢 Passos e Resultados

| # | Elemento Testado | Critério | Resultado Real | Status |
|---|---|---|---|---|
| 1 | Header / Menu hamburguer | Visível, funcional, sem sobreposição | Exibido corretamente | ✅ PASS |
| 2 | Lista de itens do carrinho | Itens empilhados verticalmente, imagem e texto legíveis | Layout correto | ✅ PASS |
| 3 | Campos de endereço | Inputs ocupam 100% da largura, labels visíveis, teclado não quebra layout | Campos responsivos | ✅ PASS |
| 4 | Botões de ação (Continuar / Cancelar) | Largura mínima de 44px, texto legível, sem sobreposição | Botões corretos | ✅ PASS |
| 5 | Tabela de resumo do pedido | Adaptada à largura de 390px, sem scroll horizontal | **Tabela ultrapassa 390px — scroll horizontal indesejado** | ❌ FAIL |
| 6 | Botão "Finalizar Compra" | Visível sem precisar rolar horizontalmente, toque responsivo | Botão correto | ✅ PASS |

---

## 📊 Resumo da Execução

| Total | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 6 | 5 | 1 | 83% |

---

## 🐛 Bug Gerado {#bug-298}

### BUG-298 — Tabela de resumo do pedido causa scroll horizontal no checkout mobile

**Status:** 🔴 ABERTO | **Severidade:** Média | **Prioridade:** Alta

| Campo | Valor |
|---|---|
| **ID** | BUG-298 |
| **Dispositivo** | iPhone 14 — 390x844px (Chrome DevTools) |
| **Ambiente** | Staging v2.14.0 |
| **Data** | 06/03/2026 |

**Passos para reproduzir:**
1. Abrir Chrome DevTools → emular iPhone 14 (390px)
2. Logar e adicionar produto ao carrinho
3. Acessar o Checkout
4. Observar a tabela de resumo do pedido

**Resultado Esperado:**
```
Tabela adaptada a 390px — sem scroll horizontal
```

**Resultado Obtido:**
```
Tabela com largura fixa ultrapassa 390px
Scroll horizontal aparece na página
Parte do conteúdo fica oculto
```

**Evidências:**
```
evidencias/TCM-001/
├── 01-checkout-mobile-geral.png       # tela geral OK
├── 02-tabela-scroll-horizontal.png    # tabela ultrapassando a tela
└── 03-conteudo-cortado.png            # conteúdo parcialmente oculto
```

**Hipótese:** Tabela com `width` fixo em px no CSS. Solução: `width: 100%` + `overflow-x: auto` no container.
"""

TCM002 = """# TCM-002 — Navegação Mobile (Samsung Galaxy S21)

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TCM-002 |
| **Tipo** | Teste de Responsividade |
| **User Story relacionada** | SHOP-186 |
| **Sprint** | Sprint 9 |
| **Dispositivo simulado** | Samsung Galaxy S21 — 360 x 800px |
| **Ferramenta** | Chrome DevTools (Device Emulation) |
| **Prioridade** | 🟡 Média |
| **Ambiente** | Staging |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 06/03/2026 |
| **Status final** | ✅ PASS (6/6) |

---

## 🎯 Objetivo

Verificar se a navegação principal (menu, links, breadcrumbs) funciona corretamente em dispositivo Android de resolução 360px.

---

## 🔧 Como configurar o ambiente

1. Abrir Chrome → F12 → Toggle Device Toolbar
2. Selecionar **Samsung Galaxy S21** ou definir manualmente: **360 x 800px**
3. Acessar o ambiente de Staging

---

## ✅ Pré-condições

- [ ] Chrome DevTools com emulação Galaxy S21 (360x800px)
- [ ] Usuário logado

---

## 🔢 Passos e Resultados

| # | Elemento Testado | Critério | Resultado Real | Status |
|---|---|---|---|---|
| 1 | Menu hamburguer | Ícone visível no header, abre ao toque, exibe todos os links | Funcionou corretamente | ✅ PASS |
| 2 | Logo / Home | Clicável, redireciona para a página inicial | Redirecionamento correto | ✅ PASS |
| 3 | Barra de busca | Expansível ao toque, campo ocupa largura da tela, teclado não quebra layout | Comportamento correto | ✅ PASS |
| 4 | Links de categoria | Visíveis no menu mobile, tamanho de toque adequado (mínimo 44px) | Links acessíveis | ✅ PASS |
| 5 | Breadcrumb de navegação | Exibido acima do conteúdo, truncado com "..." quando muito longo | Truncado corretamente | ✅ PASS |
| 6 | Footer mobile | Links visíveis, empilhados verticalmente, sem sobreposição | Footer responsivo | ✅ PASS |

---

## 📊 Resumo da Execução

| Total | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 6 | 6 | 0 | 100% |

---

## 📝 Observações

Navegação mobile aprovada para resolução Android de 360px. Todos os elementos de navegação respeitaram o tamanho mínimo de toque de 44px recomendado pelo WCAG. Nenhum bug encontrado.
"""

TCM003 = """# TCM-003 — Formulário de Cadastro em Tablet (iPad Pro)

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TCM-003 |
| **Tipo** | Teste de Responsividade |
| **User Story relacionada** | SHOP-110 |
| **Sprint** | Sprint 9 |
| **Dispositivo simulado** | iPad Pro — 1024 x 1366px |
| **Ferramenta** | Chrome DevTools (Device Emulation) |
| **Prioridade** | 🟡 Média |
| **Ambiente** | Staging |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 06/03/2026 |
| **Status final** | ✅ PASS (5/5) |

---

## 🎯 Objetivo

Verificar se o formulário de cadastro se adapta corretamente à resolução tablet de 1024px, aproveitando o espaço disponível sem distorções.

---

## 🔧 Como configurar o ambiente

1. Abrir Chrome → F12 → Toggle Device Toolbar
2. Selecionar **iPad Pro** ou definir manualmente: **1024 x 1366px**
3. Acessar a página de cadastro no Staging

---

## ✅ Pré-condições

- [ ] Chrome DevTools com emulação iPad Pro (1024x1366px)
- [ ] Sem sessão ativa

---

## 🔢 Passos e Resultados

| # | Elemento Testado | Critério | Resultado Real | Status |
|---|---|---|---|---|
| 1 | Layout geral do formulário | Centralizado, largura máxima adequada (não ocupa 100% em tablet) | Layout bem proporcionado | ✅ PASS |
| 2 | Campos de input | Largura adequada para tablet, labels alinhadas, espaçamento confortável | Campos corretos | ✅ PASS |
| 3 | Botão "Cadastrar" | Largura proporcional, não esticado em 100% da tela como no mobile | Botão bem proporcional | ✅ PASS |
| 4 | Mensagens de erro | Aparecem abaixo do campo correspondente, sem sobreposição | Erros bem posicionados | ✅ PASS |
| 5 | Teclado virtual (simulado) | Layout não quebra ao simular abertura do teclado no DevTools | Layout estável | ✅ PASS |

---

## 📊 Resumo da Execução

| Total | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 5 | 5 | 0 | 100% |

---

## 📝 Observações

Formulário de cadastro aprovado para resolução tablet. O layout aproveitou bem o espaço extra disponível em 1024px sem distorcer os elementos. Nenhum bug encontrado.
"""

TCM004 = """# TCM-004 — API REST: Endpoint de Login

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TCM-004 |
| **Tipo** | Teste de API REST |
| **Endpoint** | `POST /api/auth/login` |
| **Ferramenta** | Postman |
| **Sprint** | Sprint 10 |
| **Prioridade** | 🔴 Alta |
| **Ambiente** | Staging — `https://staging.shopdemo.com` |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 07/03/2026 |
| **Status final** | ✅ PASS (5/5) |

---

## 🎯 Objetivo

Validar o endpoint de autenticação, verificando status codes, estrutura do response body e comportamento com dados inválidos.

---

## ✅ Pré-condições

- [ ] Postman instalado e configurado
- [ ] Environment de Staging configurado no Postman com variável `{{base_url}}`
- [ ] Usuário de teste cadastrado: `qa_teste@email.com` / `Teste@123`

---

## 🔢 Cenários e Resultados

### Cenário 1 — Login com credenciais válidas

**Request:**
```
Method:  POST
URL:     {{base_url}}/api/auth/login
Headers: Content-Type: application/json

Body:
{
  "email": "qa_teste@email.com",
  "password": "Teste@123"
}
```

**Resultado Esperado:**
```
Status: 200 OK
Body:
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR...",
  "user": {
    "id": 42,
    "email": "qa_teste@email.com",
    "name": "Teste QA"
  }
}
```

**Resultado Real:** `200 OK` — Body com token e dados do usuário conforme esperado | ✅ PASS

---

### Cenário 2 — Login com senha incorreta

**Request:** mesmo endpoint, `"password": "senhaerrada"`

**Resultado Esperado:** `401 Unauthorized` — `{"success": false, "message": "Credenciais inválidas"}`

**Resultado Real:** `401 Unauthorized` — Body correto | ✅ PASS

---

### Cenário 3 — Login com e-mail não cadastrado

**Request:** `"email": "naoexiste@email.com"`

**Resultado Esperado:** `404 Not Found` — `{"success": false, "message": "Usuário não encontrado"}`

**Resultado Real:** `404 Not Found` — Body correto | ✅ PASS

---

### Cenário 4 — Body vazio (sem campos)

**Request:** Body `{}`

**Resultado Esperado:** `400 Bad Request` — `{"success": false, "message": "Campos obrigatórios ausentes"}`

**Resultado Real:** `400 Bad Request` — Body correto | ✅ PASS

---

### Cenário 5 — Token retornado é válido para requests autenticados

Usando o token do Cenário 1 em um endpoint protegido (`GET /api/user/profile`):

**Resultado Esperado:** `200 OK` com dados do perfil

**Resultado Real:** `200 OK` — Token aceito e dados retornados corretamente | ✅ PASS

---

## 📊 Resumo da Execução

| Total | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 5 | 5 | 0 | 100% |

---

## 📝 Observações

Todos os cenários do endpoint de login responderam com os status codes corretos e bodies esperados. O token JWT gerado foi validado com sucesso em requisição autenticada subsequente.
"""

TCM005 = """# TCM-005 — API REST: Endpoint de Listagem de Produtos

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | TCM-005 |
| **Tipo** | Teste de API REST |
| **Endpoint** | `GET /api/products` |
| **Ferramenta** | Postman |
| **Sprint** | Sprint 10 |
| **Prioridade** | 🟡 Média |
| **Ambiente** | Staging — `https://staging.shopdemo.com` |
| **QA Responsável** | Lucas Montenegro |
| **Data de execução** | 07/03/2026 |
| **Status final** | ❌ FAIL (4/5 cenários OK — 1 falhou) |

---

## 🎯 Objetivo

Validar o endpoint de listagem de produtos, verificando status code, estrutura do response, filtros por query params e paginação.

---

## ✅ Pré-condições

- [ ] Postman com environment de Staging configurado
- [ ] Token de autenticação válido na variável `{{token}}`
- [ ] Pelo menos 20 produtos cadastrados no banco de Staging

---

## 🔢 Cenários e Resultados

### Cenário 1 — Listagem geral de produtos

**Request:**
```
Method:  GET
URL:     {{base_url}}/api/products
Headers: Authorization: Bearer {{token}}
```

**Resultado Esperado:** `200 OK` — Array de produtos com id, name, price, category, image_url

**Resultado Real:** `200 OK` — Estrutura correta com todos os campos | ✅ PASS

---

### Cenário 2 — Filtro por categoria via query param

**Request:** `GET /api/products?category=tenis`

**Resultado Esperado:** `200 OK` — Apenas produtos da categoria "tenis"

**Resultado Real:** `200 OK` — Somente tênis retornados | ✅ PASS

---

### Cenário 3 — Filtro por faixa de preço

**Request:** `GET /api/products?min_price=50&max_price=200`

**Resultado Esperado:** `200 OK` — Apenas produtos entre R$50 e R$200

**Resultado Real:** `200 OK` — Todos os preços dentro da faixa | ✅ PASS

---

### Cenário 4 — Categoria inexistente

**Request:** `GET /api/products?category=categoria_inexistente`

**Resultado Esperado:** `200 OK` — Array vazio `[]`

**Resultado Real:** `200 OK` — `[]` retornado corretamente | ✅ PASS

---

### Cenário 5 — Paginação dos resultados

**Request:** `GET /api/products?page=1&limit=10`

**Resultado Esperado:**
```json
{
  "data": [...],        // 10 produtos
  "total": 47,          // total de produtos
  "page": 1,
  "limit": 10,
  "total_pages": 5
}
```

**Resultado Real:**
```json
[...] // retornou TODOS os 47 produtos sem paginar
```
Status `200 OK` mas sem estrutura de paginação | ❌ FAIL

---

## 📊 Resumo da Execução

| Total | PASS | FAIL | % Aprovação |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## 🐛 Bug Gerado

Cenário 5 falhou → Bug Report: [BUG-301](./bug-report/BUG-301-api-produtos-sem-paginacao.md)

---

## 📝 Observações

Filtros funcionam corretamente de forma individual. O problema está na paginação — o endpoint ignora os parâmetros `page` e `limit`, retornando todos os registros de uma vez. Isso pode causar lentidão severa em produção com grande volume de dados.
"""

BUG301 = """# BUG-301 — Endpoint de produtos ignora parâmetros de paginação

**Status:** 🔴 ABERTO | **Severidade:** Alta | **Sprint:** 10

---

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | BUG-301 |
| **Test Case relacionado** | [TCM-005](../TCM-005-api-produtos.md) |
| **Endpoint afetado** | `GET /api/products` |
| **Sprint** | Sprint 10 |
| **Data de abertura** | 07/03/2026 |
| **Reportado por** | Lucas Montenegro — QA |
| **Severidade** | 🔴 Alta |
| **Prioridade** | 🔴 Alta |
| **Ferramenta** | Postman |
| **Ambiente** | Staging v2.14.0 |

---

## 📝 Descrição

O endpoint `GET /api/products` ignora os query parameters `page` e `limit` quando enviados na requisição. Em vez de retornar o número de itens solicitado por página, o endpoint retorna **todos os produtos cadastrados** em um único response, sem estrutura de paginação.

---

## 🔁 Passos para Reproduzir

1. Abrir Postman com environment de Staging configurado
2. Autenticar e obter token válido
3. Enviar request:
```
GET {{base_url}}/api/products?page=1&limit=10
Authorization: Bearer {{token}}
```
4. Observar o response recebido

---

## ✅ Resultado Esperado

```json
{
  "data": [ /* 10 produtos */ ],
  "total": 47,
  "page": 1,
  "limit": 10,
  "total_pages": 5
}
```

## ❌ Resultado Obtido

```json
[
  { "id": 1, "name": "...", "price": ... },
  { "id": 2, "name": "...", "price": ... },
  /* ... todos os 47 produtos retornados */
]
```

> Sem campo `total`, `page`, `limit` ou `total_pages`. Parâmetros da query completamente ignorados.

---

## 🎥 Evidências

```
evidencias/TCM-005/
├── 01-request-com-paginacao.png        # request enviado com page=1&limit=10
├── 02-response-sem-paginacao.png       # response com todos os 47 registros
└── 03-postman-collection-export.json   # collection exportada do Postman
```

---

## 💥 Impacto

- Em produção com volume alto de produtos, retornar tudo de uma vez pode causar **timeout** e **lentidão severa** no app mobile
- Clientes mobile em redes lentas (3G/4G) receberão payloads enormes desnecessariamente
- Front-end mobile que depende de paginação para scroll infinito ficará quebrado

---

## 💡 Hipótese para o Desenvolvedor

O controller do endpoint provavelmente não está lendo os query params `page` e `limit` da requisição. Verificar se a lógica de paginação foi implementada no service ou se os params estão sendo ignorados antes de chegar à query do banco.

---

## 🔄 Histórico

| Data | Ação | Responsável |
|---|---|---|
| 07/03/2026 | Bug aberto após falha no cenário 5 do TCM-005 | Lucas Montenegro — QA |
| — | Aguardando triagem | — |
"""

EVIDENCIAS = """# 📁 Evidências

Organizado por Test Case. Cada pasta contém screenshots do Postman ou Chrome DevTools.

## Estrutura

```
evidencias/
├── TCM-001/        # screenshots do checkout mobile (iPhone 14)
├── TCM-002/        # screenshots da navegação (Galaxy S21)
├── TCM-003/        # screenshots do formulário (iPad Pro)
├── TCM-004/        # screenshots das requisições de login no Postman
└── TCM-005/        # screenshots das requisições de produtos + paginação
```

## Boas práticas

- Para API: exporte a Collection do Postman (`.json`) e salve aqui
- Para responsividade: use F12 → Print Screen com o dispositivo visível
- Nomeie com número sequencial: `01-descricao.png`
"""

# ── criação dos arquivos ─────────────────────────────────────────────────────

arquivos = {
    "README.md":                                            README,
    "responsividade/TCM-001-layout-mobile-checkout.md":    TCM001,
    "responsividade/TCM-002-navegacao-mobile.md":          TCM002,
    "responsividade/TCM-003-formulario-mobile.md":         TCM003,
    "api/TCM-004-api-login.md":                            TCM004,
    "api/TCM-005-api-produtos.md":                         TCM005,
    "api/bug-report/BUG-301-api-produtos-sem-paginacao.md": BUG301,
    "evidencias/README.md":                                EVIDENCIAS,
}

print("\n🚀 Criando estrutura do repositório qa-mobile-testing...\n")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  ✅ {caminho}")

print("\n✨ Pronto! Estrutura criada com sucesso.")
print("\nPróximos passos:\n")
print("  1. Crie o repositório 'qa-mobile-testing' no GitHub")
print("  2. git clone https://github.com/lucasmontenegrodev/qa-mobile-testing.git")
print("  3. cd qa-mobile-testing")
print("  4. Coloque este script dentro da pasta e rode: python setup_mobile.py")
print("  5. git add .")
print('  6. git commit -m "feat: estrutura completa de testes mobile"')
print("  7. git push\n")
