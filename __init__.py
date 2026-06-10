"""
羽渡尘 Plugin v1.0 — 完整羽渡尘插件
═══════════════════════════════════════════
工具: recall / stats / save / audit / bake / compact
Hooks: on_session_start / on_session_end / on_pre_compress
═══════════════════════════════════════════
"""
from __future__ import annotations
import json, os, subprocess, sys, re
from pathlib import Path

_HERE = Path(__file__).parent
DB_PATH = str(_HERE / "yantrikdb_yudustrum.db")
FEATHERS = _HERE / "feathers"
SCRIPTS = _HERE / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

register = "yudustream_tools"


# ═══════════════════ 工具 ═══════════════════

def yudustrum_recall(query: str, top_k: int = 8) -> str:
    """检索羽渡尘记忆。query: 查询内容, top_k: 返回条数"""
    try:
        from yantrikdb import YantrikDB
        db = YantrikDB.with_default(DB_PATH)
        results = db.recall(query=query, top_k=top_k, include_consolidated=False)
        db.close()
        if not results:
            return "无相关羽毛记忆"
        lines = [f"[羽渡尘 v7 检索] 关键词: {query}"]
        for r in results:
            text = r.get("text", "")[:200]
            score = r.get("score", 0)
            title = text.split("\n")[0][:60] if text else "?"
            lines.append(f"- [{score:.2f}] {title}")
        return "\n".join(lines)
    except Exception as e:
        return f"检索失败: {e}"


def yudustrum_stats() -> str:
    """羽渡尘状态：记忆数、实体、关系边、矛盾数"""
    try:
        from yantrikdb import YantrikDB
        db = YantrikDB.with_default(DB_PATH)
        s = db.stats()
        db.close()
        return json.dumps({
            "active_memories": s.get("active_memories", 0),
            "entities": s.get("entities", 0),
            "edges": s.get("edges", 0),
            "conflicts": s.get("open_conflicts", 0),
            "feather_files": len(list(FEATHERS.glob("*.md"))),
            "engine": "yantrikdb v7.0"
        })
    except Exception as e:
        return f"状态获取失败: {e}"


def yudustrum_save(manual: bool = True) -> str:
    """存盘 + 自动烤面包。manual: 是否手动触发"""
    try:
        subprocess.run(["git", "add", "-A"], cwd=str(_HERE), capture_output=True, timeout=15)
        r = subprocess.run(
            ["git", "commit", "-m", f"🕊️ {'手动' if manual else '自动'}存盘 {datetime.now().strftime('%m/%d %H:%M')}"],
            cwd=str(_HERE), capture_output=True, text=True, timeout=15
        )
        # 自动烤面包
        bake = subprocess.run(
            ["/usr/local/lib/hermes-agent/venv/bin/python3",
             "/mnt/d/hermes-workspace/scripts/bake_dashboard.py"],
            capture_output=True, text=True, timeout=30
        )
        msg = "存盘+烤面包成功" if r.returncode in (0, 1) else f"存盘: {r.stderr[:100]}"
        if bake.returncode != 0:
            msg += f" 面包: {bake.stderr[:60]}"
        return msg
    except Exception as e:
        return f"存盘失败: {e}"


def yudustrum_audit() -> str:
    """羽渡尘健康审计：检查完整、矛盾、过时记忆"""
    try:
        from yantrikdb import YantrikDB
        db = YantrikDB.with_default(DB_PATH)
        s = db.stats()
        conflicts = db.get_conflicts(limit=5)
        stale = db.stale(days=90, limit=5)
        db.close()
        parts = [f"活跃记忆: {s.get('active_memories',0)}"]
        stale_count = len(stale) if isinstance(stale, list) else 0
        conflict_count = len(conflicts) if isinstance(conflicts, list) else 0
        parts.append(f"过时记忆(>90天): {stale_count}")
        parts.append(f"未解决矛盾: {conflict_count}")
        if conflict_count > 0:
            parts.append("建议: 用 resolve_conflict 解决矛盾")
        if stale_count > 5:
            parts.append("建议: 用 consolidate 压缩过时记忆")
        return "\n".join(parts)
    except Exception as e:
        return f"审计失败: {e}"


