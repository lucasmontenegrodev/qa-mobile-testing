# 📱 QA Mobile Testing — Responsividade & API

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