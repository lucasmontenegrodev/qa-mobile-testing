# TCM-005 — API REST: Endpoint de Listagem de Produtos

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