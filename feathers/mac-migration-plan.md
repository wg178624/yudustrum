---
title: "mac migration plan"
tags: [reference]
type: reference
---

# MacBook 迁移计划

如果用户从 Windows/WSL 切换到 MacBook，羽渡尘和工具的迁移方案：

## 不受影响的数据（直接拷贝）
- 羽毛文件（`feathers/*.md`）— 纯文本，跨平台
- 向量库（ChromaDB 目录）— 拷贝即可
- 神蕴索引（`shenyun.json`）— 纯 JSON
- Git 版本历史（`.git/`）— 保留
- D 盘教材（13 本 PDF）— 拷贝
- GitHub（eie-learning-lab）— `git clone`
- VPS（ssh）— 照连
- aihot / CF Worker — 全在线服务

## 需要重新配置的
- Hermes Agent 本体 — 当前跑在 WSL 里，Mac 需重装（`pip install hermes-agent`）
- Chrome 共享视野 — Linux Chrome → macOS Chrome，加 `--remote-debugging-port=9222`
- Ollama — Mac 有 native 版，M 芯片有 GPU 加速
- SSH key — 拷贝 `~/.ssh/`
- WSL 别名/代理配置 — Mac 用 zsh，需重写 `.zshrc`

## 最需要规划的
- WSL 整套环境 → Mac 替代方案：Docker Desktop / OrbStack
- WSLg 显示的 Linux 窗口 → Mac 原生窗口

迁移时我可以写一个迁移脚本，一键搞定。
