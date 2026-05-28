# MEMORY.md 字符限制与 Hermes 记忆配置

> 2026-05-26 会话中用户发现 `memory.memory_char_limit: 2200` 并询问能否扩容。

## 配置位置

```yaml
# ~/.hermes/config.yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
  memory_char_limit: 2200    # MEMORY.md 最大字符数（含空格和标点）
  user_char_limit: 1375      # USER.md 最大字符数
  provider: ''               # 可选：honcho, mem0 等外部记忆后端
  flush_min_turns: 6         # 最少隔多少轮对话写入一次
  nudge_interval: 10         # 提示用户保存记忆的间隔轮数
```

通过 CLI 修改：
```bash
hermes config set memory.memory_char_limit 4000
hermes config set memory.user_char_limit 2000
```

## 扩容的代价

| 容量 | 额外注入 token/次 | 日均额外开销 | 备注 |
|:----:|:---------------:|:----------:|------|
| 2,200（默认） | 0（基准） | ¥0 | 当前状态 |
| 4,000 | ~+1,800 | ~+¥0.50 | 适合塞更多配置信息 |
| 6,000 | ~+3,800 | ~+¥1.00 | 小心：每次对话都注入更多 |

**关键权衡**：
- 扩容后每次对话多注入 X token → 日均花费微涨（约10%）
- 更大的副作用是：每次改 MEMORY.md → 前缀哈希变 → DeepSeek 缓存 MISS → 预热期多花钱
- 最优策略：MEMORY.md 只存最核心、不频繁改的信息（画像/铁律/配置），细节放羽毛库

## 替代方案（不扩容也够）

1. **压缩现有 2,200 字** — 去掉冗余描述、合并同类项、用短语替代句子
2. **把低频信息移到羽毛库** — 让羽渡尘检索这些信息，而不是全量注入
3. **定期清理过期条目** — 旧配置/已解决项转为羽毛，释放 MEMORY.md 空间

## 相关文件

- `~/.hermes/config.yaml` — 主配置文件
- `~/.hermes/memories/MEMORY.md` — 当前记忆内容
- `~/.hermes/memories/USER.md` — 用户画像内容
