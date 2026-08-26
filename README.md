<!-- README.md | Atualizado em: 26-08-2026 17:56:48(GMT-04:00) -->

# 🧠 Painel de Contexto — .vitalia

![Status](https://img.shields.io/badge/Status-LIVRE-2ea44f?style=for-the-badge&logo=github&logoColor=white)
![Semáforo](https://img.shields.io/badge/Semáforo-Desbloqueado-success?style=for-the-badge)
![Modo](https://img.shields.io/badge/Modo-Integrado%20(Full%20Observability)-8250df?style=for-the-badge)
![Sync](https://img.shields.io/badge/Sync-Multi--Machine%20Cloud-0969da?style=for-the-badge)
![Grounding](https://img.shields.io/badge/Grounding-0%20Pendentes-green?style=for-the-badge)

> **Vitalia Kit v0.5.0 — Ledger de Memória Persistente e Orquestração Multi-Máquina.**  
> Este repositório armazena o histórico distribuído, aprendizados consolidados e o controle de concorrência das sessões de trabalho do framework Vitalia.

---

## 📡 Topologia de Shards & Sincronização

<div align="center">

```mermaid
flowchart TD
  Cloud(("Nuvem Central (.vitalia)<br/>origin/main"))
  M_f23704e7["andrenote (f23704e7)<br/>● Ativo (Em Sessão)<br/>Modo: Integrado"]

  Cloud <-->|"26-08-2026 15:30:00(GMT-04:00)"| M_f23704e7

  style Cloud stroke:#0969da,stroke-width:2px,fill:#ddf4ff,color:#0969da
  style M_f23704e7 stroke:#6e7781,stroke-width:1px,fill:#f6f8fa,color:#57606a

```

</div>

---

## 🖥️ Máquinas e Status Atual

<table>
  <thead>
    <tr>
      <th align="left">Máquina / ID</th>
      <th align="left">Tarefa Atual</th>
      <th align="center">Ambiente</th>
      <th align="center">Status</th>
      <th align="left">Último Sync</th>
      <th align="left">Próximo Passo (P0)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>andrenote</strong><br/><code>f23704e7</code></td>
      <td>Feature 008 - Refatoração Engine & Guardian (Finalizada)</td>
      <td align="center"><span style="background-color:#8250df;color:white;padding:2px 6px;border-radius:4px;font-size:11px;">Integrado</span></td>
      <td align="center"><span style="color:#2ea44f;font-weight:bold;">● Concluído</span></td>
      <td>26-08-2026 15:30:00(GMT-04:00)</td>
      <td>Rodar o comando /vitalia-session-consolidate</td>
    </tr>

  </tbody>
</table>

---

## 🎯 Sessão Ativa em Destaque

- **Feature Ativa:** Feature 008 - Refatoração Engine & Guardian (Finalizada)
- **Máquina em Execução:** `andrenote` (`7f367bd3`)
- **Semáforo:** `LIVRE`
- **Próximo Passo (P0):**
  > Rodar o comando /vitalia-session-consolidate


---

## 📚 Histórico, Decisões & Guard Rails

<details>
<summary><strong>🔍 Clique para expandir o Histórico Completo de Sessões</strong></summary>

<br/>

### ✅ Sessão Encerrada em 26-08-2026 15:31(GMT-04:00)
- **Máquina:** `Unknown` (`f23704e7`)
- **Tarefa:** Feature 008 - Refatoração Engine & Guardian (Finalizada)
- **Atividades:**
  - - Isolamento dos schemas (learning/decision) exclusivamente no kit
  - Atualização unificada de hooks para scan_environment.py
  - Sincronização de Contratos_Comportamentais_contexto.md
  - Validação prática do hook scan_environment com --cwd
- **Próximo Passo:** Rodar o comando /vitalia-session-consolidate

---

### ✅ Sessão Encerrada em 25-08-2026 21:12:59(GMT-04:00)
- **Máquina:** `andrenote` (`7f367bd3`)
- **Tarefa:** session_history
- **Atividades:**
  - - Consolidação do Briefing canônico e atualização das specs 004 e 007 (Separação de Dados e Views, semáforo em JSON, limpeza de atexit).
- **Próximo Passo:** Unknown

---

### ✅ Sessão Encerrada em Unknown
- **Máquina:** `andrenote` (`7f367bd3`)
- **Tarefa:** Brainstorming e PRD Técnico da Feature 008 (Controle de Contexto & UX/UI)
- **Atividades:**
  - - Auditoria de Git e Repositórios da Tríade de Projetos
  - Briefing Canônico de Arquitetura (docs/BRIEFING_ARQUITETURA_CONTROLE_CONTEXTO.md)
  - Mockup Visual temp.md (Shields.io, Mermaid centralizado M_ e tabelas HTML)
  - PRD Técnico com Matriz Diferencial Modo Integrado vs Standalone (docs/PRD_CONTROLE_CONTEXTO_VITALIA.md)
  - Assentamento da Regra Geral Vitalia de Strict Fallback em learnings.jsonl
- **Próximo Passo:** Iniciar o ciclo SDD da Feature 008 acionando /vitalia-spec-specify para gerar spec.md e plan.md com base no PRD

---

### ✅ Sessão Encerrada em 22-08-2026 10:08(GMT-04:00)
- **Máquina:** `andrenote` (`7f367bd3`)
- **Tarefa:** Benchmark de Indústria, Saneamento de Testes e Sincronização do Kit Global
- **Atividades:**
  - - Auditoria de mercado das decisões do resultado.md, autópsia comportamental, sincronização integral de componentes para o Kit Global (~/.vitalia/kit/), refatoração de tests/test_e2e_feature_007.py e conftest.py para consumo exclusivo de kit_env_bootstrap.init(), remoção da pasta manutencao_kit/ e validação pura de 11 testes (unitários/E2E) com tráfego TCP confirmado no Redis.
- **Próximo Passo:** Iniciar ciclo SDD da Feature 008 (Refatoração do Motor de Contexto vitalia_context_engine.py, state/semaphore.json e README.md visual)

---

### ✅ Sessão Encerrada em 21-08-2026 20:36(GMT-04:00)
- **Máquina:** `andrenote` (`7f367bd3`)
- **Tarefa:** Feature 007 (Emenda 1) - Environment Bootstrap, Probes Ativos e Menu HITL
- **Atividades:**
  - - Ciclo SDD completo para a Emenda 1 da Feature 007. Implementado kit_env_bootstrap.py com parser nativo de .env e injecao de sys.path da .venv. Atualizados hooks guardian_context.py, scan_environment.py e llm_judge.py com probes reais. Suite de 11 testes automatizados aprovada com 100% de sucesso contra containers Docker e Ollama NO2.
- **Próximo Passo:** Iniciar Feature 008 (Refatoracao do Motor de Contexto vitalia_context_engine.py, state/semaphore.json e README.md visual)

---

### ✅ Sessão Encerrada em 21-08-2026 17:04(GMT-04:00)
- **Máquina:** `andrenote` (`7f367bd3`)
- **Tarefa:** Feature 007 - Testes de Integração e E2E do Guardian de Contexto
- **Atividades:**
  - - Validação completa da Feature 007: 23 testes unitários/integração + 5 testes E2E reais (tests/test_e2e_feature_007.py) com leitura de .env, tráfego TCP autenticado contra container Docker vitalia_redis (PING/SET/GET/DEL) e avaliação semântica no Ollama NO2.
- **Próximo Passo:** Refatoração do mecanismo de exibição de contexto no repositório da nuvem (vitalia_context_engine.py e README.md visual — Feature 008)

---

### ✅ Sessão Encerrada em 21-08-2026 16:38:23(GMT-04:00)
- **Máquina:** `Unknown` (`7f367bd3`)
- **Tarefa:** Feature 007 - Guardian de Contexto
- **Atividades:**
  - - Execução completa do tasks.md. Implementação do guardian_context.py (filtração por pid/token), scan_environment.py (probes reais) e llm_judge.py (gate SDD determinístico/Qwen). Configuração dos TOMLs (brainstorming e session-end).
- **Próximo Passo:** Testes end-to-end do Guardian na próxima feature simulada.

---

### ✅ Sessão Encerrada em 21-08-2026 14:44:16(GMT-04:00)
- **Máquina:** `andrenote` (`7f367bd3`)
- **Tarefa:** Unknown Task
- **Atividades:**
  - - Brainstorming completo para Feature 007 (Guardian de Contexto + LLM-as-Judge). Decisões: stdlib-only nos hooks, guardian filtra SESSION_HISTORY por relevância, LLM-as-Judge (Qwen NO2) na spec 007, curadoria grounding = HITL no session-end, scan_environment.py com probe real, Feature 008 adiada para sessão separada. resultado.md escrito como briefing da próxima sessão.
- **Próximo Passo:** Iniciar SDD Feature 007 via /vitalia-spec-specify

---

### ✅ Sessão Encerrada em 19-08-2026 20:17:00(GMT-04:00)
- **Máquina:** `andre-desktop` (`f23704e7`)
- **Tarefa:** Unknown Task
- **Atividades:**
  - - Correção do workflow de brainstorming: criado dynamic-questioning.yaml (9 domínios P0), scan_environment.py (hook passivo), atualizado brainstorming.toml v0.5.0 e emendado Artigo I da Constituição Vitalia (ciclo PEV de 6 etapas).
- **Próximo Passo:** Incorporar agentes vitalia-agent-kit-main no kit atual (Feature 008)

---

### ✅ Sessão Encerrada em 19-08-2026 15:06:35(GMT-04:00)
- **Máquina:** `andrenote` (`7f367bd3`)
- **Tarefa:** Feature 006: grounding-guard-rails + correção de regressões em workflows
- **Atividades:**
  - - Retomada da correção do kit
- **Próximo Passo:** Publicar repositórios no GitHub usando publicar-repos.md

---

### ✅ Sessão Encerrada em 13-08-2026 16:44(GMT-04:00)
- **Máquina:** `andrenote` (`7f367bd3`)
- **Tarefa:** Feature 006: grounding-guard-rails + correção de regressões
- **Atividades:**
  - - Sem resumo detalhado.
- **Próximo Passo:** Publicar repositórios no GitHub usando publicar-repos.md

---

### ✅ Sessão Encerrada em 13-08-2026 16:44(GMT-04:00)
- **Máquina:** `andrenote` (`7f367bd3`)
- **Tarefa:** Feature 006: grounding-guard-rails + correção de regressões
- **Atividades:**
  - - Sem resumo detalhado.
- **Próximo Passo:** Publicar repositórios no GitHub usando publicar-repos.md

---

### ✅ Sessão Encerrada em 17-08-2026 07:03:00(GMT-04:00)
- **Máquina:** `Unknown` (`7f367bd3`)
- **Tarefa:** Feature 006: grounding-guard-rails + correção de regressões em workflows
- **Atividades:**
  - - Sem resumo detalhado.
- **Próximo Passo:** Iniciar o planejamento e documentação da próxima feature (Feature 007) ou iniciar um novo fluxo de trabalho.

---

### ✅ Sessão Encerrada em 13-08-2026 16:44(GMT-04:00)
- **Máquina:** `andrenote` (`7f367bd3`)
- **Tarefa:** Feature 006: grounding-guard-rails + correção de regressões
- **Atividades:**
  - - Sem resumo detalhado.
- **Próximo Passo:** Publicar repositórios no GitHub usando publicar-repos.md

---

### ✅ Sessão Encerrada em 2026-08-08T09:28:31-04:00
- **Máquina:** `Unknown` (`7f367bd3`)
- **Tarefa:** Observability Enhancement - Documentação e Manuais
- **Atividades:**
  - - Sem resumo detalhado.
- **Próximo Passo:** Iniciar a Automação do Bench Test pipeline (criação de scripts e eventual integração visual com o Dashboard).

---


</details>

<details>
<summary><strong>⚖️ Clique para expandir as Decisões Arquiteturais Consolidadas</strong></summary>

<br/>

| Máquina (ID) | Decisão Arquitetural | Impacto / Racional |
| :--- | :--- | :--- |
| **Máquina** (`7f367bd3`) | **KIT** | [DECISÃO] Priorização estrita da Feature 008 no saneamento de débitos técnicos (motor de contexto e semáforo isolado em state/semaphore.json), postergando incorporação de novos agentes para ciclos futuros. |
| **Máquina** (`7f367bd3`) | **KIT** | [DECISÃO] Adoção do padrão Layered Evaluation Architecture (Chão Determinístico em código para permissão de ferramentas por fase + Teto Semântico no LLM Judge local Qwen para aderência à Constituição/regras clínicas). |
| **Máquina** (`7f367bd3`) | **DEC-007: Probes Reais de Conectividade com Credenciais do Workspace** | Hooks usam REDIS_URL e NO2_SERVER_IP reais para verificar saude dos servicos em tempo real. |
| **Máquina** (`7f367bd3`) | **DEC-006: Protocolo HITL para Falhas de Ambiente** | Adotado menu interativo com 3 opcoes (Autocorrecao, Fallback de degradacao, Parada imediata) em caso de .env/.venv ausentes ou containers desligados. |
| **Máquina** (`7f367bd3`) | **DEC-005: Bootstrap Central de Ambiente (kit_env_bootstrap.py)** | Criado helper kit_env_bootstrap.py com auto-descoberta de raiz, parser .env nativo e injecao de site-packages do .venv no sys.path para todos os hooks do kit. |
| **Máquina** (`7f367bd3`) | **Decisão** | [KIT] Padrão Vitalia para scripts invocados por hooks .toml: Opção C — stdlib-only obrigatório. Módulos externos (redis, requests, ollama) são importados dinamicamente com try/except, nunca como dependência rígida. Garante funcionamento em qualquer Python 3 sem venv. |
| **Máquina** (`7f367bd3`) | **Decisão** | [KIT] scan_environment.py deve: (1) probar conectividade real de Redis (import dinâmico + ping com timeout), (2) probar Ollama/NO2 via HTTP, (3) usar sufixo PID no output (env_context_<pid>.json) para evitar colisão entre workflows paralelos, (4) detectar e reportar VIRTUAL_ENV ativo. |
| **Máquina** (`7f367bd3`) | **Decisão** | [ARCH] Curadoria do grounding-domains.jsonl (promoção de entradas local→global, rejeição) deve ser responsabilidade exclusiva do workflow session-end, com etapa HITL que consulte o usuário. Curadoria manual direta nos arquivos é inaceitável. |
| **Máquina** (`62a9aef0`) | **Decisão** | [SEGURANÇA SPA] O Dashboard Local não deve acessar PHI no Redis sem redação (Masking) em tempo real via WebSocket, e exige JWT estrito para o front. |
| **Máquina** (`62a9aef0`) | **Decisão** | [DECISÃO] Adotado Opção A (Narrow Tooling) para Arquiteto e Opção A (On-the-loop sync) para Task Verifier. |
| **Máquina** (`62a9aef0`) | **Decisão** | [TECH DEBT] Implantar Opção A (State Machine/LangGraph determinística) para Enforcement do SDD. Atualmente usando Opção B (Prompt Reinforcement) provisoriamente. |
| **Máquina** (`62a9aef0`) | **Decisão** | [TECH DEBT] O workflow brainstorming ignorava o contexto. Solução: delegar a recuperação de contexto ao Sub-Agente para evitar estouro de tokens (window overflow) e alucinações, em vez de injetar o histórico inteiro. Risco provisório aceito: PHI nos logs crus até que o Sub-Agente Guardião seja construído para sanitização (Data Vault). |
| **Máquina** (`f23704e7`) | **Decisão** | Artigo I da Constituição emendado: SDD passa a ser ciclo PEV de 6 etapas formais (RAG Sync → specify → plan → tasks → Task Verifier Gate → implement). |
| **Máquina** (`f23704e7`) | **Decisão** | Separação kit × projeto: todos os 4 arquivos desta sessão foram criados/modificados exclusivamente em ~/.vitalia/kit/. O projeto agente-local não foi tocado. |
| **Máquina** (`7f367bd3`) | **Decisão** | Thin Client e Agnosticismo de Paths: Arquivos nos diretórios locais .agents / .gemini são meros shims; lógicas e templates devem ser consumidos do Kit Global e referenciados por {{VITALIA_DIR}} para evitar hardcoding. |
| **Máquina** (`7f367bd3`) | **Decisão** | Observabilidade via Dashboard de Vidro: Todas as execuções de LLM locais interceptadas via Fernet encryption para a fila vitalia_events, permitindo visualização de logs em WebSockets para depurar debates entre Arquiteto e Engenheiro. |
| **Máquina** (`7f367bd3`) | **Decisão** | Sub-Agente Policy & Task Verifier (Híbrido): Nova etapa silenciosa entre o spec-tasks e spec-implement. Usa script Python para quebrar tarefas e Qwen2.5-coder:7b para micro-inferência 1-para-1, barrando transições se houver violações. |
| **Máquina** (`7f367bd3`) | **Decisão** | Abandono de Múltiplos Arquivos de Spec: Em vez de spec médica, pedagógica etc. separadas, usa-se o workflow /vitalia-spec-specify acoplado ao sistema de Presets, modulando as seções da spec dinamicamente no runtime. |

</details>

<details>
<summary><strong>🛡️ Clique para expandir os Guard Rails de Grounding e Domínios</strong></summary>

<br/>

| Arquivo de Regras | Status | Domínios Monitorados | Pendentes de Curadoria HITL |
| :--- | :---: | :--- | :---: |
| `grounding-domains.yaml` (Global) | ✅ Ativo | `llm_models`, `python_packages`, `external_apis`, `security_practices`, `regulations`, `cloud_services`, `scientific_claims` | — |
| [grounding-domains-local.yaml](./grounding-domains-local.yaml) (Projeto) | ✅ Presente — 26-08-2026 13:56 | Domínios locais específicos do workspace | ✅ 0 pendentes |

</details>

---

<sub>Painel gerado automaticamente pelo motor de contexto do Vitalia Kit (<code>vitalia_context_engine.py --action consolidate</code>).</sub>
