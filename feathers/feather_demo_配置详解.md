---
title: "羽渡尘配置详解"
tags: [教程, 配置, 架构]
type: doc
retrieval: auto
---

# 羽渡尘配置详解

## 插件注册

在 `plugin.yaml` 中注册：

```yaml
name: yudustream
description: 羽渡尘记忆系统
tools: yudustream_tools
hooks:
  - on_message
  - on_session_start
  - on_session_end
  - on_pre_compress
```

## 数据库

基于 zvec（阿里开源矢量数据库）：
- FTS 全文检索 + jieba 中文分词
- WAL 预写日志（崩溃安全）
- 0-2ms 平均检索延迟

## 6 个内置工具

| 工具 | 功能 |
|------|------|
| recall | 检索相关记忆 |
| stats | 查看系统状态 |
| save | 手动存盘 |
| audit | 健康检查 |
| bake | 更新仪表盘 |
| compact | 压缩重复记忆 |
