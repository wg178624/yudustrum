---
title: "CF Worker 反代爬虫方案"
tags: [reference]
type: reference
---

# CF Worker 代理爬虫模式

用户拥有一个 Cloudflare Worker 部署在 `hermes-scraper.g1786245232.workers.dev`，可以绕过目标网站对 WSL IP 的封锁。

## 用法

```bash
# 代理 GET 请求
curl -sL "https://hermes-scraper.g1786245232.workers.dev/?url=https://目标网站.com/路径" \
  -A "Mozilla/5.0" \
  -o output.file
```

## 适用场景

- Libgen 下载学术书籍/论文（绕过 bot 检测）
- Google/Bing 搜索（绕过 CAPTCHA）
- 任何对 WSL 原生 IP 做限制的站点

## 已验证（2026-05-27）

- Libgen.li 搜索：HTTP 200 ✅（51535 bytes）
- Libgen.li 图书详情页：HTTP 200 ✅
- Libgen get.php + key 直接下载 PDF：HTTP 200 ✅（13MB PDF）

## 注意事项

- 大文件下载（>50MB）可能触发 CF Worker 超时（免费计划 30s 限制）
- 不能用于流媒体/视频
- 仅供个人学术用途
