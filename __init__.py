"""
羽渡尘 Plugin v1.1 — 全功能
═══════════════════════════════════════════
6工具 + on_message 自动检索
═══════════════════════════════════════════
"""
from __future__ import annotations
import json, os, subprocess, sys
from pathlib import Path
from datetime import datetime

_HERE = Path(__file__).parent
DB_PATH = str(_HERE / "yantrikdb_yudustrum.db")
FEATHERS = _HERE / "feathers"

register = "yudustream_tools"


# ═══════════════════ 核心 ═══════════════════

def _recall(query: str, top_k: int = 5) -> list:
    """内部检索，返回原始结果"""
    try:
        from yantrikdb import YantrikDB
        db = YantrikDB.with_default(DB_PATH)
        results = db.recall(query=query, top_k=top_k, include_consolidated=False)
        db.close()
        return results or []
    except:
        return []


def _auto_inject(user_message: str) -> str:
    """自动检索并拼接成提示块"""
    results = _recall(user_message, top_k=5)
    if not results:
        return ""
    lines = ["[羽渡尘 v7 自动加载]"]
    for r in results:
        text = r.get("text", "")[:200]
        score = r.get("score", 0)
        title = text.split("\n")[0][:60] if text else "?"
        lines.append(f"  [{score:.2f}] {title}")
    return "\n".join(lines)


# ═══════════════════ 工具 ═══════════════════

def yudustrum_recall(query: str, top_k: int = 8) -> str:
    """检索羽渡尘记忆。query: 查询内容, top_k: 返回条数"""
    results = _recall(query, top_k)
    if not results:
        return "无相关羽毛记忆"
    lines = [f"[羽渡尘 v7 检索] {query}"]
    for r in results:
        text = r.get("text", "")[:200]
        score = r.get("score", 0)
        title = text.split("\n")[0][:60] if text else "?"
        lines.append(f"- [{score:.2f}] {title}")
    return "\n".join(lines)


def yudustrum_stats() -> str:
    """羽渡尘状态"""
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
    """存盘 + 自动烤面包"""
    try:
        subprocess.run(["git", "add", "-A"], cwd=str(_HERE), capture_output=True, timeout=15)
        r = subprocess.run(
            ["git", "commit", "-m", f"🕊️ {'手动' if manual else '自动'}存盘 {datetime.now().strftime('%m/%d %H:%M')}"],
            cwd=str(_HERE), capture_output=True, text=True, timeout=15
        )
        subprocess.run(["/usr/local/lib/hermes-agent/venv/bin/python3",
                       "/mnt/d/hermes-workspace/scripts/bake_dashboard.py"],
                       capture_output=True, timeout=30)
        return "存盘+烤面包成功" if r.returncode in (0, 1) else f"存盘: {r.stderr[:100]}"
    except Exception as e:
        return f"存盘失败: {e}"


def yudustrum_audit() -> str:
    """健康审计"""
    try:
        from yantrikdb import YantrikDB
        db = YantrikDB.with_default(DB_PATH)
        s = db.stats()
        conflicts = db.get_conflicts(limit=5)
        stale = db.stale(days=90, limit=5)
        db.close()
        c = len(conflicts) if isinstance(conflicts, list) else 0
        st = len(stale) if isinstance(stale, list) else 0
        parts = [f"活跃: {s.get('active_memories',0)}", f"过时(>90天): {st}", f"矛盾: {c}"]
        if c: parts.append("建议: resolve_conflict 解决矛盾")
        if st > 5: parts.append("建议: consolidate 压缩过时")
        return "\n".join(parts)
    except Exception as e:
        return f"审计失败: {e}"


def yudustrum_bake() -> str:
    """手动烤面包"""
    try:
        r = subprocess.run(
            ["/usr/local/lib/hermes-agent/venv/bin/python3",
             "/mnt/d/hermes-workspace/scripts/bake_dashboard.py"],
            capture_output=True, text=True, timeout=30
        )
        return r.stdout.strip() if r.returncode == 0 else f"失败: {r.stderr[:100]}"
    except Exception as e:
        return f"失败: {e}"


def yudustrum_compact() -> str:
    """压缩（干跑，不实际删除）"""
    try:
        from yantrikdb import YantrikDB, consolidate
        db = YantrikDB.with_default(DB_PATH)
        result = consolidate(db, sim_threshold=0.85, time_window_days=30, dry_run=True)
        db.close()
        return json.dumps(result)
    except Exception as e:
        return f"压缩失败: {e}"


# ═══════════════════ 工具注册 ═══════════════════

yudustream_tools = [
    {"name": "yudustrum_recall", "description": "检索羽渡尘记忆。输入问题返回相关记忆片段。",
     "parameters": {"type": "object", "properties": {
         "query": {"type": "string", "description": "检索问题"},
         "top_k": {"type": "integer", "description": "返回条数", "default": 8}},
         "required": ["query"]}},
    {"name": "yudustrum_stats", "description": "羽渡尘状态：记忆数、实体、关系边、矛盾。",
     "parameters": {"type": "object", "properties": {}}},
    {"name": "yudustrum_save", "description": "存盘+自动烤面包。",
     "parameters": {"type": "object", "properties": {
         "manual": {"type": "boolean", "description": "手动触发", "default": True}}}},
    {"name": "yudustrum_audit", "description": "健康审计：过时记忆、矛盾。",
     "parameters": {"type": "object", "properties": {}}},
    {"name": "yudustrum_bake", "description": "手动烤面包：更新仪表盘。",
     "parameters": {"type": "object", "properties": {}}},
    {"name": "yudustrum_compact", "description": "压缩过时记忆（干跑预览）。",
     "parameters": {"type": "object", "properties": {}}}
]


# ═══════════════════ Hooks ═══════════════════

def on_message(context):
    """每条消息自动检索羽渡尘"""
    try:
        msg = context.get("content", "")
        if msg and len(msg) > 3:
            injected = _auto_inject(msg)
            if injected:
                context.setdefault("yudustrum_auto", injected)
    except:
        pass
    return context


def on_session_start(context):
    """会话开始注入"""
    try:
        top = _recall("", 5)
        if top:
            context.setdefault("yudustrum_init",
                [{"text": r.get("text", "")[:300], "score": r.get("score", 0)} for r in top])
    except:
        pass
    return context


def on_session_end(context):
    """会话结束存盘"""
    try:
        subprocess.run(["git", "add", "-A"], cwd=str(_HERE), capture_output=True, timeout=15)
        subprocess.run(["git", "commit", "-m", f"🕊️ 结束存盘 {datetime.now().strftime('%m/%d %H:%M')}"],
                      cwd=str(_HERE), capture_output=True, timeout=15)
        subprocess.run(["/usr/local/lib/hermes-agent/venv/bin/python3",
                       "/mnt/d/hermes-workspace/scripts/bake_dashboard.py"],
                       capture_output=True, timeout=30)
    except:
        pass
    return context


def on_pre_compress(context):
    """压缩前抢救"""
    try:
        top = _recall("", 5)
        if top:
            context.setdefault("memories", []).extend(
                [{"text": r.get("text", "")[:500], "score": r.get("score", 0)} for r in top[:5]]
            )
    except:
        pass
    return context
