---
title: "羽渡尘系统架构"
tags: [架构, 核心]
type: doc
retrieval: auto
---

# 羽渡尘系统架构

## 整体架构

```
用户输入 → 羽渡尘插件 → zvec 引擎 → FTS 检索 → 结果注入
                ↑                          ↓
           feathers/ 源文件          Zvec Studio 可视化
```

## 引擎层

基于 zvec（阿里开源矢量数据库）：
- FTS 全文检索 + jieba 中文分词
- WAL 预写日志（崩溃恢复）
- 0-2ms 平均检索延迟
- Apache-2.0 协议

## 插件层

Hermes Agent 插件，6 工具 + 4 hooks：
- recall / stats / save / audit / bake / compact
- on_message / on_session_start / on_session_end / on_pre_compress
