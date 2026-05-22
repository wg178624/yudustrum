---
title: 本地技能包迭代全览
tags: [技能, 版本, 迭代, 更新日志]
created: 2026-05-07T21:00:00+08:00
updated: 2026-05-22T14:00:00+08:00
type: feather
---

# 🪶 第4片羽毛 · 本地技能包迭代全览

## 🪶 羽渡尘
记忆管理系统
- v1.0.0 初版：四大目录 + 神蕴索引 + 自动存盘
- v1.1.0 中文注释规则 + 用户偏好 + Obsidian 集成
- v1.2.0 全局行为规则：先搜羽毛，命中引用，未命中建议存
- v1.3.0 iCloud Drive 集成
- v2.0.0 SQLite FTS5 全文搜索引擎
- v2.1.0 向量化引擎上线 ChromaDB（5月10日）
- v3.0.0 分层记忆 L0→L1→L2→L3（5月14日）
  - 参考 TencentDB Agent Memory 架构
  - Atom 自动提取，Scenario 场景聚合
- v4.0.0 符号化压缩 + 溯源链（5月22日）
  - YAML 摘要代替全文，省 70% Token
  - 每条事实可溯源到文件第几行
  - L3 Persona 自动构建
- v4.1.0 实体链接（5月22日）
  - 648 个实体，45 文件覆盖
  - 参考 Mem0 ADD-only 设计
- v4.2.0 反馈权重（5月22日）
  - 高频实体自动排前
  - 参考 Cognee 反馈闭环
- v4.3.0 时间窗口（5月22日）
  - 过期事实自动标记失效
  - 参考 Graphiti 时序知识图谱

## 🏥 系统维护医生 v1.1.0
kejilion.sh 工具箱
- v1.0.0 初版：命令参考
- v1.1.0 医疗化重写

## ⚔️ 振刀 v2.0.0
DeepSeek 缓存省钱
- v1.0.0 初版
- v1.1.0 官方文档校准
- v2.0.0 改名振刀

## 📦 货比三家 v1.0.0
花小钱办大事
- v1.0.0 初版

## 📘 EIE 私教 → eie-tutor → eie-csdiy-roadmap
电子信息工程学习路线
- v1.0.0 初版：仅模电
- v2.0.0 扩为 EIE 全能私教
- v2.1.0 新增高等数学+概率论教材（5月8日）
- v3.0.0 更名为 eie-csdiy-roadmap（5月8日）
  - 基于 csdiy.wiki 的四阶段自学路线
  - MIT/UCB/Stanford 公开课推荐
  - 3Blue1Brown 可视化教程对接

## 🔗 Chrome Bridge（新，5月10日）
Chrome 共享视野系统
- v1.0.0 Windows Chrome 远程调试桥接
- v2.0.0 WSL Linux Chrome 直连（5月10日）
  - Chrome 148 安装到 WSL
  - 通过 WSLg 在 Windows 桌面显示
  - 终端敲 chrome 启动
  - 数据独立在 D:\408\ChromeData
  - 最终方案：Linux Chrome 专用，Windows Chrome 不动

## 📡 AI HOT（新，5月8日）
AI 热点实时查询
- v1.0.0 安装配置
- 对接 aihot.virxact.com API
- 中文 AI 资讯实时抓取

## 🔄 Quansloth（新，5月21日）
本地 KV Cache 压缩引擎
- v1.0.0 引擎编译通过
  - TurboQuant CUDA 编译 100%
  - llama-server / llama-simple 就绪
  - RTX 4070 推理测试通过（306 tok/s）
  - 待解决：Qwen3.5 9B 兼容性问题
  - 待解决：gradio 依赖 Python 3.13 兼容

## 🧹 已退役
- OpenClaw（5月10日卸载）
- xrdp 远程桌面（5月10日禁用并卸载）
- VS Code 主力 IDE → 已换 Google Antigravity

## 🧬 技能合并（5月22日 — 9个→6个）
- chrome-bridge → windows-wsl-bridge（v3.0.0 合并）
- eie-tutor → eie-csdiy-roadmap（v1.3.0 合并，更名为 eie 全能体系）
- zhendao-cache → huo-bi-san-jia（v2.0.0 合并，货比三家+振刀合体）

## 🧠 羽渡尘完整进化史（截至 2026-05-22）

### 存储层
| 版本 | 新增能力 | 参考来源 |
|:----|---------|:--------:|
| v0   | SQLite FTS5 关键词搜索 | 自研 |
| v1   | shenyun.json 索引 + 自动存盘 | 自研 |
| v2   | ChromaDB 语义搜索 | Ollama nomic-embed-text |
| v3   | L0→L1→L2→L3 分层记忆 | TencentDB Agent Memory |
| v4   | 符号化压缩 + 溯源链 | 自研 |
| v4.1 | 实体链接 (648个) | Mem0 |
| v4.2 | 反馈权重 | Cognee |
| v4.3 | 时间窗口 | Graphiti |
| v5.0 | GraphRAG 关系图谱 (135节点/1414边) | NetworkX |
| v5.1 | 分层压缩 + LLM自动融合 + 冷热换页 | MemGPT |
| v5.2 | Agentic Memory 健康检查 + 周报 | 自研 |
| v5.3 | 记忆版本控制 + 变更追踪 | Git-like |
| v5.4 | Semantic Density Distillation | 自研 |
| v5.5 | 缓存对齐器 + 多路召回 | 自研 |
| v5.6 | 缓存块对齐 (全prompt) | DeepSeek KV Cache 文档 |
| v5.7 | 系统自检钩子 | 自研 |

### 数据统计
- 脚本数: 14 个 (yudustream 系列)
- 实体数: 648
- 关系边: 1414
- Git commit: 18 次
- 开发周期: 5月4日 — 5月22日（18天）

### 参考项目一览
| 项目 | 贡献 |
|:----|:----|
| TencentDB Agent Memory | 分层存储 L0→L3 |
| Mem0 | 实体链接 + ADD-only |
| Zep Graphiti | 时间窗口 + 事实生命周期 |
| Cognee | 反馈权重 + 自进化 |
| MemGPT | 虚拟内存换页 + 自动摘要 |
| GraphRAG | 关系图谱构建 |
| NetworkX | 图数据库引擎 |
| DeepSeek API | 缓存机制理解 + 对齐优化 |
