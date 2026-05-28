---
title: "tencentdb agent memory"
tags: [reference]
type: reference
---

# TencentDB Agent Memory — 分层记忆架构参考

> 来源：https://github.com/Tencent/TencentDB-Agent-Memory
> 参考日期：2026-05-10
> 用途：羽渡尘 v3 分层记忆（L0-L3）的架构灵感

## 核心理念

- **记忆分层**：不把所有数据平铺为向量，而是分层存储
- **符号化记忆**：用最少符号表达最多语义（Mermaid 画布）
- **渐进式披露与异构存储**：低层保留证据（DB/文件），高层保留结构（Markdown）
- **100% 可恢复**：每一条信息都可通过索引链路完整溯源

## 四层金字塔

| 层级 | 名称 | 羽渡尘对应 | 存储 |
|:----:|------|-----------|------|
| L0 | Conversation（原始对话） | Feathers（羽毛） | Markdown |
| L1 | Atom（结构化事实） | atoms/*.atom.json | JSON |
| L2 | Scenario（场景块） | scenarios/*.scenario.json | JSON |
| L3 | Persona（用户画像） | 记忆系统 + 偏好 | Hermes Memory |

## 参考数据

| Benchmark | 改进前 | 改进后 | 提升 |
|:---|---:|---:|---:|
| WideSearch 成功率 | 33% | 50% | +51% |
| SWE-bench 成功率 | 58.4% | 64.2% | +9.9% |
| PersonaMem 准确率 | 48% | 76% | +59% |
| Token 消耗(WideSearch) | 221M | 85M | -61% |

## 对羽渡尘的改进

1. 从平坦向量存储 → 分层记忆（三层次）
2. 从纯文本羽毛 → 结构化事实提取（Atom）
3. 从关键词搜索 → 场景聚合 + 语义搜索
4. 从单一索引 → 层索引（layer_index.json）
