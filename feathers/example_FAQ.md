---
title: "常见问题"
tags: [FAQ, 帮助]
type: doc
retrieval: explicit
---

# 常见问题

## 需要什么依赖？

仅需 Python 3.10+ 和 `pip install zvec`。

## 支持哪些语言？

中英文混合，支持 jieba 分词的 FTS 全文检索。

## 数据库会丢数据吗？

zvec 使用 WAL 预写日志，进程崩溃或断电后自动恢复，数据不丢。

## 跟 Hermes Agent 的关系？

羽渡尘作为 Hermes 插件运行，完全兼容 Hermes 的插件系统和工具注册机制。

## 如何可视化数据？

启动 Zvec Studio：
```bash
pip install zvec-studio
zvec-studio
```
打开 http://localhost:7860 即可浏览数据。
