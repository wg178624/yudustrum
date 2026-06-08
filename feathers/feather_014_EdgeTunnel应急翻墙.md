---
title: "EdgeTunnel CF Worker 应急翻墙备用"
brief: "EdgeTunnel CF Worker应急翻墙方案：利用Cloudflare Workers搭建备用代理，适用于VPS故障时的紧急通道。"
tags: [CF Worker, 翻墙, EdgeTunnel, 应急, V2Ray]
type: feather
created: 2026-05-27
summary: "EdgeTunnel 部署指南 — 用 Cloudflare Worker 做应急翻墙通道，V2RayN 挂了时备用"
---

# EdgeTunnel — CF Worker 应急翻墙

## 简介

EdgeTunnel 是一个开源项目，利用 Cloudflare Workers/Pages 的边缘网络（330+ 数据中心）建立代理隧道。当 V2RayN 的 VPS 被封时作为备用通道。

## 部署步骤

### 前提
- 一个 Cloudflare 账号（你已经有，hermes-scraper worker 就在上面）
- 一个域名托管在 Cloudflare（可选，非必需）

### 方式一：Worker 部署（推荐）
1. 登录 Cloudflare Dashboard → Workers & Pages
2. 创建新的 Worker
3. 从 EdgeTunnel 的 GitHub 复制 worker.js 代码
4. 粘贴 → 部署
5. 记下 Worker 地址：`https://你的项目.子域名.workers.dev`

### 方式二：Pages 部署
1. Fork EdgeTunnel 的 GitHub 仓库
2. Cloudflare Dashboard → Workers & Pages → 创建 Pages
3. 连接你的 GitHub 仓库
4. 自动部署

### 客户端配置
部署后得到一个 Worker 地址：
```
https://你的项目.你的子域名.workers.dev
```

在 V2RayN 或其他客户端中配置：
- 地址：Worker 地址
- 端口：443
- 协议：根据 EdgeTunnel 支持的协议（通常是 WebSocket + TLS）

## 注意事项

- 免费 Worker：每天 10 万请求，适合轻量使用
- 看视频/下载大文件会超限
- 仅作应急使用，主力还是 V2RayN + VPS
- 你的 CF Worker 已有一个 scraper，建议新建一个专用的

## 什么时候用

当 V2RayN 连不上时：
1. 浏览器打开你的 EdgeTunnel Worker 地址
2. 配置客户端连接
3. 应急用来看网页/查资料

V2RayN 恢复后切回主力通道。
