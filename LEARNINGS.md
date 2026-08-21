<!-- LEARNINGS.md | Atualizado em: 21-08-2026 14:50:53(GMT-04:00) -->

# Aprendizados da Sessão

- [KIT] dynamic-questioning.yaml deve ser um Registry estruturado separado do prompt TOML. Permite extensão de domínios sem modificar o workflow. `[f23704e7]`
- [KIT] Hook before do TOML é o mecanismo correto para Scan Passivo de Ambiente via scan_environment.py --cwd={{cwd}}. Resultado em ~/.vitalia/kit/tmp/env_context.json. `[f23704e7]`
- [KIT] Saúde e Proteção de Dados devem ser P0 explícito no ordering das perguntas do brainstorming — não apenas regras de grounding. `[f23704e7]`
- [KIT] Padrão de indústria 2025: regras always-on não devem estar apenas no system prompt. Policy Evaluation Layer (código + LLM-as-Judge) é o padrão correto para enforcement de constituição. `[f23704e7]`
- [KIT] knowledge-curator (auto-expansão do kit) existe no vitalia-agent-kit-main mas não tem equivalente no kit atual — gap registrado como Feature 008 para próxima sessão. `[f23704e7]`
- Para evitar Context Drift, pesquisamos 3 opções de sanitização em transição de fase: 1. Progress -> Compress -> Reset (Modular Handoff), 2. Proactive Data Vaulting, 3. Revisitable Memory com Circuit Breakers. A serem decididas futuramente. `[62a9aef0]`
- IMPORTANTE: Ao iniciar esta sessão, ler OBRIGATORIAMENTE o arquivo 'resultado.md' na raiz do projeto (agente-local/resultado.md). Ele contém o briefing completo do brainstorming de 21-08-2026, as decisões arquiteturais registradas e as instruções comportamentais para simulação da Feature 007 enquanto o código ainda não existe. Lê-lo é pré-condição para iniciar qualquer trabalho. `[7f367bd3]`
