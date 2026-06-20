---
title: "羽渡尘最佳实践"
tags: [教程, 最佳实践, 技巧]
type: doc
retrieval: auto
---

# 羽渡尘最佳实践

## 记忆组织方式

1. **单篇单主题**：每篇羽毛只记录一个知识点
2. **Frontmatter**：善用 tags 标签分类
3. **retrieval 控制**：高频知识设为 auto，低频设为 explicit

## 系统集成

羽渡尘支持多种集成方式：
- Hermes Agent 插件（推荐）
- MCP 服务
- 独立 Python API

## 数据分析

通过 Zvec Studio（localhost:7860）可实时查看：
- 文档数量与存储占用
- FTS 检索测试
- 索引完整性
