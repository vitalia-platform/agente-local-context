<!-- DASHBOARD.md | Atualizado em: 19-08-2026 15:07:30(GMT-04:00) -->

# Dashboard de Contexto: .vitalia

## Semáforo de Sincronização

- **Status:** LIVRE
- **Máquina:** N/A
- **Expira em:** N/A

## Shards Ativos

| Máquina | Tarefa Atual | Etapas | Status | Último Sync | Próximo Passo (P0) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **andrenote** (7f367bd3) | Feature 006: grounding-guard-rails + correção de regressões em workflows | - Retomada da correção do kit
 | Concluído | 19-08-2026 15:06:35(GMT-04:00) | Publicar repositórios no GitHub usando publicar-repos.md |

## Arquitetura de Contexto

```mermaid
graph TD
  Raiz["Repositório Raiz (.vitalia)"]
  7f367bd3["Shard: andrenote"] --> Raiz
```

## Guard Rails de Grounding

| Arquivo | Status | Pendentes |
| :--- | :--- | :--- |
| `grounding-domains.yaml` (global) | ✅ Ativo | — |
| [grounding-domains-local.yaml](./grounding-domains-local.yaml) (projeto) | ✅ Presente — 19-08-2026 11:07 | ✅ 0 pendentes |
