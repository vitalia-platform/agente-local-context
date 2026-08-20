import json
import uuid
import datetime

ts = "19-08-2026 15:55:00(GMT-04:00)"
machine_id = "7f367bd3"

learnings = [
    "Engenharia de Comportamento: O método 'operação de texto' falhou pois prompts .toml são especificações probabilísticas. Inserções devem respeitar semântica posicional; guard rails de conteúdo vão no final (Regra Cross-Cutting) para não interferir na âncora de comportamento original.",
    "Regra de Delegação Contínua: O Agente Arquiteto não deve usar memória base para tecnologias restritas; ele obrigatoriamente DELEGA as buscas ao Sub-Agente Pesquisador via Grounding Registry, resolvendo o Interleaving Problem.",
    "Memória RAG e Context Overload: A leitura do ambiente agora utiliza pgvector (banco vetorial local) para varredura passiva de arquivos. Limpeza de índices órfãos (stale) acontece na fase session-end via DELETE CASCADE.",
    "Tool Bridge (Redis Streams): Contorna as limitações de roteamento de ferramentas no AutoGen. O VitaliaOllamaClient intercepta, envia para vitalia:tool_requests, aguarda o worker e então devolve ao AutoGen, garantindo concorrência limpa.",
    "Dynamic Domain Routing: O grounding-domains.yaml deixou de ser lista plana para ser um Grounding Registry com schemas de validação. Ferramentas exigem retorno estruturado aderente ao schema embutido."
]

decisions = [
    "Abandono de Múltiplos Arquivos de Spec: Em vez de spec médica, pedagógica etc. separadas, usa-se o workflow /vitalia-spec-specify acoplado ao sistema de Presets, modulando as seções da spec dinamicamente no runtime.",
    "Sub-Agente Policy & Task Verifier (Híbrido): Nova etapa silenciosa entre o spec-tasks e spec-implement. Usa script Python para quebrar tarefas e Qwen2.5-coder:7b para micro-inferência 1-para-1, barrando transições se houver violações.",
    "Observabilidade via Dashboard de Vidro: Todas as execuções de LLM locais interceptadas via Fernet encryption para a fila vitalia_events, permitindo visualização de logs em WebSockets para depurar debates entre Arquiteto e Engenheiro.",
    "Thin Client e Agnosticismo de Paths: Arquivos nos diretórios locais .agents / .gemini são meros shims; lógicas e templates devem ser consumidos do Kit Global e referenciados por {{VITALIA_DIR}} para evitar hardcoding."
]

with open("/home/andre/projetos/assistidos/agente-local/.vitalia/memory/session/data/learnings.jsonl", "a", encoding="utf-8") as f:
    for text in learnings:
        obj = {
            "id": str(uuid.uuid4())[:8],
            "machine_id": machine_id,
            "timestamp": ts,
            "learning": f"[KIT] {text}"
        }
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")

with open("/home/andre/projetos/assistidos/agente-local/.vitalia/memory/session/data/decisions.jsonl", "a", encoding="utf-8") as f:
    for text in decisions:
        obj = {
            "id": str(uuid.uuid4())[:8],
            "machine_id": machine_id,
            "timestamp": ts,
            "decision": text
        }
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")