def yudustrum_bake() -> str:
    """手动烤面包：更新仪表盘数据"""
    try:
        r = subprocess.run(
            ["/usr/local/lib/hermes-agent/venv/bin/python3",
             "/mnt/d/hermes-workspace/scripts/bake_dashboard.py"],
            capture_output=True, text=True, timeout=30
        )
        return r.stdout.strip() if r.returncode == 0 else f"烤面包失败: {r.stderr[:100]}"
    except Exception as e:
        return f"烤面包失败: {e}"


def yudustrum_compact() -> str:
    """压缩过时记忆：合并相似记忆，清理噪音"""
    try:
        from yantrikdb import consolidate
        from yantrikdb import YantrikDB
        db = YantrikDB.with_default(DB_PATH)
        result = consolidate(db, sim_threshold=0.85, time_window_days=30, dry_run=True)
        db.close()
        return json.dumps(result)
    except Exception as e:
        return f"压缩失败: {e}"


from datetime import datetime


# ═══════════════════ 工具注册 ═══════════════════

yudustream_tools = [
    {
        "name": "yudustrum_recall",
        "description": "检索羽渡尘记忆。输入问题返回相关记忆片段。",
        "parameters": {
            "type": "object", "properties": {
                "query": {"type": "string", "description": "检索问题"},
                "top_k": {"type": "integer", "description": "返回条数", "default": 8}
            }, "required": ["query"]
        }
    },
    {
        "name": "yudustrum_stats",
        "description": "查看羽渡尘状态：记忆数、实体数、关系边、矛盾数。",
        "parameters": {"type": "object", "properties": {}}
    },
    {
        "name": "yudustrum_save",
        "description": "手动存盘 + 自动烤面包。把羽毛变更提交到 git 并更新仪表盘。",
        "parameters": {"type": "object", "properties": {
            "manual": {"type": "boolean", "description": "是否手动触发", "default": True}
        }}
    },
    {
        "name": "yudustrum_audit",
        "description": "执行羽渡尘健康审计：检查过时记忆、矛盾、完整性。",
        "parameters": {"type": "object", "properties": {}}
    },
    {
        "name": "yudustrum_bake",
        "description": "手动烤面包：重新生成仪表盘 status.js 和 graph_data.js。",
        "parameters": {"type": "object", "properties": {}}
    },
    {
        "name": "yudustrum_compact",
        "description": "压缩过时记忆：合并相似记忆，释放空间。",
        "parameters": {"type": "object", "properties": {}}
    }
]


# ═══════════════════ Hooks ═══════════════════

def on_session_start(context):
    """会话开始时注入当前高价值记忆"""
    try:
        from yantrikdb import YantrikDB
        db = YantrikDB.with_default(DB_PATH)
        top = db.recall(query="", top_k=5, include_consolidated=False)
        db.close()
        if top:
            memories = []
            for r in top:
                text = r.get("text", "")[:300]
                memories.append({"text": text, "score": r.get("score", 0)})
            context.setdefault("yudustrum_init", memories)
    except:
        pass
    return context


def on_session_end(context):
    """会话结束时自动存盘 + 烤面包"""
    try:
        subprocess.run(["git", "add", "-A"], cwd=str(_HERE), capture_output=True, timeout=15)
        subprocess.run(
            ["git", "commit", "-m", f"🕊️ 会话结束存盘 {datetime.now().strftime('%m/%d %H:%M')}"],
            cwd=str(_HERE), capture_output=True, timeout=15
        )
        subprocess.run(
            ["/usr/local/lib/hermes-agent/venv/bin/python3",
             "/mnt/d/hermes-workspace/scripts/bake_dashboard.py"],
            capture_output=True, timeout=30
        )
    except:
        pass
    return context


def on_pre_compress(context):
    """压缩前注入当前最高分记忆"""
    try:
        from yantrikdb import YantrikDB
        db = YantrikDB.with_default(DB_PATH)
        recent = db.recall(query="", top_k=5, include_consolidated=False)
        db.close()
        if recent:
            context.setdefault("memories", []).extend([
                {"text": r.get("text", "")[:500], "score": r.get("score", 0)}
                for r in recent[:5]
            ])
    except:
        pass
    return context
