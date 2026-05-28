# Obsidian 集成参考

## 库路径

Obsidian 库路径：`D:\hermes-workspace`
已在 `.env` 中设为 `OBSIDIAN_VAULT_PATH="/mnt/d/hermes-workspace"`

## 库内的羽渡尘内容

```
D:\hermes-workspace（Obsidian 库）
  └── skills/yudustream/
        ├── feathers/        ← 羽毛（Markdown，Obsidian 图谱自动连线）
        ├── 教材库/           ← 教材 PDF（junction 直通 iCloud，不占额外空间）
        ├── entities/        ← 实体索引（JSON，可查看不可写）
        ├── graph/           ← 135节点图谱
        ├── persona/         ← L3用户画像
        └── ...
```

## 教材库 junction

教材库使用 Windows 目录联接（junction）而非复制：
```
cmd.exe /c "mklink /J D:\hermes-workspace\skills\yudustream\教材库 D:\iCloudDrive\iCloud~md~obsidian\Linux\教材"
```

优势：
- 不占用额外磁盘空间（共19本教材 ~285MB，但链接本身 <1KB）
- 教材本体在 iCloud Drive 中，符合用户"数据脱离C盘独立存活"的备份策略
- Windows/Obsidian 原生识别 junction，无权限问题
- WSL 下通过 `/mnt/d/hermes-workspace/skills/yudustream/教材库/` 可正常访问

## 工作流

1. 用户在 Obsidian 中读写/创建羽毛（`feathers/*.md`）
2. 用户告知"看完了/改完了"
3. 跑羽渡尘管线更新索引：
   ```bash
   python3 /mnt/d/hermes-workspace/scripts/yudustream_entity.py  # 实体提取
   python3 /mnt/d/hermes-workspace/scripts/yudustream_v4.py      # L3画像更新
   cd /mnt/d/hermes-workspace/skills/yudustream && git add -A && git commit -m "💾 Obsidian编辑存盘"
   ```
4. 羽渡尘缓存刷新（下次对话自动触发）

## 注意事项

- Obsidian 只读写 `feathers/` 目录的 Markdown 文件
- `entities/` / `graph/` / `persona/` 是羽渡尘内部数据，不在 Obsidian 中编辑
- 图谱视图：Obsidian Graph View（词共现）≠ 羽渡尘 GraphRAG（135节点算法）。两种图谱可对照查看
