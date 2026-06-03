---
title: "DeepSeek KV Cache 官方文档 确认笔记"
tags: [DeepSeek, KV Cache, 缓存对齐, API, 羽渡尘]
type: feather
created: 2026-05-27
summary: "DeepSeek KV Cache 官方文档精读。确认缓存前缀单元完整匹配机制。验证羽渡尘缓存对齐策略正确。新增认知: 预热需1-2次MISS"
---

# DeepSeek KV Cache 官方文档

来源：https://api-docs.deepseek.com/zh-cn/guides/kv_cache

## 核心机制

- 缓存对所有用户默认开启，无需修改代码
- 缓存基于"缓存前缀单元"完整匹配
- 受 Sliding Window Attention 影响

## 缓存落盘三种时机

1. 请求边界持久化 — 每次请求在输入结束和输出结束位置各产出一个缓存前缀单元
2. 公共前缀检测持久化 — 系统自动检测多请求的公共前缀并落盘
3. 固定 token 间隔持久化 — 长输入按固定间隔切出缓存单元

## 示例分析

例一：多轮对话
  请求1: system + "中国首都是?" → MISS（落盘）
  请求2: system + "中国首都是?" + assistant + "美国首都是?" → system + user1 部分 HIT

例二：长文本问答
  请求1: system + <财报> + "总结" → MISS
  请求2: system + <财报> + "分析盈利" → MISS（检测到公共前缀 system + <财报>）
  请求3: system + <财报> + "分析收支" → system + <财报> HIT

## 对羽渡尘的验证

✅ 固定 system prompt → 正确
✅ 记忆前缀绝对稳定 → 正确
✅ 字典序对齐 → 正确
✅ 首次 MISS 不可避免 → 设计如此
✅ >99% 命中率是合理的（预热期 1-2 次 MISS）
