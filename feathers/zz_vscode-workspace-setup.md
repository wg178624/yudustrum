---
title: "VSCode 工作区配置"
tags: [reference]
type: reference
---

# VSCode 工作区配置（Hermes 羽渡尘）

## 位置

`D:\hermes-workspace\.vscode\`

## 推荐拓展（extensions.json）

```json
{
    "recommendations": [
        "ms-vscode.cpptools",          // C/C++ 智能提示
        "ms-vscode.cpptools-themes",
        "ms-vscode.cpptools-extension-pack",
        "yzhang.markdown-all-in-one",  // 羽毛编写
        "ms-vscode-remote.remote-wsl", // WSL 远程开发
        "eamodio.gitlens",             // Git 历史
        "vscode-icons-team.vscode-icons",
        "streetsidesoftware.code-spell-checker"
    ]
}
```

## 预置配置（settings.json）

```json
{
    "editor.fontSize": 14,
    "editor.tabSize": 4,
    "files.autoSave": "onFocusChange",
    "C_Cpp.default.compilerPath": "/usr/bin/gcc",
    "C_Cpp.default.cStandard": "c17",
    "C_Cpp.default.cppStandard": "c++17",
    "markdown.preview.breaks": true
}
```

## 用途

- Remote - WSL 连进 Debian 写 C/C++ 学习代码
- Markdown 插件写羽毛（预览/补全/目录）
- GitLens 追踪羽渡尘修改历史
