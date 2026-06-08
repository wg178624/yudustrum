---
title: 工具使用手册（当前环境）
brief: "Hermes工作环境工具使用说明：文件读写、代码执行、浏览器操作、技能管理、日志处理等命令参考。"
tags: [工具, WSL, Hermes, Chrome, VPS, Obsidian]
created: 2026-05-04T20:35:00+08:00
updated: 2026-05-29T21:00:00+08:00
type: feather
---

# 🪶 第2片羽毛 · 工具使用手册（更新至 5/29）

## 核心工作流

```
你 → Hermes (DeepSeek V4 Flash)
  → 检索羽渡尘（实体/图谱/FTS5/向量）
  → 执行任务（终端/浏览器/Python/Git）
  → 存盘（备份 → 烘焙 → commit）
```

## 羽渡尘（记忆+学习系统）

| 项目 | 路径 |
|------|------|
| 数据根目录 | `D:\hermes-workspace\skills\yudustrum\` |
| 羽毛库 | `feathers/`（31 片 .md） |
| 实体索引 | `entities/entity_index.json`（1329 实体） |
| 神蕴索引 | `shenyun.json`（28 条） |
| 教材库 | `教材库/`（21 本 PDF） |
| 仪表盘 | `dashboard.html`（浏览器打开） |
| 后端 | `server.py`（端口 8080，cron @reboot） |
| Nginx 反代 | 端口 8081，静态文件+API 代理 |

## 运行环境

| 设备 | 名称 | 用途 |
|:----:|:----:|------|
| 机械革命极光X | 鸡哥/老家 | 主力开发（32GB/4070/2TB） |
| WSL Debian 13 | — | Hermes + 羽渡尘运行 |
| RackNerd 圣何塞 | VPS | 翻墙专用（1核/967MB） |

**铁律：VPS 只管翻墙，所有开发在老家 WSL 搞。除非 VPS 坏了不进。**

## 浏览器（爬虫/搜索）

| 方案 | 端口 | 用途 |
|:----:|:----:|------|
| Linux Chrome headless | 9222 | 主力爬虫/百科/搜索（crontab @reboot） |
| CF Worker 反代 | — | 能过的站优先用 Worker（hermes-scraper.workers.dev） |

Worker 不行时回退浏览器。

## 存盘流程

```bash
python3 /mnt/d/hermes-workspace/scripts/yudustream_backup.py     # 备份核心数据到 D:\408\
python3 /mnt/d/hermes-workspace/scripts/bake_dashboard.py         # 烘焙仪表盘数据
cd /mnt/d/hermes-workspace/skills/yudustrum && git add -A && git commit -m "💾 ..."
```

## 系统工具

| 工具 | 用途 |
|------|------|
| `k` | kejilion.sh 系统维护（两地通用） |
| `gcc` | C 语言编译器（14.2.0） |
| `tesseract` | OCR（英文书直接读，中文书+预处理） |
| `python3` | 3.13.5，主力语言 |
| `nginx` | 仪表盘反代（端口 8081） |
| `mariadb` | MySQL 兼容，已建 yudustrum 库 |

## 学习工具

| 工具 | 用途 |
|:----:|------|
| 计组（唐朔飞） | T0 进行中 |
| C Primer Plus | T0 配合计组 |
| 模电（童诗白） | T1 |
| 数电（阎石） | T1 |
| 工程控制论（钱学森 + 英文原版） | T1 |
| LTSpice | 模电仿真（Windows 免费） |
| Icarus Verilog | 数电仿真（apt install） |

## 已废弃/退役

| 项目 | 原因 |
|:----|:----|
| CodeX | 不需要编码代理 |
| OpenClaw | 已卸载（5/10） |
| Ollama | 本地模型不如 API 划算 |
| NVIDIA NIM API Key | 已失效，不再使用 |
| ChromaDB 向量搜索 | 已合并入检索管线 |
| WhatsApp Bridge | VPS 临时残留，已清理 |
