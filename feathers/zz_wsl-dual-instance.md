---
title: "WSL 双实例（Debian+Ubuntu）方案"
tags: [reference]
type: reference
---

# WSL 双实例访问参考

## 环境概述

用户有两台 WSL 实例：
- **Debian 13**（主力）：Hermes Agent 运行环境，日常开发/羽渡尘管线
- **Ubuntu**（实验场）：安装后未常开，用于测试可能搞炸系统的操作

## WSL 实例间通讯方式

### 1. 跨实例命令执行（Ubuntu 需运行中）

```bash
wsl.exe -d Ubuntu -- bash -c "命令"
```

从 Debian 向 Ubuntu 发送命令并取回结果。Ubuntu 停止状态时可启动，但需要用户授权。

### 2. 文件系统访问（Ubuntu 停止状态也可读）

```
\\wsl.localhost\Ubuntu\home\<用户名>\
```

通过 `/mnt/` 路径也可在 WSL Debian 中访问：
```
# Ubuntu 运行后可通过网络 IP 访问
UBUNTU_IP=$(wsl.exe -d Ubuntu -- hostname -I 2>/dev/null | tr -d '\r' | awk '{print $1}')
ping $UBUNTU_IP  # ICMP 互通
```

### 3. 虚拟网络互通（两个实例均运行中）

WSL2 实例在同一个虚拟交换机上，各分配独立 IP：
- Debian 13：172.24.56.x/20
- Ubuntu：172.24.57.254/20

可 SSH / curl / scp 互访。

## 典型使用场景

1. **实验隔离**：在 Ubuntu 上试装危险包/改系统配置，搞炸了 `wsl --terminate Ubuntu` 重置
2. **远程诊断**：Ubuntu 上编译/运行出错，从 Debian 远程进去查日志
3. **配置迁移**：Ubuntu 上试成功的配置，复制到 Debian 做正式环境
