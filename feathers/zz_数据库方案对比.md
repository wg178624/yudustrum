---
title: "数据库后端方案（SQLite vs MySQL）"
tags: [reference]
type: reference
---

# 羽渡尘数据库后端选型参考

## 背景

羽渡尘最初用文件系统 + grep 搜索羽毛（Markdown 文件 + `grep -ril`）。随着羽毛数量增长，需要数据库后端提升检索效率。

## 评估方案

### 方案A：MySQL + ngram 全文索引

| 项目 | 结论 |
|---|---|
| 中文全文搜索 | ✅ `WITH PARSER ngram` 支持中文 |
| 安装 | ❌ Debian 源无 MySQL，需手动编译或 Docker |
| 资源占用 | ❌ 需要运行 mysqld 服务 |
| D 盘部署 | ⚠️ 数据文件可放 D 盘，但服务在 WSL |
| 适用场景 | 大规模多用户，羽渡尘场景杀鸡用牛刀 |

```sql
CREATE TABLE feathers (
    id VARCHAR(64) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    tags VARCHAR(512),
    content TEXT NOT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_title (title),
    INDEX idx_tags (tags(255)),
    INDEX idx_created (created DESC)
);
ALTER TABLE feathers ADD FULLTEXT INDEX ft_content 
    (title, tags, content) WITH PARSER ngram;
    
SELECT * FROM feathers 
WHERE MATCH(content) AGAINST('羽渡尘' IN NATURAL LANGUAGE MODE);
```

**关键发现：** MariaDB（Debian 默认的 MySQL 替代）**不支持 ngram 分词器**，其默认全文分词器按空格/标点分词，不识别中文。

### 方案B：SQLite FTS5（选中方案 ✅）

| 项目 | 结论 |
|---|---|
| 中文全文搜索 | ✅ `tokenize='unicode61'` 支持中文 |
| 安装 | ✅ 系统自带，`sqlite3` 已安装 |
| 资源占用 | ✅ 无服务进程，单文件即数据库 |
| D 盘部署 | ✅ 直接建在 `D:\hermes-workspace\skills\yudustream\` |
| Python 集成 | ✅ `import sqlite3` 标准库，无需额外包 |
| 查看数据 | ✅ 可用任何 SQLite 浏览器打开 |

```sql
-- 建表 + FTS5 全文索引
CREATE TABLE feathers (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    tags TEXT NOT NULL DEFAULT '[]',
    content TEXT NOT NULL,
    source_path TEXT,
    created TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE VIRTUAL TABLE feathers_fts USING fts5(
    title, tags, content,
    content=feathers,
    content_rowid='rowid',
    tokenize='unicode61'
);

-- 中文全文搜索
SELECT * FROM feathers_fts 
WHERE feathers_fts MATCH '羽渡尘';
```

### 方案C：MariaDB 默认分词器（不推荐 ❌）

默认 InnoDB 全文索引按 `ft_min_word_len`（默认 3）和 `ft_max_word_len`（默认 84）切词，中文被当成单字节字符，**无法正确识别中文字词边界**。实测 `MATCH AGAINST('羽渡尘')` 返回空结果。

## 最终决定

采用 **SQLite FTS5** 作为羽渡尘数据库后端。原因：
1. 零安装、零配置、零服务进程
2. `unicode61` 分词器实测支持中文
3. 单文件可放 D 盘，随羽毛库一起迁移
4. Python 标准库直接连接，无额外依赖
5. 文件系统羽毛保留不变，数据库仅作为搜索引擎加速

## 扩展阅读

- [SQLite FTS5 官方文档](https://www.sqlite.org/fts5.html)
- [MySQL 8.0 全文搜索 (ngram)](https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html)
