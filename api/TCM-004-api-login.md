# TCM-004 — API REST: Endpoint de Login

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