---
title: "MEMORY.md / USER.md / L3 区别"
tags: [reference]
type: reference
---

# MEMORY.md vs USER.md vs 铁律技能 vs 羽渡尘 — 四系统分工（v5.8）

Hermes Agent 框架和羽渡尘之间有**四个独立的存储系统**，分工不同，不能混用。

## 四系统一览

| 系统 | 位置 | 限额 | 注入prompt | 谁管理 | 内容类型 |
|:----|:----|:----:|:----------:|:------|:---------|
| **羽渡尘羽毛库** | `D:/yudustream/feathers/` | D盘506GB | ❌ 按需检索 | Agent + v5管线 | **主力记忆**：全部知识、配置、学习记录、图谱 |
| **user-iron-laws** | `~/.hermes/skills/dogfood/user-iron-laws/SKILL.md` | 无（skill文件） | 加载后生效 | Agent（永久刻入SSD） | **行为铁律**：爬虫规则、安全红线、称呼、搬家分级 |
| **USER.md** | `~/.hermes/memories/USER.md` | 5,000字 (已扩) | ✅ 每次对话 | Agent (memory tool) | **用户画像**：姓名、生日、偏好、计划、设备、账号 |
| **MEMORY.md** | `~/.hermes/memories/MEMORY.md` | 2,200字 | ✅ 每次对话 | yudustream_bootstrap.py | **实时快照窗口**：羽渡尘活跃实体+L3画像（动态生成） |

## 优先级（存储→检索）

```
存储优先级（新知识去哪）：
  1. 羽渡尘羽毛库 ← 一切新知识优先存这里
  2. USER.md ← 个人信息/偏好
  3. MEMORY.md ← 不直接存（只做快照窗口）

检索优先级（需要信息时）：
  1. MEMORY.md / USER.md ← 自动注入，秒读
  2. 羽渡尘 ← 四路召回按需检索
  3. user-iron-laws ← 永恒的行为约束
```

## 历史教训（2026-05-26 重构前的问题）

重构前 MEMORY.md 同时塞了环境配置 + 用户画像 + 铁律，导致 96% 满且 USER.md 半空。用户连续三次纠正才彻底厘清分工。

**核心原则：**
- 个人信息 → USER.md（不要放 MEMORY.md）
- 行为规则 → user-iron-laws 技能（刻入 SSD，不依赖任何文件）
- 知识记录 → 羽渡尘（feathers目录 + git版本化）
- MEMORY.md → 只做羽渡尘的快照窗口（动态生成，不做主力存储）
