<!-- LEARNINGS.md | Atualizado em: 20-08-2026 12:20:30(GMT-04:00) -->

# Aprendizados da Sessão

- [KIT] dynamic-questioning.yaml deve ser um Registry estruturado separado do prompt TOML. Permite extensão de domínios sem modificar o workflow. `[f23704e7]`
- [KIT] Hook before do TOML é o mecanismo correto para Scan Passivo de Ambiente via scan_environment.py --cwd={{cwd}}. Resultado em ~/.vitalia/kit/tmp/env_context.json. `[f23704e7]`
- [KIT] Saúde e Proteção de Dados devem ser P0 explícito no ordering das perguntas do brainstorming — não apenas regras de grounding. `[f23704e7]`
- [KIT] Padrão de indústria 2025: regras always-on não devem estar apenas no system prompt. Policy Evaluation Layer (código + LLM-as-Judge) é o padrão correto para enforcement de constituição. `[f23704e7]`
- [KIT] knowledge-curator (auto-expansão do kit) existe no vitalia-agent-kit-main mas não tem equivalente no kit atual — gap registrado como Feature 008 para próxima sessão. `[f23704e7]`
- Para evitar Context Drift, pesquisamos 3 opções de sanitização em transição de fase: 1. Progress -> Compress -> Reset (Modular Handoff), 2. Proactive Data Vaulting, 3. Revisitable Memory com Circuit Breakers. A serem decididas futuramente. `[62a9aef0]`
