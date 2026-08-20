<!-- DECISIONS.md | Atualizado em: 19-08-2026 20:22:57(GMT-04:00) -->

# Decisões Arquiteturais

- Abandono de Múltiplos Arquivos de Spec: Em vez de spec médica, pedagógica etc. separadas, usa-se o workflow /vitalia-spec-specify acoplado ao sistema de Presets, modulando as seções da spec dinamicamente no runtime. `[7f367bd3]`
- Sub-Agente Policy & Task Verifier (Híbrido): Nova etapa silenciosa entre o spec-tasks e spec-implement. Usa script Python para quebrar tarefas e Qwen2.5-coder:7b para micro-inferência 1-para-1, barrando transições se houver violações. `[7f367bd3]`
- Observabilidade via Dashboard de Vidro: Todas as execuções de LLM locais interceptadas via Fernet encryption para a fila vitalia_events, permitindo visualização de logs em WebSockets para depurar debates entre Arquiteto e Engenheiro. `[7f367bd3]`
- Thin Client e Agnosticismo de Paths: Arquivos nos diretórios locais .agents / .gemini são meros shims; lógicas e templates devem ser consumidos do Kit Global e referenciados por {{VITALIA_DIR}} para evitar hardcoding. `[7f367bd3]`
- Separação kit × projeto: todos os 4 arquivos desta sessão foram criados/modificados exclusivamente em ~/.vitalia/kit/. O projeto agente-local não foi tocado. `[f23704e7]`
- Artigo I da Constituição emendado: SDD passa a ser ciclo PEV de 6 etapas formais (RAG Sync → specify → plan → tasks → Task Verifier Gate → implement). `[f23704e7]`
