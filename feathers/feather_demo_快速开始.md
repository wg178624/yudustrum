---
title: "羽渡尘快速入门指南"
tags: [教程, 快速开始, 入门]
type: doc
retrieval: auto
---

# 羽渡尘快速入门

> 本文展示羽渡尘的基本使用方法。

## 安装

```bash
pip install zvec
# 将 yudustrum 目录放入 Hermes skills/
cp -r yudustrum ~/.hermes/skills/
```

## 添加记忆

在 `feathers/` 目录下新建 `.md` 文件，格式如下：

```markdown
---
title: "我的第一条记忆"
tags: [标签1, 标签2]
type: reference
retrieval: auto
---

# 记忆标题

正文内容...
```

## 检索

系统会自动检索与当前对话相关的记忆。也可手动调用：

```
yudustrum_recall(query="你需要什么", top_k=8)
```

## 技术架构

```
用户输入 → zvec FTS 检索 → 排序合并 → 注入上下文
          ↓
     返回相关记忆
```
