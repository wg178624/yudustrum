---
title: "向量数据库搭建方案"
tags: [reference]
type: reference
---

# 羽渡尘向量数据库设置

## 架构

```
羽毛文件 (Markdown)
    ↓ 提取前3000字
Ollama nomic-embed-text (768维)
    ↓ 在 RTX 4070 上推理
ChromaDB 持久化存储
    ↓ cosine 距离检索
语义搜索结果
```

## 路径

- 向量数据库: `D:\408\yudustream_vectors\`
- 构建脚本: `/mnt/d/hermes-workspace/scripts/vectorize_yudustream_v2.py`
- 保险脚本: `/mnt/d/hermes-workspace/scripts/yudustream_safe.py`

## 模型

当前使用 Ollama `nomic-embed-text` (768维)，跑在 RTX 4070 上。
候选升级: `paraphrase-multilingual-MiniLM-L12-v2` (下载失败，需翻墙重试)。

## CRUD

### 新增羽毛后重建索引

```python
import chromadb
client = chromadb.PersistentClient(path="/mnt/d/408/yudustream_vectors")
client.delete_collection("yudustream")
# 然后重新运行 vectorize_yudustream_v2.py
```

### 查询示例

```python
import chromadb
client = chromadb.PersistentClient(path="/mnt/d/408/yudustream_vectors")
col = client.get_collection("yudustream")
results = col.query(query_texts=["用户的自然语言问题"], n_results=5)
for meta, dist in zip(results['metadatas'][0], results['distances'][0]):
    print(f"  [{1-dist:.2f}] {meta['title']}")
    print(f"  → {meta['path']}")
```

## 历史

| 版本 | 模型 | 维度 | 搜索效果 |
|:---|:---|:---:|:---:|
| v1 | all-MiniLM-L6-v2 | 384 | 0.19-0.41 |
| v2 (当前) | Ollama nomic-embed-text | 768 | 0.55-0.66 |

## 已知问题

- 文档超过 2000 字需要截断，否则 Ollama API 报错
- 更新版本后应重建集合（delete + create），增量添加可能产生不一致的向量空间
- 模型通过代理下载时需 `http_proxy=""` 绕过 v2rayN
