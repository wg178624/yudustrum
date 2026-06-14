# 🪶 羽渡尘 · Yudustrum (v5.0)

> A persistent memory system for AI agents. Version 5.0 — the open-source foundation.

**羽渡尘** is the artifact of the **Fu Hua** in Honkai Impact 3 — a divine object that governs memory. This project brings that concept to AI agents: a structured long-term memory repository.

---

## What It Does

| Layer | Description |
|-------|------------|
| **Feathers** | Markdown-based knowledge snippets with YAML frontmatter (brief/full dual storage) |
| **Auto-save** | Session-end memory backups, organized by date |
| **Anchors** | Progress checkpoints — pick up where you left off |
| **Compact** | Context compression cache for token efficiency |
| **Entity Index** | JSON-based entity extraction and relationship tracking |
| **Persona** | User profile with 3 layers (L1 base / L2 preferences / L3 persona) |

## Architecture

```
feathers/       → 精炼知识（Markdown + YAML frontmatter）
auto-save/     → 会话自动存盘
anchors/       → 进度节点
compact/       → 上下文压缩
persona/       → 用户画像（L1/L2/L3 三层）
entities/      → 实体索引与关系图谱
graph/         → 共现图谱（JSON）
```

## Tech Stack

- **Format** — Markdown with YAML frontmatter
- **Storage** — Flat files + JSON indexes
- **Agent** — Designed for AI agent long-term memory
- **Tooling** — Obsidian-compatible, human-readable

## Status

**v5.0 (archived)** — The open-source release of an actively developed system.  
The current daily‑driver is v7.0 with YantrikDB, real‑time health monitoring, and full knowledge graph — this repo is the stable foundation it evolved from.

## License

MIT
