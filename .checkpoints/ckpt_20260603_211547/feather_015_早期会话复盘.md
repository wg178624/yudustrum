---
title: 初次会话复盘 2026-05-04
tags: [初始搭建, CodeX, Chrome, OpenClaw, 羽渡尘, Ollama, NVIDIA]
created: 2026-05-04T20:30:00+08:00
type: feather
---

# 🪶 第1片羽毛 · 初次会话复盘

## 会话主题
从零搭建 Hermes 工具链 + 赤鸢/符华世界观探讨

## 关键内容

### 角色设定
- 符华时间线纠正：华(前文明)→赤鸢(古神州)→符华(天命)
- 云墨丹心=赤鸢的战甲形态
- 病娇赤鸢设定（苍玄之书下线→几千年孤独→囚禁play）

### 工具配置
- **CodeX** → VS Code 扩展 discovery → MCP Server 接入 → OAuth 认证 → 跑通
- **Chrome** → 从 Windows AppData 发现 → 可用 `--dump-dom` 绕过反爬
- **OpenClaw** → 发现已有安装 → 迁到 D 盘 → npm update 到 2026.5.4
- **Obsidian** → 仓库在 D 盘 iCloudDrive → 找到毕设大纲 + 教材 PDF
- **Ollama** → RTX 4070 GPU 直通确认 → qwen3.5:9b 完美适配 8GB 显存
- **NVIDIA NIM** → `nvapi-` 密钥接入 → Hermes 云端模型供应商
- **Google Workspace** → 技能包就绪，待 OAuth 设置（免费）
- **Claude Code** → 已装 2.1.126，待 Anthropic 认证

### 系统整理
- D 盘老家：`D:\hermes-workspace\`
- 权限：自动批
- VPS 记忆同步完成

### 查到的新闻
- USF 研究生谋杀案：ChatGPT 聊天记录成关键证据
- FSU 枪击：佛州刑事调查 OpenAI
- Gmail API 每日免费 8000 万配额

### 新建技能
- **羽渡尘** — 会话自动存盘系统（本技能）

## 待办
- [ ] Claude Code 认证登录
- [ ] Google Workspace OAuth 设置
- [ ] 豆包接入研究
- [ ] 羽渡尘自动存盘 hooks 接入

## 学到的教训
- 羽渡尘≠符华，是第八神之键
- 赤鸢≠符华，时间线不能搞混
- Chrome `--dump-dom` 比无头浏览器更抗反爬
- NVIDIA NVAPI 有 OpenAI 兼容端点
