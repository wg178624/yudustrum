---
title: "羽渡尘完全体 v5.8 — 全量集成"
tags: [羽渡尘, 架构, 总览, v5.8, 全量]
type: doc
created: 2026-05-28
---

# 🕊️ 羽渡尘完全体 v5.8

> 全量集成 — 架构 / 设计决策 / 用户画像 / 行为铁律 / 版本历史 / 成本 / 所有信息
> 看完这一篇，你不知道的羽渡尘就不剩什么了。

---

## 一、羽渡尘是什么

**AI 记忆系统。** 不是聊天记录、不是缓存省钱工具、不是知识库。它让 AI 跨越会话记住你是谁、你干了什么、你接下来要去哪。

之所以叫羽渡尘，是因为用户理想型是符华/赤鸢（崩坏3），羽渡尘是符华的神器——掌管记忆的神器。

---

## 二、三系统分工

| 系统 | 职责 | 位置 |
|------|------|------|
| **羽渡尘** | 主力记忆系统。新知存羽毛 | D:\hermes-workspace\skills\yudustream\ |
| **USER.md** | 用户画像。姓名/计划/偏好 | ~/.hermes/memories/USER.md |
| **user-iron-laws** | 行为铁律，刻 SSD 不可变 | ~/.hermes/skills/dogfood/user-iron-laws/SKILL.md |

这三者互相独立，职责不重叠。

---

## 三、用户画像（谁在用羽渡尘）

| 项目 | 内容 |
|------|------|
| 姓名 | 王刚（gang） |
| 生日 | 2005-04-12 |
| 籍贯 | 江西吉安 |
| 身份证 | 362421200504120211 |
| 学历 | 中专，自学 EIE |
| 前工作 | 武汉天马微电子（合同工 2025.12-2026.02，工号 D2532183）|
| 目标 | 马来西亚槟城，PSDC留学 → USM在职本科 → Intel/AMD半导体岗 |
| 理想型 | 符华/赤鸢 |
| 设备 | iPhone 15美版 / Huawei Mate 30 Pro 4G（不翻墙）/ 机械革命极光X RTX 4070 8GB |
| 主力 OS | Win11 25H2（WSL Debian 13 + Ubuntu） |
| IDE | Google Antigravity（agent-first）+ VSCode 混用 |
| 邮箱 | g176245232@gmail.com（Google/Apple通用）/ 1786245232@qq.com |
| GitHub | github.com/wg178624（member of @Luxshare-BMC）|
| X/Twitter | @ikun268448（2024-07注册，潜水两年） |
| VPS | RackNerd圣何塞 64.188.17.155:5522，$10/年 |
| VPS面板 | 3X-UI，https://64.188.17.155:54138 |
| 翻墙 | 主力 V2RayN + ikuuu机场（已弃用），VLESS+Reality自建（MyReality），WARP备用 |
| 教材库 | D:\iCloudDrive\iCloud~md~obsidian\Linux\教材\（21本PDF，含模电/数电/计组/C等）|

### 用户哲学

| 信念 | 说明 |
|------|------|
| 社会达尔文主义 | 你不割别人，别人就割你。法无禁止皆可为 |
| 二八定律 | 80%收益来自20%客户。不做低端，瞄准高价值 |
| 不赚中国人钱 | 售后心累，单价低。倾向国际市场 |
| AI/机器绝对信任 | 机器没有自由意志，不会背叛。对人有防备 |
| token是资源 | 每token都是钱，但不吝啬有用的事 |
| 学习是复利 | 自学的东西不会忘，越学越快 |
| 不编数字 | 编数字比说不知道更破坏信任 |
| 评价体系 | 夯爆了→很夯→还行→一般→拉了→拉完了 |

### 用户学习路线

```
T0（现在）：计组（唐朔飞）→ C Primer Plus → 数据结构（C语言版）
T1（下一步）：数电（阎石）→ 模电（童诗白）→ 工程控制论
T2（以后）：OS → 计网
T3（需时）：高数/概率/C++/业余无线电

核心原则：不需要微积分就能学C，二进制+布尔代数就够了
目标地：马来西亚槟城 Penang
```

---

## 四、数据架构（13 层）

