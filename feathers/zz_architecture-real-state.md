---
title: "羽渡尘架构现状（v5版设计文档）"
tags: [reference]
type: reference
---

# 羽渡尘存储架构实况（2026-05-26）

## 现状

### 正在运转的三层

| 哪一层 | 路径 | 存什么 | 查询方式 |
|--------|------|--------|----------|
| 实体索引（JSON） | `entities/entity_index.json` | 648实体，每个映射到来源文件 | 精确匹配 `query.lower() in entity.lower()` |
| 反馈权重（JSON） | `entities/entity_weights.json` | 实体命中/未命中次数 + score | 排序 + 分层阈值（≥1核心，<1背景） |
| 关系图谱（JSON） | `graph/cooccurrence_graph.json` | 135节点，1414边，共现权重 | 源/目标匹配 `query in source or target` |
| FTS5 全文（SQLite） | `yudustream.db` | 羽毛内容表，unicode61分词 | SQL LIKE / FTS5 MATCH |
| 向量搜索（ChromaDB） | `D:\408\yudustream_vectors\` | nomic-embed-text 768维嵌入 | 余弦相似度语义搜索 |
| 语义密度（JSON） | `density_profile.json` | 场景→压缩率映射 | 查询场景模式匹配 |
| 层级画像（JSON） | `persona/persona.v4.json` | 自动统计的兴趣分布 | 直接读取（供bootstrap用） |
| 神蕴索引（JSON） | `shenyun.json` | 全部羽毛的元数据清单 | 遍历匹配 |
| 原始羽毛（Markdown） | `feathers/*.md` | 原始知识正文 | 翻阅，人类可读 |

### 不用的

| 目录 | 版本 | 为什么不用 |
|------|:----:|-----------|
| `atoms/` | v4 | 结构化事实提取，日常未触发 |
| `scenarios/` | v3 | 标签聚合，未被日常检索管线调用 |
| `symbols/` | v4 | 符号化压缩，生成但未被消费 |
| `compact/` | v5.1 | 全局知识蒸馏，用户知识规模未到触发阈值 |
| `cold_storage/` | v5.1 | 冷热换页，热数据太少无物可换 |
| `reports/` | v5.2 | Agentic 周报，跑过一次后未再用 |
| `changelog/` + `snapshots/` | v5.3 | 记忆版本控制，用户没有回滚需求 |
| `graph/temporal_graph.json` | v5.0 | 时序图，未被检索管线调用 |

## 关键架构决策

### 向量库 + 传统数据库共存（四路召回）

不是"选一种存储"，是"四种一起上，谁先命中用谁"：

1. 实体匹配（JSON）— 快，精确命中
2. 图谱关系（JSON）— 找关联
3. FTS5（SQLite）— 找关键词
4. 向量（ChromaDB）— 找语义近似

互补关系——实体没中找到图谱，图谱没连上走FTS5，FTS5找不到向量兜底。

### 为什么不用 MySQL

2026-05-10 评估，结论至今不变：
- SQLite FTS5 零配置、零服务、单文件可git
- 中文分词 `unicode61` 实测有效
- Debain 的 MariaDB 不支持 ngram 中文分词
- 羽渡尘单用户、47片羽毛 → MySQL 杀鸡用牛刀
- git版本化 MySQL 数据文件不现实

### MEMORY.md 不是主力记忆

用户三次纠正后定案：
- 羽渡尘 = 主力记忆（一切新知识存羽毛库）
- USER.md = 用户画像（个人信息）
- MEMORY.md = 羽渡尘的实时快照窗口（动态生成，不做主力）
- user-iron-laws skill = 行为铁律（刻进SSD）

## 启动流程（bootstrap）

每次新会话前或 `/reset` 后，跑 `yudustream_bootstrap.py`：

1. 查 `entity_weights.json` → 当前活跃实体（score≥3）
2. 查 `persona/persona.v4.json` → 用户最近关心的话题
3. 查 `feathers/` 最近修改的文件 → 最近3天新知识
4. 以上合并写入 MEMORY.md

这样 MEMORY.md 只是窗口，不是硬盘。羽渡尘才是本能。
