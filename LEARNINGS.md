<!-- LEARNINGS.md | Atualizado em: 26-08-2026 18:04:57(GMT-04:00) -->

# Aprendizados da Sessão

- [KIT] dynamic-questioning.yaml deve ser um Registry estruturado separado do prompt TOML. Permite extensão de domínios sem modificar o workflow. `[f23704e7]`
- [KIT] Hook before do TOML é o mecanismo correto para Scan Passivo de Ambiente via scan_environment.py --cwd={{cwd}}. Resultado em ~/.vitalia/kit/tmp/env_context.json. `[f23704e7]`
- [KIT] Saúde e Proteção de Dados devem ser P0 explícito no ordering das perguntas do brainstorming — não apenas regras de grounding. `[f23704e7]`
- [KIT] Padrão de indústria 2025: regras always-on não devem estar apenas no system prompt. Policy Evaluation Layer (código + LLM-as-Judge) é o padrão correto para enforcement de constituição. `[f23704e7]`
- [KIT] knowledge-curator (auto-expansão do kit) existe no vitalia-agent-kit-main mas não tem equivalente no kit atual — gap registrado como Feature 008 para próxima sessão. `[f23704e7]`
- Para evitar Context Drift, pesquisamos 3 opções de sanitização em transição de fase: 1. Progress -> Compress -> Reset (Modular Handoff), 2. Proactive Data Vaulting, 3. Revisitable Memory com Circuit Breakers. A serem decididas futuramente. `[62a9aef0]`
- IMPORTANTE: Ao iniciar esta sessão, ler OBRIGATORIAMENTE o arquivo 'resultado.md' na raiz do projeto (agente-local/resultado.md). Ele contém o briefing completo do brainstorming de 21-08-2026, as decisões arquiteturais registradas e as instruções comportamentais para simulação da Feature 007 enquanto o código ainda não existe. Lê-lo é pré-condição para iniciar qualquer trabalho. `[7f367bd3]`
- [KIT] Hooks stdlib-only (scan_environment.py / guardian_context.py) que dependem de variáveis de ambiente necessitam que o .env esteja carregado no processo ou que haja parser nativo para que os probes de rede ativos (Redis/Ollama) executem sem fallback. `[7f367bd3]`
- [KIT] A validação de hooks de infraestrutura deve ser sempre acompanhada de suíte E2E com o .venv do projeto para disparar tráfego real contra containers Docker locais. `[7f367bd3]`
- [PROJETO] Suíte E2E criada em tests/test_e2e_feature_007.py para validação contínua dos guardrails de contexto e conectividade de infraestrutura. `[7f367bd3]`
- [KIT] O isolamento em stdlib-only puro sem acoplamento ao workspace gerava falsos negativos em subshells desacoplados. O padrão arquitetural correto é Bootstrap de Venv/.env com Injeção dinâmica de sys.path, Fallback Gracioso e Consulta HITL. `[7f367bd3]`
- [KIT] A injeção dinâmica de site-packages do virtualenv em sys.path permite que hooks globais acessem bibliotecas do projeto (redis, requests, pydantic) sem exigir ativação manual de venv no shell. `[7f367bd3]`
- [KIT] Protocolo HITL com menu de 3 opções (Autocorreção assistida, Fallback de degradação, Parada) assegura governança e transparência diante de falhas de infraestrutura. `[7f367bd3]`
- [PROJETO] A manutenção de fontes do kit em manutencao_kit/ no repositório local garante versionamento e rastreabilidade dos scripts instalados no diretório global ~/.vitalia/kit/. `[7f367bd3]`
- [KIT] Test harnesses de infraestrutura não devem reimplementar lógica auxiliar de parsing nem fazer monkeypatch de paths; devem consumir estritamente o módulo central kit_env_bootstrap.init(). `[7f367bd3]`
- [KIT] O Redis por padrão (loglevel notice) não grava operações CRUD normais no stdout (docker logs); a auditoria de tráfego em tempo real deve ser feita via redis-cli monitor e info commandstats. `[7f367bd3]`
- [PROJETO] A segregação clara entre specs de produto (agente-local/specs/) e specs da infraestrutura do Kit Global (~/.vitalia/kit/specs/) é um débito técnico essencial para eliminar ambiguidade de escopo do agente. `[7f367bd3]`
- [KIT] Regra Geral Vitalia: O modo stdlib-only é ativado SE E SOMENTE SE a infraestrutura do agente-local não for detectada (Strict Fallback). Em presença do agente-local, o motor DEVE explorar toda a infraestrutura rica (.venv, Redis, barramento vitalia_events, WebSockets) para observabilidade em tempo real. `[7f367bd3]`
- Hospedar arquivos de schema estruturados (como JSON schemas) fisicamente no kit e referenciá-los nos prompts impede a deriva alucinatória de metadados por LLMs durante operações de ledger (JSONL). `[f23704e7]`
- O design de injeção de ambiente (kit_env_bootstrap.py) permite invocar scripts globais do kit contra repositórios independentes através do parâmetro explícito --cwd, mantendo as fontes isoladas sem duplicação. `[f23704e7]`
