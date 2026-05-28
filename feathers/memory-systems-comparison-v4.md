---
title: "memory systems comparison v4"
tags: [reference]
type: reference
---

# 四大 Agent 记忆系统研究（2026-05-22）

## 研究结论

为羽渡尘 v4.3 的实体链接/反馈权重/时间窗口三大特性提供设计参考。

## 项目对比

| 维度 | Mem0 | Zep Graphiti | Letta/MemGPT | Cognee |
|------|------|-------------|-------------|--------|
| 核心架构 | ADD-only 事实提取 + 混合检索 | 时序知识图谱（时间窗口） | OS 虚拟内存分层 | Session cache + 知识图谱 |
| 抗遗忘 | 永不覆盖，只增不删 | 旧事实自动失效不删除 | 摘要压缩，原始保留 | 缓存+持久图同步 |
| 省 Token | ~6.8K/次检索 | 检索零 LLM 调用 | 70%水位触发摘要 | 自动路由最低成本策略 |
| 检索 | 语义+BM25+实体 | 语义+BM25+BFS | 语义向量 | 图+向量+KQL+LLM |

## 羽渡尘采纳情况

- Mem0 实体链接 → v4.1 entity_index.json ✅
- Cognee 反馈权重 → v4.2 entity_weights.json ✅
- Graphiti 时间窗口 → v4.3 fact_timeline.json ✅
- Letta 分层渐进 → v4 L0→L3 ✅

## 来源

- Mem0: https://github.com/mem0ai/mem0
- Zep Graphiti: https://github.com/getzep/graphiti
- Letta: https://github.com/letta-ai/letta
- Cognee: https://github.com/topoteretes/cognee
