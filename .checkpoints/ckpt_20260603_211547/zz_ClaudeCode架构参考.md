---
title: "Claude Code 架构参考"
tags: [reference]
type: reference
---

# Claude Code 扩展体系设计参考

来源：https://code.claude.com/docs/en/
日期：2026-05-27

## 五大扩展机制

| 机制 | 作用 | 何时加 | 上下文成本 |
|------|------|--------|-----------|
| CLAUDE.md | 持久上下文, 每次会话自动加载 | 同规则错两次 | 全量, 每请求 |
| Skills | 可复用知识/流程, 按需加载 | 第3次粘贴同一流程 | description低, body仅调用时 |
| Subagents | 隔离上下文只返回摘要 | 侧任务刷屏主上下文 | 独立窗口 |
| MCP | 连接外部工具/数据库/API | 频繁从浏览器贴数据 | 低, 工具调用时才加载 |
| Hooks | 生命周期自动化(30+事件) | 每次文件编辑后自动触发 | 零(外部执行) |

## Skills 关键设计

- description: 1536字符截断。尾缀when_to_use
- disable-model-invocation: true → 仅用户手动/xxx调用
- user-invocable: false → 仅Claude自动调用
- allowed-tools: 预授权工具列表
- context: fork → 在子代理中运行
- !`command` 动态上下文注入(预处理, Claude看到的是结果)
- SKILL.md < 500行, 详参放同目录子文件

## CLAUDE.md 关键设计

- < 200行
- @path 导入其他文件(最深层4层)
- .claude/rules/ 路径/文件类型限定
- 分层: managed > user > project > local(CLAUDE.local.md)
- AGENTS.md 兼容: @AGENTS.md 导入
- subdirectory CLAUDE.md 按需加载
- Auto memory: Claude自写笔记, 200行/25KB限制

## Subagents 关键设计

- 独立上下文窗口 + 自定义system prompt
- 独立工具访问权限
- 可预加载skills
- 可持久记忆
- 前台(等待)或后台(异步)
- 链式子代理(结果→下一个)
- 自动委派: Claude根据description自动决定何时用

## MCP 关键设计

- HTTP/SSE/stdio三种连接
- scope: project > user
- 动态工具更新 + 自动重连
- output限流可配置

## Hooks 关键设计(30+事件)

- SessionStart / PreToolUse / PostToolUse / UserPromptSubmit / Stop 等
- 4种handler: command/http/mcp/prompt/agent
- decision control: allow/deny/modify
- 可注入额外上下文
- 可异步运行

## 对羽渡尘的改进

已实施：
1. SKILL.md瘦身: 17K→1.6K tokens ✅
2. retrieval: explicit frontmatter ✅
3. subagent预加载约定 ✅
4. summary标准化 ✅

待实施：
- bootstrap加前置检索hook(PreToolUse类似)
- !`command` 动态注入模式(回答前自动查羽渡尘)
