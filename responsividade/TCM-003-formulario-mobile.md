# TCM-003 — Formulário de Cadastro em Tablet (iPad Pro)

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