@echo off
chcp 65001 >nul
echo 🕊️ 羽渡尘 自检 + 仪表盘刷新
echo =============================
echo.
echo 正在运行自检...
wsl python3 /mnt/d/hermes-workspace/scripts/yudustream_audit.py
echo.
echo 正在烘焙仪表盘...
wsl python3 /mnt/d/hermes-workspace/scripts/bake_dashboard.py
echo.
echo ✅ 完成！正在打开仪表盘...
start chrome "file:///D:/hermes-workspace/skills/yudustream/dashboard.html"
echo.
pause
