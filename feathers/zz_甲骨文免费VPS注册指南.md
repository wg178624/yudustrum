---
title: "甲骨文免费VPS注册指南"
tags: [VPS, 甲骨文, 教程]
type: reference
created: 2026-06-19
retrieval: explicit
---

# 甲骨文 Oracle Cloud 免费 VPS 注册指南

## 免费资源
- ARM Ampere A1：4核 / 24GB RAM / 200GB SSD（自由分配）
- 公网 IPv4 + IPv6
- 10TB/月流量
- 永久免费（不升级就不扣钱）

## 注册前准备
- [ ] 工行星座卡 Visa / 招行万事达（选一张）
- [ ] Gmail 邮箱
- [ ] 国内手机号（收验证码）
- [ ] 信用卡账单地址（吉安那个）

## 注册步骤

### 1. 网络环境（最重要）
- [ ] 断开翻墙（关小火箭）
- [ ] 用 4G 热点直连（不要 VPS）
- [ ] Chrome 开无痕模式
- [ ] 不要开任何 VPN/代理

### 2. 打开官网
```
https://www.oracle.com/cloud/free/
```
点击 "Start for free"

### 3. 填写信息
- [ ] 国家：中国（真实）
- [ ] 姓名：王刚（拼音，跟卡一致）
- [ ] 邮箱：g176245232@gmail.com
- [ ] 密码：设置一个
- [ ] 验证邮箱（收邮件点链接）

### 4. 地址信息
- [ ] 客户类型：Individual
- [ ] 地址填信用卡账单地址（英文或拼音）
- [ ] 手机号：你的国内号
- [ ] 主区域：Phoenix 或 Tokyo（ARM 配额更多）

### 5. 信用卡验证
- [ ] 输入卡号 / 有效期 / CVV
- [ ] 不会扣钱（仅预授权验证）
- [ ] 验证成功继续，失败等 24 小时再试

### 6. 等待开通
- [ ] 10分钟 - 2小时
- [ ] 收到 "Welcome to Oracle Cloud" 邮件 = 成功

## 创建实例
- [ ] 登录 https://cloud.oracle.com
- [ ] Compute → Instances → Create Instance
- [ ] 选 Ubuntu 22.04/24.04
- [ ] Shape：Ampere ARM（确认有 "Always Free Eligible" 标签）
- [ ] 配置：2核 + 12GB 或 4核 + 24GB
- [ ] SSH 密钥：生成并下载保存
- [ ] 创建完成

## 注意事项
- 失败别灰心，甲骨文注册是玄学
- 不要频繁尝试（等 24 小时）
- 长期闲置可能被回收
- 建议跑个服务保活（翻墙/羽渡尘/监控）
