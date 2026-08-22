<!-- DECISIONS.md | Atualizado em: 21-08-2026 20:36:57(GMT-04:00) -->

# Decisões Arquiteturais

- Abandono de Múltiplos Arquivos de Spec: Em vez de spec médica, pedagógica etc. separadas, usa-se o workflow /vitalia-spec-specify acoplado ao sistema de Presets, modulando as seções da spec dinamicamente no runtime. `[7f367bd3]`
- Sub-Agente Policy & Task Verifier (Híbrido): Nova etapa silenciosa entre o spec-tasks e spec-implement. Usa script Python para quebrar tarefas e Qwen2.5-coder:7b para micro-inferência 1-para-1, barrando transições se houver violações. `[7f367bd3]`
- Observabilidade via Dashboard de Vidro: Todas as execuções de LLM locais interceptadas via Fernet encryption para a fila vitalia_events, permitindo visualização de logs em WebSockets para depurar debates entre Arquiteto e Engenheiro. `[7f367bd3]`
- Thin Client e Agnosticismo de Paths: Arquivos nos diretórios locais .agents / .gemini são meros shims; lógicas e templates devem ser consumidos do Kit Global e referenciados por {{VITALIA_DIR}} para evitar hardcoding. `[7f367bd3]`
- Separação kit × projeto: todos os 4 arquivos desta sessão foram criados/modificados exclusivamente em ~/.vitalia/kit/. O projeto agente-local não foi tocado. `[f23704e7]`
- Artigo I da Constituição emendado: SDD passa a ser ciclo PEV de 6 etapas formais (RAG Sync → specify → plan → tasks → Task Verifier Gate → implement). `[f23704e7]`
- [TECH DEBT] O workflow brainstorming ignorava o contexto. Solução: delegar a recuperação de contexto ao Sub-Agente para evitar estouro de tokens (window overflow) e alucinações, em vez de injetar o histórico inteiro. Risco provisório aceito: PHI nos logs crus até que o Sub-Agente Guardião seja construído para sanitização (Data Vault). `[62a9aef0]`
- [TECH DEBT] Implantar Opção A (State Machine/LangGraph determinística) para Enforcement do SDD. Atualmente usando Opção B (Prompt Reinforcement) provisoriamente. `[62a9aef0]`
- [DECISÃO] Adotado Opção A (Narrow Tooling) para Arquiteto e Opção A (On-the-loop sync) para Task Verifier. `[62a9aef0]`
- [SEGURANÇA SPA] O Dashboard Local não deve acessar PHI no Redis sem redação (Masking) em tempo real via WebSocket, e exige JWT estrito para o front. `[62a9aef0]`
- [ARCH] Curadoria do grounding-domains.jsonl (promoção de entradas local→global, rejeição) deve ser responsabilidade exclusiva do workflow session-end, com etapa HITL que consulte o usuário. Curadoria manual direta nos arquivos é inaceitável. `[7f367bd3]`
- [KIT] scan_environment.py deve: (1) probar conectividade real de Redis (import dinâmico + ping com timeout), (2) probar Ollama/NO2 via HTTP, (3) usar sufixo PID no output (env_context_<pid>.json) para evitar colisão entre workflows paralelos, (4) detectar e reportar VIRTUAL_ENV ativo. `[7f367bd3]`
- [KIT] Padrão Vitalia para scripts invocados por hooks .toml: Opção C — stdlib-only obrigatório. Módulos externos (redis, requests, ollama) são importados dinamicamente com try/except, nunca como dependência rígida. Garante funcionamento em qualquer Python 3 sem venv. `[7f367bd3]`
- Criado helper kit_env_bootstrap.py com auto-descoberta de raiz, parser .env nativo e injecao de site-packages do .venv no sys.path para todos os hooks do kit. `[7f367bd3]`
- Adotado menu interativo com 3 opcoes (Autocorrecao, Fallback de degradacao, Parada imediata) em caso de .env/.venv ausentes ou containers desligados. `[7f367bd3]`
- Hooks usam REDIS_URL e NO2_SERVER_IP reais para verificar saude dos servicos em tempo real. `[7f367bd3]`
