# TCM-001 — Layout do Checkout em Mobile (iPhone 14)

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