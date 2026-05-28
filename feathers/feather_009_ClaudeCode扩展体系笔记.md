---
title: "Claude Code 扩展体系官方文档笔记"
tags: [Claude Code, Skills, Subagents, MCP, Hooks, 架构参考]
type: feather
created: 2026-05-27
---

# Claude Code 扩展体系 — 读书笔记

官网：https://code.claude.com/docs/en/
索引：https://code.claude.com/docs/llms.txt（AI可读）

## 五大扩展机制

| 机制 | 作用 | 何时加 |
|------|------|--------|
| CLAUDE.md | 持久上下文，每次会话自动加载 | 同一个规则 Claude 错两次 |
| Skills | 可复用知识/流程，按需加载 | 第三次粘贴同一段流程 |
| Subagents | 隔离上下文，只返回摘要 | 测任务刷屏主上下文 |
| MCP | 连接外部工具/数据库/API | 频繁从浏览器贴数据 |
| Hooks | 生命周期自动化（30+事件） | 每次文件编辑后自动触发 |

## Skills 核心设计

### 文件结构
```
my-skill/
├── SKILL.md           # 主内容（必需）
├── reference.md        # 详细参考（按需加载）
├── examples/           # 示例输出
└── scripts/            # 可执行脚本
```

### 关键 frontmatter
```yaml
---
name: my-skill                    # 显示名，默认目录名
description: 做什么+何时用        # Claude 决定是否自动调用
when_to_use: 触发短语             # 追加到 description
disable-model-invocation: true    # 仅用户手动调用
user-invocable: false             # 仅 Claude 调用
allowed-tools: Bash Read          # 预授权工具
context: fork                     # 在子代理中运行
agent: Explore                    # 子代理类型
arguments: [issue, branch]        # 命名参数列表
paths: "src/**/*.py"              # 路径限定
---
```

### 动态上下文注入
```
!`git diff HEAD`          # shell命令输出替换占位符
```!                    # 多行命令块
```
在 Claude 看到之前执行，结果是静态文本注入。

### 上下文成本设计
- description 在会话启动时加载（1,536字符截断）
- 完整 body 仅在被调用时加载
- 子代理预加载 skills 时完整注入
- SKILL.md 建议 <500 行

### 技能生命周期
- 调用后完整内容进入会话，持续存在
- auto-compaction 时保留最近 5000 token
- 可重新调用恢复完整内容

## Subagents 设计

- 独立上下文窗口 + 自定义 system prompt
- 独立工具访问权限
- 可预加载 skills
- 可启用持久记忆
- 前台（等待结果）或后台（异步通知）
- 父会话只收到摘要

### 适用场景
- 读大量文件的调研任务
- 并行多路探索
- 链式子代理（结果传给下一个）
- 当前上下文已满时卸货

## CLAUDE.md 设计

- 建议 <200 行
- @path/to/file 导入其他文件（最深4层）
- .claude/rules/ 路径/文件类型限定规则
- 分层：managed > user > project > local
- AGENTS.md 兼容：@AGENTS.md 导入
- subdirectory CLAUDE.md 按需加载

## MCP 设计

- HTTP/SSE/stdio 三种连接方式
- 本地 scope、project scope、user scope
- 动态工具更新、自动重连
- 可限制 output 上限
- 预授权 OAuth

## Hooks 设计

- 30+ 生命周期事件（SessionStart/PreToolUse/PostToolUse等）
- 4种 handler：command/http/mcp tool/prompt
- 支持 decision control（允许/拒绝/修改）
- 可注入额外上下文
- 作用域：project or user

## 对羽渡尘的启发

1. Skill 上下文成本设计 — 我们已经瘦身
2. disable-model-invocation — 某些羽毛可设仅用户调
3. subagent 预加载 skills — delegate_task 可以加
4. hooks 注入上下文 — 类似 cron 但更精细
5. @import 语法 — 羽毛之间可以互相引用
6. .claude/rules/ 路径限定 — 可为不同目录设不同规则
