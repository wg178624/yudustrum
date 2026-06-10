"""
羽渡尘 — Hermes Plugin
羽渡尘记忆系统插件。注册 yudustrum_recall 工具和自动存盘 hooks。
"""
from __future__ import annotations

import json, os, subprocess, sys
from pathlib import Path

# 添加羽渡尘库路径
_HERE = Path(__file__).parent
SCRIPTS = _HERE / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

DB_PATH = str(_HERE / "yantrikdb_yudustrum.db")
FEATHERS = _HERE / "feathers"

# 注册入口（Hermes 插件加载器查找这个对象）
register = "yudustream_tools"


def yudustrum_recall(query: str, top_k: int = 5) -> str:
    """搜索羽渡尘记忆库。query: 查询内容, top_k: 返回条数"""
    try:
        from yantrikdb import YantrikDB
        db = YantrikDB.with_default(DB_PATH)
        results = db.recall(query=query, top_k=top_k, include_consolidated=False)
        db.close()
        if not results:
            return "无相关羽毛记忆"
        lines = []
        for r in results:
            text = r.get("text", "")[:200]
            score = r.get("score", 0)
            title = text.split("\n")[0][:60] if text else "?"
            lines.append(f"- [{score:.2f}] {title}")
        return "\n".join(lines)
    except Exception as e:
        return f"检索失败: {e}"


def yudustrum_stats() -> str:
    """查看羽渡尘状态：羽毛数、实体数、关系边"""
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
            "feather_files": len(list(FEATHERS.glob("feather_*.md")))
        })
    except Exception as e:
        return f"状态获取失败: {e}"


def yudustrum_save(manual: bool = True) -> str:
    """存盘（git commit 当前状态）。manual: 是否手动触发"""
    try:
        result = subprocess.run(
            ["git", "add", "-A", "&&", "git", "commit", "-m",
             f"🕊️ 自动存盘 {'手动' if manual else 'session结束'}"],
            cwd=str(_HERE), capture_output=True, text=True, timeout=30
        )
        return "存盘成功" if result.returncode == 0 else f"存盘: {result.stderr[:100]}"
    except Exception as e:
        return f"存盘失败: {e}"


# 工具描述（Hermes 自动注册为可用工具）
yudustrum_tools = [
    {
        "name": "yudustrum_recall",
        "description": "检索羽渡尘记忆。输入问题返回相关记忆片段。",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "检索问题"},
                "top_k": {"type": "integer", "description": "返回条数", "default": 5}
            },
            "required": ["query"]
        }
    },
    {
        "name": "yudustrum_stats",
        "description": "查看羽渡尘当前状态：记忆数、实体数、关系边。",
        "parameters": {"type": "object", "properties": {}}
    },
    {
        "name": "yudustrum_save",
        "description": "手动存盘。把当前羽毛变更提交到 git。",
        "parameters": {
            "type": "object",
            "properties": {
                "manual": {"type": "boolean", "description": "是否手动触发", "default": True}
            }
        }
    }
]


# hooks
def on_session_end(context):
    """会话结束时自动存盘"""
    yudustrum_save(manual=False)
    return context


def on_pre_compress(context):
    """压缩前注入当前最高等级的记忆"""
    try:
        from yantrikdb import YantrikDB
        db = YantrikDB.with_default(DB_PATH)
        recent = db.recall(query="", top_k=3, include_consolidated=False)
        db.close()
        if recent:
            import json
            context.setdefault("memories", []).extend([
                {"text": r.get("text", "")[:500], "score": r.get("score", 0)}
                for r in recent[:3]
            ])
    except:
        pass
    return context
