# TCM-006 - Login Mobile (Samsung Galaxy A54)

| Campo | Valor |
|---|---|
| ID | TCM-006 |
| Tipo | Responsividade |
| Funcionalidade | Login e Autenticacao |
| User Story | SHOP-401 |
| Sprint | Sprint 12 |
| Dispositivo | Samsung Galaxy A54 - 393 x 851px |
| Ferramenta | Chrome DevTools |
| Prioridade | Alta |
| Ambiente | Staging |
| QA Responsavel | Lucas Montenegro |
| Data | 12/03/2026 |
| Status | FAIL (5/6 - 1 falhou) |

---

## Como configurar

1. Abrir Chrome, F12, Toggle Device Toolbar
2. Selecionar Samsung Galaxy A54 ou definir 393 x 851px manualmente
3. Acessar a pagina de login no Staging

---

## Pre-condicoes

- Chrome DevTools com emulacao Galaxy A54 (393x851px)
- Usuario de teste cadastrado e ativo

---

## Casos de Teste

| # | Elemento | Criterio | Resultado Real | Status |
|---|---|---|---|---|
| 1 | Layout geral da tela de login | Campos, botao e logo visiveis sem scroll horizontal | Layout correto, sem overflow | PASS |
| 2 | Campo de e-mail | Largura 100%, teclado tipo email ativado ao focar | Teclado email ativado corretamente | PASS |
| 3 | Campo de senha | Largura 100%, icone de exibir senha visivel e funcional | Icone funcional | PASS |
| 4 | Botao Entrar | Largura minima 44px, texto legivel, sem sobreposicao | Botao correto | PASS |
| 5 | Mensagem de erro (senha incorreta) | Mensagem exibida abaixo do campo sem quebrar layout | Mensagem empurra o botao para fora da tela em 393px | FAIL |
| 6 | Link "Esqueci minha senha" | Visivel, clicavel, tamanho de toque adequado | Link correto | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 6 | 5 | 1 | 83% |

---

## Bug Report

### BUG-341 - Mensagem de erro no login empurra botao para fora da area visivel em mobile

| Campo | Valor |
|---|---|
| ID | BUG-341 |
| Dispositivo | Samsung Galaxy A54 - 393x851px |
| Ambiente | Staging v2.15.0 |
| Severidade | Media |
| Prioridade | Alta |
| Status | Aberto |

Passos para reproduzir:
1. Emular Galaxy A54 (393px) no Chrome DevTools
2. Acessar a tela de login
3. Digitar senha incorreta e tentar logar
4. Observar o posicionamento do botao "Entrar" apos a mensagem de erro aparecer

Resultado Esperado:
Mensagem de erro exibida inline abaixo do campo de senha, botao "Entrar" permanece visivel

Resultado Obtido:
Mensagem de erro com altura fixa empurra o botao "Entrar" parcialmente para fora da area visivel, exigindo scroll para acessar

Evidencias:
```
evidencias/TCM-006/
├── 01-login-layout-geral.png
├── 02-mensagem-erro-botao-deslocado.png
└── 03-scroll-necessario-para-botao.png
```

Hipotese: Mensagem de erro com height fixo no CSS. Solucao: usar height dinamico ou posicionar a mensagem de forma que nao desloque os elementos abaixo.