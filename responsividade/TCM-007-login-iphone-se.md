# TCM-007 - Login Mobile (iPhone SE 3a geracao)

| Campo | Valor |
|---|---|
| ID | TCM-007 |
| Tipo | Responsividade |
| Funcionalidade | Login e Autenticacao |
| User Story | SHOP-401 |
| Sprint | Sprint 12 |
| Dispositivo | iPhone SE 3a geracao - 375 x 667px |
| Ferramenta | Chrome DevTools |
| Prioridade | Alta |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data | 12/03/2026 |
| Status | PASS (6/6) |

---

## Como configurar

1. Abrir Chrome, F12, Toggle Device Toolbar
2. Selecionar iPhone SE ou definir 375 x 667px manualmente
3. Acessar a pagina de login no Staging

---

## Pre-condicoes

- Chrome DevTools com emulacao iPhone SE (375x667px)
- Usuario de teste cadastrado e ativo

---

## Casos de Teste

| # | Elemento | Criterio | Resultado Real | Status |
|---|---|---|---|---|
| 1 | Layout geral | Todos os elementos visiveis na tela menor (667px de altura) sem scroll | Layout adaptado corretamente | PASS |
| 2 | Campo de e-mail | Largura 100%, teclado email ao focar | Comportamento correto | PASS |
| 3 | Campo de senha | Icone de exibir/ocultar senha visivel e funcional | Icone funcional | PASS |
| 4 | Botao Entrar | Visivel sem scroll, toque responsivo | Botao acessivel | PASS |
| 5 | Mensagem de erro | Exibida sem deslocar outros elementos | Mensagem posicionada corretamente | PASS |
| 6 | Link "Esqueci minha senha" | Visivel abaixo do botao, tamanho de toque adequado | Link acessivel | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 6 | 6 | 0 | 100% |

---

## Observacoes

Login aprovado para iPhone SE (375px). Todos os elementos respeitaram o espaco reduzido da tela de 667px de altura. Nenhum bug encontrado.