<!-- LEARNINGS.md | Atualizado em: 28-08-2026 12:18:06(GMT-04:00) -->
# 💡 Aprendizados Técnicos e Lições Aprendidas Consolidadas

**Data/Hora de Geração:** `28-08-2026 12:18:06(GMT-04:00)` | **Fuso Horário:** America/Cuiaba `(GMT-04:00)`

## [PROJETO]
- **Aprendizado:** [KIT] dynamic-questioning.yaml deve ser um Registry estruturado separado do prompt TOML. Permite extensão de domínios sem modificar o workflow.
  - **Racional:** Registro defasado
  - **Origem:** `f23704e7` | **Data:** 19-08-2026 20:17(GMT-04:00)
- **Aprendizado:** [KIT] Hook before do TOML é o mecanismo correto para Scan Passivo de Ambiente via scan_environment.py --cwd={{cwd}}. Resultado em ~/.vitalia/kit/tmp/env_context.json.
  - **Racional:** Registro defasado
  - **Origem:** `f23704e7` | **Data:** 19-08-2026 20:17(GMT-04:00)
- **Aprendizado:** [KIT] Saúde e Proteção de Dados devem ser P0 explícito no ordering das perguntas do brainstorming — não apenas regras de grounding.
  - **Racional:** Registro defasado
  - **Origem:** `f23704e7` | **Data:** 19-08-2026 20:17(GMT-04:00)
- **Aprendizado:** [KIT] Padrão de indústria 2025: regras always-on não devem estar apenas no system prompt. Policy Evaluation Layer (código + LLM-as-Judge) é o padrão correto para enforcement de constituição.
  - **Racional:** Registro defasado
  - **Origem:** `f23704e7` | **Data:** 19-08-2026 20:17(GMT-04:00)
- **Aprendizado:** [KIT] knowledge-curator (auto-expansão do kit) existe no vitalia-agent-kit-main mas não tem equivalente no kit atual — gap registrado como Feature 008 para próxima sessão.
  - **Racional:** Registro defasado
  - **Origem:** `f23704e7` | **Data:** 19-08-2026 20:17(GMT-04:00)
- **Aprendizado:** Para evitar Context Drift, pesquisamos 3 opções de sanitização em transição de fase: 1. Progress -> Compress -> Reset (Modular Handoff), 2. Proactive Data Vaulting, 3. Revisitable Memory com Circuit Breakers. A serem decididas futuramente.
  - **Racional:** Registro defasado
  - **Origem:** `62a9aef0` | **Data:** 20-08-2026 09:50(GMT-04:00)
- **Aprendizado:** IMPORTANTE: Ao iniciar esta sessão, ler OBRIGATORIAMENTE o arquivo 'resultado.md' na raiz do projeto (agente-local/resultado.md). Ele contém o briefing completo do brainstorming de 21-08-2026, as decisões arquiteturais registradas e as instruções comportamentais para simulação da Feature 007 enquanto o código ainda não existe. Lê-lo é pré-condição para iniciar qualquer trabalho.
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 21-08-2026 14:37:41(GMT-04:00)
- **Aprendizado:** [KIT] Hooks stdlib-only (scan_environment.py / guardian_context.py) que dependem de variáveis de ambiente necessitam que o .env esteja carregado no processo ou que haja parser nativo para que os probes de rede ativos (Redis/Ollama) executem sem fallback.
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 21-08-2026 17:04(GMT-04:00)
- **Aprendizado:** [KIT] A validação de hooks de infraestrutura deve ser sempre acompanhada de suíte E2E com o .venv do projeto para disparar tráfego real contra containers Docker locais.
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 21-08-2026 17:04(GMT-04:00)
- **Aprendizado:** [PROJETO] Suíte E2E criada em tests/test_e2e_feature_007.py para validação contínua dos guardrails de contexto e conectividade de infraestrutura.
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 21-08-2026 17:04(GMT-04:00)
- **Aprendizado:** O Hook Runner necessita injetar dinamicamente o PYTHONPATH apontando para o seu diretório pai (~/.vitalia/kit/scripts) de forma que scripts secundários consigam importar os módulos do Kit, independente de onde sejam acionados.
  - **Racional:** Registro defasado
  - **Origem:** `f23704e7` | **Data:** 26-08-2026 22:07(GMT-04:00)
- **Aprendizado:** Arquivos adicionados ao .gitignore após já estarem sendo rastreados pelo Git devem ser explicitamente desindexados com 'git rm -r --cached <pasta>' para que parem de ser identificados como modificados durante regenerações sistêmicas.
  - **Racional:** Registro defasado
  - **Origem:** `f23704e7` | **Data:** 26-08-2026 22:07(GMT-04:00)

## KIT
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 21-08-2026 20:36(GMT-04:00)
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 21-08-2026 20:36(GMT-04:00)
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 21-08-2026 20:36(GMT-04:00)
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 22-08-2026 10:08(GMT-04:00)
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 22-08-2026 10:08(GMT-04:00)
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 24-08-2026 11:05:00(GMT-04:00)
- **Aprendizado:** Hospedar arquivos de schema estruturados (como JSON schemas) fisicamente no kit e referenciá-los nos prompts impede a deriva alucinatória de metadados por LLMs durante operações de ledger (JSONL).
  - **Racional:** Registro defasado
  - **Origem:** `f23704e7` | **Data:** 26-08-2026 15:31(GMT-04:00)
- **Aprendizado:** O design de injeção de ambiente (kit_env_bootstrap.py) permite invocar scripts globais do kit contra repositórios independentes através do parâmetro explícito --cwd, mantendo as fontes isoladas sem duplicação.
  - **Racional:** Registro defasado
  - **Origem:** `f23704e7` | **Data:** 26-08-2026 15:31(GMT-04:00)
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 28-08-2026 12:16(GMT-04:00)
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 28-08-2026 12:16(GMT-04:00)
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 28-08-2026 12:16(GMT-04:00)

## PROJETO
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 21-08-2026 20:36(GMT-04:00)
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 22-08-2026 10:08(GMT-04:00)
- **Aprendizado:** 
  - **Racional:** Registro defasado
  - **Origem:** `7f367bd3` | **Data:** 28-08-2026 12:16(GMT-04:00)

## [KIT]
- **Aprendizado:** Modular Monolith com Auto-Injeção de Sys.Path no topo de cada submódulo permite execução autônoma via CLI sem erros de import.
  - **Racional:** Assegura resiliência máxima e suporte estrito ao modo Standalone stdlib-only sem depender de pip install -e .
  - **Origem:** `andrenote` | **Data:** 28-08-2026 09:12:43(GMT-04:00)
- **Aprendizado:** Conferência defensiva sintática pré-gravação com py_compile elimina 100% dos riscos de corrupção sintática em modificadores de código.
  - **Racional:** Impede que quebras de linha ou caracteres escapados corrompam código funcional em produção.
  - **Origem:** `andrenote` | **Data:** 28-08-2026 09:12:43(GMT-04:00)
- **Aprendizado:** Consumir dashboard_template.md com placeholders dedicados desacopla a camada visual da lógica de persistência e garante fidelidade ao temp.md.
  - **Racional:** Permite alterar layout e badges sem alterar o código de backend do Context Engine.
  - **Origem:** `andrenote` | **Data:** 28-08-2026 09:12:43(GMT-04:00)
