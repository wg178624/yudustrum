var STATUS = {
  "feathers": 57,
  "entities": 1828,
  "l3_facts": 164,
  "health_score": 76,
  "git_commits": 95,
  "disk_free_gb": 452,
  "ghosts": 0,
  "textbooks": 21,
  "feather_list": [
    "DASHBOARD.md",
    "README.md",
    "architecture-real-state.md",
    "cache-alignment-filter.md",
    "cf-worker-scraping.md",
    "claude-code-architecture.md",
    "control-theory-audit.md",
    "database-backend.md",
    "deep-learning-activation.md",
    "deepseek-cache-mechanics.md",
    "feather_001_20260504_会话复盘.md",
    "feather_002_工具使用手册.md",
    "feather_003_EIE完整培养方案与书单.md",
    "feather_004_本地技能包迭代全览.md",
    "feather_005_大家伙配置讨论_5月26日.md",
    "feather_006_华为韬定律.md",
    "feather_007_羽渡尘脑图总览.md",
    "feather_008_工程控制论入库.md",
    "feather_009_ClaudeCode扩展体系笔记.md",
    "feather_010_马来西亚半导体NIMP2030.md",
    "feather_011_教材库学习路线图.md",
    "feather_012_csdiy自学指南.md",
    "feather_013_收藏夹薅下来计划.md",
    "feather_014_比特币白皮书.md",
    "feather_015_VLESS_Reality_VPN教程.md",
    "feather_016_EdgeTunnel_应急翻墙.md",
    "feather_017_GoogleAntigravity入门教程.md",
    "feather_018_DeepSeekKV缓存官方确认.md",
    "feather_019_3Blue1Brown可视化教程资源索引.md",
    "feather_020_符华传记·云墨丹心-赤鸢仙人五万年.md",
    "feather_021_教材更新日志-2026-05-08-高数与概率论.md",
    "feather_022_用户设备清单.md",
    "feather_023_羽渡尘完全体v5.9.md",
    "feather_024_存盘历史.md",
    "mac-migration-plan.md",
    "memory-char-limit-and-config.md",
    "memory-hierarchy-explained.md",
    "memory-systems-comparison-v4.md",
    "memory-systems-implementation.md",
    "memory-systems-research.md",
    "memory-vs-user-vs-l3.md",
    "mindnode-opml-export.md",
    "obsidian-integration.md",
    "ref_c_file_ops.md",
    "ref_c_malloc_free.md",
    "ref_c_pointers_sizeof.md",
    "ref_c_printf_scanf.md",
    "ref_c_string_ops.md",
    "retrieve-cite-checklist.md",
    "semia-skill-security-audit.md",
    "tencentdb-agent-memory.md",
    "v5-design-decisions.md",
    "v5-functionality-audit.md",
    "vector-db-setup.md",
    "vscode-workspace-setup.md",
    "wsl-dual-instance-access.md",
    "wsl-dual-instance.md"
  ],
  "ghost_list": [],
  "version": "5.9.0",
  "last_update": "2026-05-28 20:08:10",
  "audit_layers": {
    "结构完整": {
      "score": 25,
      "max": 25,
      "alerts": []
    },
    "行为基线": {
      "score": 15,
      "max": 25,
      "alerts": [
        "实体 1828 (基线 900-1200) → ⚠️ 偏离基线",
        "L3 164 条 (基线 60-100) → ⚠️ 偏离基线"
      ]
    },
    "交叉一致": {
      "score": 9,
      "max": 20,
      "alerts": [
        "7 磁盘有但索引无",
        "39 索引有但磁盘无",
        "实体与L3画像引用偏少"
      ]
    },
    "趋势分析": {
      "score": 15,
      "max": 15,
      "alerts": []
    },
    "自愈修复": {
      "score": 12,
      "max": 15,
      "alerts": [
        "无定时审计 → 问题不会自动发现"
      ]
    }
  }
};
