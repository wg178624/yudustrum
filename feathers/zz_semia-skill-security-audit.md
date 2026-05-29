---
title: "Semia 安全审计规则（写skill参考）"
tags: [reference]
type: reference
---

# Semia — Agent Skill 安全审计

来源：https://github.com/berabuddies/Semia（2026-05-25 开源）
Star: 231，Fork: 50
作者：berabuddies（前 RiemaLabs）

## 核心能力

静态分析 AI agent skill（SKILL.md），提取所有隐式能力：
- 执行的 shell 命令
- 发起的网络请求
- 读写的文件路径
- 引用的环境变量/密钥
- 调用的工具和参数
- 每条结论标注对应源代码行号

## 安装

```bash
pip install semia-audit
```

## 使用

```bash
# 扫描单个 skill
semia scan ./some-skill

# 扫描 + 修复
semia repair ./some-skill

# 输出格式
# 默认：report.md（按严重级别排序）
# 支持：SARIF 2.1.0（GitHub Code Scanning）、JSON
```

## 插件集成

支持 Codex、Claude Code、OpenClaw 作为插件安装。

## 对羽渡尘的用途

扫描 feathers/*.md 和用户安装的 third-party skills，检查：
- 是否有未声明的命令注入
- 是否有不必要的文件/网络访问
- 是否引用了不应存在的环境变量
- 每条结论锚定到具体行号，可追溯

## 注意事项

- Semia 是为 Codex/Claude Code/OpenClaw 的 skill 格式设计的
- Hermes 的 skill 格式与它们类似但不完全一致
- 扫描结果需人工判断误报
