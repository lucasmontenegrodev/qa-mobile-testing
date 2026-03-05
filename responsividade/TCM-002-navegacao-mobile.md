# TCM-002 — Navegação Mobile (Samsung Galaxy S21)

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