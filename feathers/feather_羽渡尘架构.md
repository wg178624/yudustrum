---
title: "羽渡尘系统架构"
tags: [架构, 核心]
type: doc
---

# 羽渡尘系统架构

## 整体架构

```
用户输入 → 羽渡尘插件 → 检索引擎 → 记忆召回 → 结果注入
```

## 引擎层

基于 YantrikDB 时序知识图谱引擎：
- 多路召回（实体精确匹配 + 图谱关系 + FTS5 全文搜索 + 向量语义搜索）
- L0-L3 分层记忆架构（参考 TencentDB-Agent-Memory）
- 矛盾检测与自动融合

## 插件层

Hermes Agent 插件，6 工具 + 4 hooks：
- recall / stats / save / audit / bake / compact
- on_message / on_session_start / on_session_end / on_pre_compress

## 可视化

仪表盘 dashboard.html，支持健康分、羽毛列表、知识图谱、时间轴。
