---
title: "mindnode opml export"
tags: [reference]
type: reference
---

# 羽渡尘 → MindNode 脑图导出

## 用途

将羽渡尘的知识结构（分层架构、检索管线、工具生态、学习路线）导出为视觉脑图，在 iPhone/Mac 的 MindNode 中查看和编辑。

## 导出格式

MindNode 支持导入 OPML（标准大纲格式）和 FreeMind（.mm）格式。

## 导出流程

1. 确认要导出什么内容（分层架构/检索管线/学习路线/话题关联）
2. 我生成 OPML 文件
3. 保存到 D:\hermes-workspace\skills\yudustream\ 下
4. 用户通过 iCloud Drive 传到 iPhone
5. iPhone 文件 App → 分享 → 用 MindNode 打开

## 文件位置约定

```
D:\hermes-workspace\skills\yudustream\羽渡尘脑图_MindNode.opml
D:\hermes-workspace\skills\yudustream\*_MindNode.opml
```

## 示例

### OPML 结构规范

```xml
<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
  <head>
    <title>羽渡尘知识图谱</title>
  </head>
  <body>
    <outline text="羽渡尘">
      <outline text="一级节点">
        <outline text="二级节点 — 描述"/>
      </outline>
    </outline>
  </body>
</opml>
```

- `outline text="xxx"` 中的 text 属性就是节点文字
- 嵌套结构就是脑图的分支层级
- 叶子节点（最底层）建议带简短描述

## 配合 Mermaid 使用

先在羽毛中用 Mermaid 画脑图/关系图进行预览和调整，确认结构后再导出 OPML 给 MindNode。Mermaid 在 Obsidian 中直接渲染，OPML 在 MindNode 中渲染。
