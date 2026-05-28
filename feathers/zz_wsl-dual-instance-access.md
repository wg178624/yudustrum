---
title: "wsl dual instance access"
tags: [reference]
type: reference
---

# WSL 双实例访问

## 场景

用户有 2 个 WSL 实例：
- Debian 13（主力，Hermes/羽渡尘/Chrome headless）
- Ubuntu（实验场，测试危险操作/编译/试包）

## 访问方式

### ① 命令行远程执行（需目标实例运行中）

```bash
wsl.exe -d Ubuntu -- bash -c "命令"
```

从当前实例向另一实例发命令、拿回结果。

### ② 文件系统直读（目标停止也能访问）

```
\\wsl.localhost\Ubuntu\home\用户名\
```

Windows 文件管理器直接打开，不需要目标实例启动。

### ③ 网络互通（两个都在跑时）

```
Debian IP  ← 虚拟交换机 →  Ubuntu IP（如 172.24.57.x）
```

可 SSH、curl、scp、ping。

## 用途

- 用户在 Ubuntu 试了某个包/工具，让我过去看日志、debug
- 编译炸了，让我远程诊断
- 试成功了，把配置搬到 Debian 这边来

## 注意事项

- **不要擅自启动 Ubuntu** — Ubuntu 是用户的实验场，D 盘根目录。启动前问一声。
- `wsl.exe -d Ubuntu -- 命令` 不需要 Ubuntu 前台运行，WSL 后台自动唤醒。
