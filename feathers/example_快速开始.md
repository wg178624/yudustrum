---
title: "快速开始"
tags: [教程, 入门]
type: doc
retrieval: auto
---

# 快速开始

## 安装

```bash
pip install zvec
# 将羽渡尘放入 Hermes skills 目录
cp -r yudustrum ~/.hermes/skills/
```

## 添加记忆

在 feathers/ 目录创建 .md 文件：

```markdown
---
title: "记忆标题"
tags: [标签1, 标签2]
retrieval: auto
---

# 标题

正文内容...
```

## 检索

系统自动将相关记忆注入对话。也可手动调用：

```
yudustrum_recall(query="需要什么", top_k=8)
```
