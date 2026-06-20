---
title: "羽渡尘系统架构"
tags: [架构, 核心]
type: doc
---

# 羽渡尘系统架构

## 整体架构

用户输入 → 羽渡尘插件 → zvec 引擎 → FTS 检索 → 结果注入

## 插件层
6 工具 + 4 hooks：recall / stats / save / audit / bake / compact
