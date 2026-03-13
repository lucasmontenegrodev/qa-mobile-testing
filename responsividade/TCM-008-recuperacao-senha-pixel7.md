# TCM-008 - Fluxo de Recuperacao de Senha Mobile (Pixel 7)

| Campo | Valor |
|---|---|
| ID | TCM-008 |
| Tipo | Responsividade |
| Funcionalidade | Recuperacao de Senha |
| User Story | SHOP-402 |
| Sprint | Sprint 12 |
| Dispositivo | Google Pixel 7 - 412 x 915px |
| Ferramenta | Chrome DevTools |
| Prioridade | Media |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data | 12/03/2026 |
| Status | PASS (5/5) |

---

## Como configurar

1. Abrir Chrome, F12, Toggle Device Toolbar
2. Selecionar Pixel 7 ou definir 412 x 915px manualmente
3. Acessar a pagina de login e clicar em "Esqueci minha senha"

---

## Pre-condicoes

- Chrome DevTools com emulacao Pixel 7 (412x915px)
- Usuario de teste com e-mail cadastrado no Staging

---

## Casos de Teste

| # | Elemento | Criterio | Resultado Real | Status |
|---|---|---|---|---|
| 1 | Tela de recuperacao de senha | Campo de e-mail e botao visiveis, layout sem overflow | Layout correto | PASS |
| 2 | Campo de e-mail | Largura 100%, teclado email ao focar, placeholder visivel | Comportamento correto | PASS |
| 3 | Botao "Enviar link de recuperacao" | Largura adequada, texto legivel, nao cortado | Botao correto | PASS |
| 4 | Mensagem de confirmacao de envio | Exibida na mesma tela sem quebrar layout, texto legivel | Mensagem exibida corretamente | PASS |
| 5 | Link "Voltar ao login" | Visivel abaixo da mensagem de confirmacao, clicavel | Link acessivel e funcional | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 5 | 0 | 100% |

---

## Observacoes

Fluxo de recuperacao de senha aprovado para Pixel 7 (412px). Layout adaptado corretamente em todas as etapas do fluxo. Nenhum bug encontrado.