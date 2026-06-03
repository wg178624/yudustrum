---
title: "记忆系统实现方案"
tags: [reference]
type: reference
---

# 羽渡尘 v4.3 实现参考：4 大记忆系统设计对比

## 研究范围

| 项目 | GitHub | 核心范式 |
|------|--------|---------|
| **Mem0** | mem0ai/mem0 | ADD-only 事实提取 + 实体链接 + 多信号混合检索 |
| **Zep Graphiti** | getzep/graphiti | 时序知识图谱（时间窗口 + 溯源链） |
| **Letta/MemGPT** | letta-ai/letta | OS 虚拟内存分层（Core/Archival/Recall） |
| **Cognee** | topoteretes/cognee | Session cache + 知识图谱 + 反馈权重 |

## 已实现功能映射

| 策略 | 来源 | 羽渡尘位置 | 实现方式 |
|:----|:----|:-----------|:---------|
| 实体链接检索回退 | Mem0 | `entities/entity_index.json` | 正则提取 + 去重索引，648 实体 / 45 文件 |
| 反馈权重自排序 | Cognee | `entities/entity_weights.json` | 命中+1，未命中-1，自动排序 |
| 时间窗口过期标记 | Graphiti | `entities/fact_timeline.json` | record_fact + expire_fact 接口 |
| 溯源链 100% 可恢复 | Graphiti | v4 trace_chain | 每条 Atom 带源文件行号 + trace_id |
| 符号化压缩省 Token | TencentDB | v4 Symbolic | JSON 符号摘要替代全文 |

## 未实现但值得跟踪

| 功能 | 来源 | 备注 |
|:----|:----|:----|
| Mermaid 符号图谱 | TencentDB | Token 效率最优但实现复杂度高 |
| 自动摘要触发 (70% 水位) | Letta | 当前靠手动 `太虚剑神`，可自动化 |
| 图遍历检索 (BFS) | Graphiti | 依赖图数据库，当前先用实体索引近似 |
| Session cache 双存储 | Cognee | 收益有限，等羽毛 50+ 再考虑 |
