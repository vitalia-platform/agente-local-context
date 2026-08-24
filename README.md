<!-- README.md | Atualizado em: 24-08-2026 12:04:25(GMT-04:00) -->

# Dashboard de Contexto: .vitalia

## Semáforo de Sincronização

- **Status:** LIVRE | **Data:** 24-08-2026 12:04:25(GMT-04:00)
- **Máquina:** N/A
- **Expira em:** N/A

## Shards Ativos

| Máquina | Tarefa Atual | Etapas | Status | Último Sync | Próximo Passo (P0) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **andrenote** (7f367bd3) | Brainstorming e PRD Técnico da Feature 008 (Controle de Contexto & UX/UI) | ['Auditoria de Git e Repositórios da Tríade de Projetos', 'Briefing Canônico de Arquitetura (docs/BRIEFING_ARQUITETURA_CONTROLE_CONTEXTO.md)', 'Mockup Visual temp.md (Shields.io, Mermaid centralizado M_ e tabelas HTML)', 'PRD Técnico com Matriz Diferencial Modo Integrado vs Standalone (docs/PRD_CONTROLE_CONTEXTO_VITALIA.md)', 'Assentamento da Regra Geral Vitalia de Strict Fallback em learnings.jsonl'] | Concluído | 24-08-2026 12:02:30(GMT-04:00) | Iniciar o ciclo SDD da Feature 008 acionando /vitalia-spec-specify para gerar spec.md e plan.md com base no PRD |
| **andre-desktop** (f23704e7) | Correção do Workflow de Brainstorming — Vitalia Kit | - Varredura completa do kit antigo (vitalia-agent-kit-main) e kit atual
- Pesquisa de indústria: Policy Evaluation Layer, PEV cycle, Task Verification
- Criado: ~/.vitalia/kit/config/dynamic-questioning.yaml (9 domínios, P0 saúde/privacidade)
- Criado: ~/.vitalia/kit/scripts/hooks/scan_environment.py (scan passivo agnóstico)
- Atualizado: brainstorming.toml v0.4.0 → v0.5.0 (hook before, STOP/SCAN/ASK/WAIT, Sub-Agente Pesquisador)
- Emendado: architect-constitution.md — Artigo I agora reflete ciclo PEV de 6 etapas
 | Concluído | ⚠️ 19-08-2026 20:17:00(GMT-04:00) | Analisar e incorporar agentes e workflows do vitalia-agent-kit-main no kit atual (Feature 008) |

## Topologia de Shards e Sincronização

```mermaid
graph TD
  "Raiz"["Repositório Raiz (.vitalia)"]
  "7f367bd3"["andrenote (7f367bd3)"] --> "Raiz"
  "f23704e7"["andre-desktop (f23704e7)"] --> "Raiz"
```

## Guard Rails de Grounding

| Arquivo | Status | Pendentes |
| :--- | :--- | :--- |
| `grounding-domains.yaml` (global) | ✅ Ativo | — |
| [grounding-domains-local.yaml](./grounding-domains-local.yaml) (projeto) | ✅ Presente — 24-08-2026 08:04 | ✅ 0 pendentes |
