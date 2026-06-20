# 🪶 羽渡尘 · Yudustrum (v6.0)

> A persistent memory system for AI agents. YantrikDB engine + multi-recall retrieval + L0-L3 hierarchical memory.

羽渡尘 is a memory system plugin for [Hermes Agent](https://github.com/NousResearch/hermes-agent). It enables AI agents to retain knowledge across conversations through structured memory management and semantic retrieval.

## Features

- **Multi-Recall Retrieval**: Entity exact matching, graph relationship search, FTS5 full-text search, vector semantic search
- **L0-L3 Hierarchical Memory**: Raw feathers → structured facts → scene aggregation → user profile
- **Knowledge Graph**: 135 nodes, 1414 edges, entity relationship network
- **Contradiction Detection**: Automatic conflict identification across memories
- **Cache Alignment**: Fixed prefix + append-only for KV cache optimization (>99% hit rate)
- **Dashboard**: Real-time health monitor, feather list, knowledge graph visualization

## Quick Start

```bash
# Deploy plugin to Hermes Agent
cp -r yudustrum ~/.hermes/skills/
# Add memories as .md files in feathers/, then recall:
yudustrum_recall(query="your question", top_k=8)
```

## Architecture

| Layer | Content | Format |
|:-----:|---------|:------:|
| L0 | Raw feathers (knowledge notes) | feathers/*.md |
| L1 | Structured facts + provenance | atoms/*.json |
| L2 | Scene aggregation | scenarios/*.json |
| L3 | User profile | persona/persona.json |
| G | Knowledge graph | graph/*.json (135 nodes, 1414 edges) |

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Search Engine | YantrikDB + SQLite FTS5 + vector index |
| Architecture | TencentDB-Agent-Memory (L3) |
| Platform | Hermes Agent plugin |
| Storage | JSON + YantrikDB dual engine |
| Visualization | dashboard.html + knowledge graph |

## License

MIT
