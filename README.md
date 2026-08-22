<!-- README.md | Atualizado em: 21-08-2026 20:36:57(GMT-04:00) -->

# Dashboard de Contexto: .vitalia

## Semáforo de Sincronização

- **Status:** LIVRE | **Data:** 21-08-2026 20:36:57(GMT-04:00)
- **Máquina:** N/A
- **Expira em:** N/A

## Shards Ativos

| Máquina | Tarefa Atual | Etapas | Status | Último Sync | Próximo Passo (P0) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **andrenote** (7f367bd3) | Feature 007 (Emenda 1) - Environment Bootstrap, Probes Ativos e Menu HITL | ['Criacao do modulo central de bootstrap (kit_env_bootstrap.py) com parser nativo .env e injecao de sys.path da .venv.', 'Implementacao do Protocolo HITL com menu de 3 opcoes (Autocorrecao, Fallback, Parar) para falhas de infraestrutura.', 'Atualizacao dos hooks guardian_context.py, scan_environment.py e llm_judge.py com probes reais de Redis e Ollama NO2.', 'Execucao do ciclo SDD completo (spec, plan, tasks, analyze, implement, report).', 'Validacao de 11 testes automatizados (pytest tests/test_env_bootstrap.py tests/test_e2e_feature_007.py) com 100% de sucesso.'] | Concluído | 21-08-2026 20:36:50(GMT-04:00) | Iniciar Feature 008 (Refatoracao do Motor de Contexto vitalia_context_engine.py, state/semaphore.json e README.md visual) |
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
| [grounding-domains-local.yaml](./grounding-domains-local.yaml) (projeto) | ✅ Presente — 21-08-2026 16:36 | ✅ 0 pendentes |
