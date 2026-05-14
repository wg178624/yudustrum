---
title: 工具使用手册
tags: [工具, CodeX, Chrome, OpenClaw, Ollama, NVIDIA, Obsidian]
created: 2026-05-04T20:35:00+08:00
type: feather
---

# 🪶 第2片羽毛 · 工具使用手册

## CodeX (编码代理)
- **位置:** VS Code 扩展 `/mnt/c/Users/j'g'f'd/.vscode/extensions/openai.chatgpt-*/bin/windows-x86_64/codex.exe`
- **MCP Server:** 已接入 Hermes 配置
- **执行:** `CODEX_PATH="..." && "$CODEX_PATH" exec --yolo "任务"`
- **认证:** `codex login --device-auth` → 浏览器输码
- **注意:** token 过期就重登，`--yolo` 绕沙箱

## Chrome (真身浏览器)
- **位置:** `/mnt/c/Users/j'g'f'd/AppData/Local/Google/Chrome/Application/chrome.exe`
- **用法:** `chrome.exe --headless --disable-gpu --no-sandbox --dump-dom <url>`
- **优势:** 有用户登录态，能过 Cloudflare 反爬
- **用户数据:** `C:\Users\j'g'f'd\AppData\Local\Google\Chrome\User Data`

## OpenClaw (AI助手邻居)
- **位置:** WSL `/root/.nvm/versions/node/v22.22.1/bin/openclaw`
- **版本:** 2026.5.4 (刚更新)
- **配置:** D 盘 `/mnt/d/hermes-workspace/configs/openclaw/`
- **Gateway端口:** 18789
- **更新:** `npm install -g openclaw@latest`

## Ollama (本地模型)
- **模型路径:** `/mnt/d/WSL/ollama_models` (D 盘)
- **GPU:** RTX 4070 直通 (8GB 显存)
- **可用模型:**
  - qwen3.5:9b (主力，6.6GB ✅ GPU)
  - qwen2.5vl:7b (视觉，6GB ✅ GPU)
  - gemma4:26b (17GB ❌ 显存不够)
  - qwen3-coder:30b (18GB ❌ 显存不够)
  - gpt-oss:20b (13GB ❌ 显存不够)
- **API端点:** `http://127.0.0.1:11434/v1`

## NVIDIA NIM (云端模型)
- **API端点:** `https://integrate.api.nvidia.com/v1`
- **API Key:** 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
- **可用模型:**
  - deepseek-ai/deepseek-v4-flash (主要)
  - meta/llama-4-maverick-17b-128e-instruct
  - qwen/qwen3-coder-480b-a35b-instruct
  - mistralai/mistral-large

## Obsidian (笔记)
- **仓库:** `/mnt/d/iCloudDrive/iCloud~md~obsidian/`
- **有毕设大纲:** PMIC 鲁棒性对比 (麒麟990 vs A16)
- **有教材:** 数电/模电/操作系统/计组 PDF
