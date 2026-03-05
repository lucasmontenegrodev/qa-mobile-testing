# BUG-301 — Endpoint de produtos ignora parâmetros de paginação

**Status:** 🔴 ABERTO | **Severidade:** Alta | **Sprint:** 10

---

## 📋 Informações Gerais

| Campo | Valor |
|---|---|
| **ID** | BUG-301 |
| **Test Case relacionado** | [TCM-005](../TCM-005-api-produtos.md) |
| **Endpoint afetado** | `GET /api/products` |
| **Sprint** | Sprint 10 |
| **Data de abertura** | 07/03/2026 |
| **Reportado por** | Lucas Montenegro — QA |
| **Severidade** | 🔴 Alta |
| **Prioridade** | 🔴 Alta |
| **Ferramenta** | Postman |
| **Ambiente** | Staging v2.14.0 |

---

## 📝 Descrição

O endpoint `GET /api/products` ignora os query parameters `page` e `limit` quando enviados na requisição. Em vez de retornar o número de itens solicitado por página, o endpoint retorna **todos os produtos cadastrados** em um único response, sem estrutura de paginação.

---

## 🔁 Passos para Reproduzir

1. Abrir Postman com environment de Staging configurado
2. Autenticar e obter token válido
3. Enviar request:
```
GET {{base_url}}/api/products?page=1&limit=10
Authorization: Bearer {{token}}
```
4. Observar o response recebido

---

## ✅ Resultado Esperado

```json
{
  "data": [ /* 10 produtos */ ],
  "total": 47,
  "page": 1,
  "limit": 10,
  "total_pages": 5
}
```

## ❌ Resultado Obtido

```json
[
  { "id": 1, "name": "...", "price": ... },
  { "id": 2, "name": "...", "price": ... },
  /* ... todos os 47 produtos retornados */
]
```

> Sem campo `total`, `page`, `limit` ou `total_pages`. Parâmetros da query completamente ignorados.

---

## 🎥 Evidências

```
evidencias/TCM-005/
├── 01-request-com-paginacao.png        # request enviado com page=1&limit=10
├── 02-response-sem-paginacao.png       # response com todos os 47 registros
└── 03-postman-collection-export.json   # collection exportada do Postman
```

---

## 💥 Impacto

- Em produção com volume alto de produtos, retornar tudo de uma vez pode causar **timeout** e **lentidão severa** no app mobile
- Clientes mobile em redes lentas (3G/4G) receberão payloads enormes desnecessariamente
- Front-end mobile que depende de paginação para scroll infinito ficará quebrado

---

## 💡 Hipótese para o Desenvolvedor

O controller do endpoint provavelmente não está lendo os query params `page` e `limit` da requisição. Verificar se a lógica de paginação foi implementada no service ou se os params estão sendo ignorados antes de chegar à query do banco.

---

## 🔄 Histórico

| Data | Ação | Responsável |
|---|---|---|
| 07/03/2026 | Bug aberto após falha no cenário 5 do TCM-005 | Lucas Montenegro — QA |
| — | Aguardando triagem | — |