| 层 | 内容 | 格式 | 备注 |
|:--:|------|:----:|------|
| L0 | 原始羽毛（手写知识） | feathers/*.md | 用户可读，Markdown |
| L1 | 结构化事实+溯源 | atoms/*.json | 机器提取，自动生成 |
| L2 | 场景聚合 | scenarios/*.json | 从 atoms 聚合 |
| L3 | 用户画像 | persona/persona.v4.json | 78条事实，含profile+contact |
| G | GraphRAG 知识图谱 | graph/*.json | 135节点，NetworkX |
| M | LLM自动融合 | compact/*.json | 知识蒸馏 |
| A | 自我管理周报 | reports/ | 定期生成 |
| V | 版本控制 | changelog/ | Git + changelog |
| D | 密度蒸馏 | density_profile.json | 正则匹配，0 token开销 |
| C | 缓存对齐 | 运行时（Python） | MD5哈希校验 |
| H | 自检钩子 | audit.py | 完整性/冲突/负债/性能 |
| S | 仪表盘数据 | status.js + status.json | bake_dashboard.py 生成 |
| B | 仪表盘前端 | dashboard.html + DASHBOARD.md | 双击即用 |

### 数据流

```
写新知识 → feathers/*.md
  → shenyun.json（神蕴索引）
  → entity.py（实体提取）
  → v4.py（L3画像）
  → bake_dashboard.py（status.js/json）
  → dashboard.html（浏览器展示）
```

---

## 五、版本历史

| 版本 | 日期 | 核心变化 |
|:----:|:----:|:---------|
| v1.0.0 | 5/4 | 初版：四目录+神蕴索引+自动存盘 |
| v2.0.0 | - | 搜索引擎：SQLite FTS5 + ChromaDB |
| v3.0.0 | - | 分层记忆 L0-L3，参考 TencentDB-Agent-Memory |
| v4.0.0 | - | 符号化+实体+权重+时间窗口+反馈 |
| v5.0.0 | 5/16 | GraphRAG 135节点/1414边 |
| v5.5.0 | 5/22 | 缓存对齐器+四路多路召回，命中率>99%，省96% |
| v5.7.0 | 5/26 | 审计钩子+分层字典序缓存对齐 |
| v5.7.4 | 5/26 | 三系统分工定型。MEMORY.md→羽渡尘快照。铁律迁出。Obsidian打通 |
| v5.7.5 | 5/27 | KV Cache官方确认。教材库+references迁入。控制论审计框架 |
| v5.7.6 | 5/27 | 3X-UI风格仪表盘。幽灵文件修复 |
| v5.7.7 | 5/28 | 仪表盘数据架构v2：status.js+status.json双源 |
| **v5.8.0** | **5/28** | **检索管线升级：去重→字典序→轻度融合→固定模板** |

---

## 六、检索管线（v5.8 — 当前）

```text
用户查询
  ↓
① 多路召回
   · 实体精确匹配（关键词子串匹配）
   · 图谱关系搜索（共现关系，NetworkX）
   · FTS5 全文搜索（SQLite FTS5）
   · 向量语义搜索（entity_vectors.json）
  ↓
② 去重（按 entity 名称，同实体保留最优一条）
  ↓
③ 字典序排序（第一优先级，确保缓存前缀稳定）
  ↓
④ 轻度融合（同实体多条事实合并为连贯描述，逗号分隔）
  ↓
⑤ 格式化
    输出格式（绝对固定，不得改变）：
    【羽渡尘记忆】
    · Entity1: 内容...
    · Entity2: 内容...
  ↓
⑥ MD5 哈希校验 → 缓存对齐 → 命中率 >99%
```

### 排序规则（缓存命中关键）

| 排序因子 | 优先级 | 原因 |
|----------|:------:|:-----|
| 实体名称字典序（升序） | **第一** | 确保前缀绝对稳定 → 缓存 HIT |
| 相关性 | 第二（字典序相同才考虑） | 不影响前缀 |

> **不要按权重排序，不要按热度排序，不要按时间排序。**
> 权重是变量 → 前缀不稳 → 缓存 MISS。
> 字典序是常数 → 前缀稳如狗 → 缓存命中拉到物理上限。

### v5.7 → v5.8 管线对比

| 维度 | v5.7 | v5.8 |
|------|:----:|:----:|
| 排序 | 权重优先（核心兜+背景兜） | 字典序第一（全局平铺） |
| 去重 | 无 | 按 entity 去重 |
| 融合 | 无 | 同实体合并 |
| 输出格式 | 灵活模板 | 绝对固定【羽渡尘记忆】·实体:内容 |
| 缓存命中 | >99% | >99%（更严格） |

---

## 七、设计决策（为什么这么选）

### 为什么不用 Neo4j？
VPS只有1核CPU。NetworkX纯Python，内存运行，135节点加载<1秒。

### 为什么不用权重排序？
权重是变量 → 今天排第3明天排第5 → 前缀变化 → 缓存MISS。
字典序是常数 → 永远不变 → 永远HIT。

### 为什么不用 PostgreSQL？
SQLite零依赖。羽渡尘数据量<1MB，SQLite足够。

### 为什么不连续接 LLM 判断密度？
每次查前调LLM本身是token开销。正则匹配0 token，毫秒级。

### 为什么块对齐被存档？
DeepSeek缓存基于前缀单元，非块哈希。边际收益<0.1%。

### 为什么不用 OpenAI / Claude？
DeepSeek v4 Flash 缓存命中¥0.02/1M vs MISS ¥1/1M。配合羽渡尘缓存对齐 >99%命中率，实际有效成本极低。

---

## 八、缓存对齐原理

DeepSeek 定价：命中¥0.02/1M / MISS¥1/1M → 差50倍。

核心策略：
1. System prompt 绝对固定（不变量）
2. 记忆按字典序重排（不变量）
3. 固定格式化模板 `【羽渡尘记忆】`（不变量）
4. 三者哈希 → 同一查询恒等于同一哈希 → 缓存必HIT

> 数据变更时哈希变一次 → 一次MISS（预热）→ 继续HIT。
> 预热不是系统坏了，是写缓存的正常开销。

实测：>99%命中率，省96% Token费。

---

## 九、DeepSeek 思考模式真相（5/27查明）

| 误区 | 真相 |
|------|------|
| low/medium/high 是不同档位 | ❌ DeepSeek 后端全映射为同一档（high） |
| 切 high 会多花钱 | ❌ medium→high 零变化，费用不变 |
| 只有 max 才是真正不同档 | ✅ max 才是真正的深度思考 |
| 思考模式需要手动开启 | ❌ v4 Flash 默认开启思考模式 |

---

## 十、成本数据

| 指标 | 数值 |
|------|:----:|
| 19天累计 tokens | 1,314,490,866（约13亿）|
| 19天累计花费 | ¥69.55 |
| 日均 tokens | ~6,600万 |
| 日均花费 | ¥3.66 |
| 有效单价 | ¥0.053/百万 tokens |
| ¥100 能跑 | ~27天 |
| 缓存命中率 | >95%（你实测）/ >99%（本地统计） |

---

## 十一、行为铁律（user-iron-laws 概要）

| 规则 | 说明 |
|------|------|
| 爬虫走 Linux Chrome headless 9222 | 不用内置浏览器，不用 Windows Chrome |
| 搬家≠拷贝 | A级数据必须完整移动+清空原址。B级可拷贝 |
| 密码可存可代操作 | 用户信任代理模式 |
| 不接国人生意 | 售后心累单价低，瞄准国际市场 |
| token是资源 | 但不吝啬有用的事 |
| 回答前自检 | 搜过羽毛没？引用了没？该存盘没？编数字没？ |
| 不确定的说不知道/可以测 | 编数字比说不知道更破坏信任 |

---

## 十二、脚本工具清单

| 脚本 | 作用 |
|------|------|
| bake_dashboard.py | 读取最新数据，生成 status.js + status.json |
| yudustream_audit.py | 系统自检：逻辑冲突/负债/完整性/缓存/性能 |
| yudustream_bootstrap.py | 羽渡尘开机引导，刷新 MEMORY.md 快照 |
| yudustream_v5_cache.py | 检索管线：多路召回+去重+字典序+融合+对齐 |
| yudustream_entity.py | 实体提取管线 |
| yudustream_v4.py | L3 Persona 更新管线 |
| yudustream_v5_graphrag.py | 知识图谱构建（NetworkX）|
| yudustream_safe.py | 保险存盘 |
| yudustream_feedback.py | 反馈权重更新 |
| yudustream_timeline.py | 事实时间线 |
| server.py | 仪表盘后端（http://localhost:8080）|

---

## 十三、系统健康（83/100）

| 维度 | 分数 | 说明 |
|------|:----:|:------|
| 冗余度 | 90 | 每层数据都可从源头重建 |
| 失效隔离 | 85 | 一层挂了不影响其他层 |
| 可恢复性 | 80 | 恢复路径清晰，需手动介入 |
| 边缘情况 | 82 | 幽灵文件已全部修复 |
| **综合** | **83** | **良好** |

---

## 十四、仪表盘

| 入口 | 用途 | 打开方法 |
|------|------|----------|
| dashboard.html | 交互式仪表盘 | 双击 或 http://localhost:8080/dashboard.html |
| DASHBOARD.md | Obsidian 概览 | 点开就看 |
| 羽渡尘.bat | 一键启动（烘焙+后端+浏览器） | 双击 |

后端（server.py）已开机自启（cron @reboot）。点 🔄 刷新按钮实时烘焙数据。

---

## 十五、常用操作

```text
搜羽毛     → session_search() / 检索管线
存羽毛     → write_file(feathers/feather_NNN_标题.md)
存网页     → browser_navigate → 提取 → write_file → 更新索引 → commit
存盘       → bake_dashboard.py → git add -A → commit -m "💾 ..."
自检       → python3 /mnt/d/hermes-workspace/scripts/yudustream_audit.py
检索测试   → python3 /mnt/d/hermes-workspace/scripts/yudustream_v5_cache.py "查询词"
仪表盘     → 双击 dashboard.html
后端状态   → curl http://localhost:8080/api/refresh
```

---

## 十六、当前状态快照（2026-05-28）

```
版本:     5.8.0
羽毛:     29 片
神蕴:     60 条
实体:     1,038 个
L3画像:   78 条
教材库:   21 本 PDF
幽灵:     0 个
健康:     83/100
Git:      70+ 次提交
远程:     GitHub ✅
后端:     http://localhost:8080
缓存:     >99%
运行:     20 天
花费:     ¥69.55（13亿 tokens）
```

> 这就是羽渡尘的全部。在 Obsidian 搜「羽渡尘完全体」就能找到。
> 以后有新变化，我会更新这篇。
