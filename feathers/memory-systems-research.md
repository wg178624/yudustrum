---
title: "memory systems research"
tags: [reference]
type: reference
---

# 4 大 AI Agent 记忆系统核心设计研究

> 研究日期：2026-05-22
> 目标：抗遗忘（不丢信息）+ 省 Token（资源即金钱）
> 来源：Mem0 / Zep Graphiti / Letta(MemGPT) / Cognee

## 一、Mem0

**核心架构**：ADD-only 事实提取 + 向量/BM25/实体三重混合检索，SQLite 变更历史追踪。

**抗遗忘**：
1. 只增不删（V3 核心设计）— 每次对话只调一次 LLM 提取新事实，永不 UPDATE/DELETE
2. 实体链接 — 人名/产品名等实体存入独立向量集合，语义检索 miss 时实体匹配兜底
3. 多信号检索 — 语义 + BM25 关键词 + 实体匹配三路并行评分后 RRF 融合

**省 Token**：
1. 单次 LLM 调用 — 一次提取全部事实，无 agentic loop，每次检索 ~6.8K token
2. Top-k 只注入最相关记忆
3. 消息截断：超过 300 字符的部分截断

**对羽渡尘价值**：实体链接做检索回退 + ADD-only 防覆盖

## 二、Zep Graphiti

**核心架构**：基于 Neo4j/FalkorDB 的时序知识图谱，实体-关系-事实三元组带时间窗口。

**抗遗忘**：
1. 显式时间窗口 — 每条事实有 `valid_at` 和 `invalidated_at`，旧事实自动失效不删除
2. Episode 溯源 — 实体和关系追溯到原始对话，完整血缘链
3. 实体演进摘要 — 随时间更新实体摘要，保留核心属性

**省 Token**：
1. 检索 **零 LLM 调用** — 全用语义嵌入 + BM25 + BFS 图遍历
2. 增量构建 — 新对话只需增量处理
3. 可插拔 reranker — 仅对已缩减的候选集执行 LLM 级匹配

**对羽渡尘价值**：时间窗口显式标记过期事实，避免给出过时答案

## 三、Letta / MemGPT

**核心架构**：类 OS 的虚拟上下文管理 — 分层记忆（Core/Archival/Recall）+ 中断驱动的上下文换页。

**抗遗忘**：
1. 三层记忆：Core（始终在上下文的精华）→ Archival（持久化语义检索）→ Recall（完整对话历史）
2. 自动摘要压缩 — 上下文达 70% 水位时触发，早期消息 LLM 摘要替代原文
3. Git 版本化的 Memory Repository — 每次编辑产生 commit，支持 diff/回滚/分支

**省 Token**：
1. 滑动窗口 + 摘要 — 早期消息压缩为摘要，远少于原始 token
2. Archival 仅注入匹配结果
3. Core Memory 有字符限制（20K char），强制精炼

**对羽渡尘价值**：三级记忆 + 自动摘要触发，最系统的抗遗忘方案

## 四、Cognee

**核心架构**：记忆控制面 — 知识图谱 + 向量双引擎，Session cache + 永久图存储双层缓存。

**抗遗忘**：
1. Session + 持久化双层 — session 内快速缓存，结束后异步同步到永久图谱
2. 反馈循环 — agent 执行结果通过 TraceEntry 反馈回图谱，影响检索权重
3. 实体描述聚合 — 定期 consolidate_entity_descriptions

**省 Token**：
1. 检索类型自适应 — `scope="auto"` 自动选最低成本策略（先 session → 图 → 全量）
2. 图谱检索不依赖 LLM — 仅用向量 + 图遍历

**对羽渡尘价值**：反馈权重让高频有用的记忆自动排前面，越用越准

## 对比总结

| 维度 | Mem0 | Graphiti | Letta | Cognee |
|:----|:----|:--------|:-----|:-------|
| 核心范式 | 只增不删+实体链接 | 时序图+时间窗口 | 虚拟内存分层 | 反馈闭环 |
| 抗遗忘核心 | 永不覆盖 | 自动失效不删 | 摘要压缩保留 | 反馈权重 |
| 省 Token 核心 | ~6.8K/次检索 | 零 LLM 检索 | 70% 自动摘要 | 自适应路由 |
| 对羽渡尘价值 | 实体链接回退 | 过期标记 | 三级记忆 | 权重自进化 |

## 羽渡尘 v4 已实现 / 待实现

| 功能 | 状态 | 来源 |
|:----|:---:|:----|
| ADD-only 存盘 | ✅ | Mem0 |
| 分层渐进披露 L0→L3 | ✅ | Letta/TencentDB |
| 符号化压缩省 Token | ✅ | TencentDB |
| 溯源链 100% 可恢复 | ✅ | Graphiti |
| 时间窗口标记过期 | ❌ | Graphiti |
| 反馈权重自进化 | ❌ | Cognee |
| 实体链接检索回退 | ❌ | Mem0 |
