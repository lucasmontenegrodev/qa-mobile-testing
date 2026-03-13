import os

TCM006 = """# TCM-006 - Login Mobile (Samsung Galaxy A54)

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
"""

TCM007 = """# TCM-007 - Login Mobile (iPhone SE 3a geracao)

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
"""

TCM008 = """# TCM-008 - Fluxo de Recuperacao de Senha Mobile (Pixel 7)

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
"""

arquivos = {
    "responsividade/TCM-006-login-galaxy-a54.md": TCM006,
    "responsividade/TCM-007-login-iphone-se.md":  TCM007,
    "responsividade/TCM-008-recuperacao-senha-pixel7.md": TCM008,
}

print("Adicionando TCM-006, TCM-007 e TCM-008 ao qa-mobile-testing...")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  OK: {caminho}")

print("\nPronto. 3 arquivos criados.")
print("\nLembre de atualizar o README.md do repositorio com os novos TCs.")
print("\nProximos passos:")
print("  git add .")
print('  git commit -m "feat: adiciona TCM-006, TCM-007 e TCM-008 login mobile"')
print("  git push")
