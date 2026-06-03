---
title: "检索引用检查清单"
tags: [reference]
type: reference
---

# 检索与引用快速清单

当用户提出技术/工程/毕设/工具问题时，按此清单执行：

## 检索步骤

```bash
YUYU="/mnt/d/hermes-workspace/skills/yudustream"
ICLOUD="/mnt/d/iCloudDrive"

# 1. 搜羽毛关键词
grep -ril "关键词" "$YUYU/feathers/" 2>/dev/null
grep -ril "关键词" "$YUYU/auto-save/" --include="SESSION_*" 2>/dev/null

# 2. 查神蕴索引标签
python3 -c "
import json
idx = json.load(open('$YUYU/shenyun.json'))
for f in idx['feathers']:
    print(f['id'], f['title'], f['tags'])
"

# 3. 搜 iCloud 笔记
grep -ril "关键词" "$ICLOUD/iCloud~md~obsidian/Linux/" --include="*.md" 2>/dev/null
ls "$ICLOUD/iCloud~md~obsidian/Linux/" 2>/dev/null | grep -i "关键词"
```

## 引用格式

### 找到羽毛
> 📖 参考：🪶 `feather_编号`「羽毛标题」

### 找到 iCloud 资料
> 📖 参考：☁️ `iCloud路径/文件名`

### 都没找到，回答末尾加
> 💡 这条信息还没有收入羽毛库，要不要我记下来？

## 快速自检（每次回答后）

- [ ] 问了技术/毕设/工具问题？
- [ ] 检索了羽毛库？
- [ ] 找到了 → 引用了？
- [ ] 没找到 → 建议存了？
