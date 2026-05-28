@echo off
chcp 65001 >nul
echo 🕊️ 羽渡尘 启动
echo ===================
echo.

echo 正在刷新数据...
wsl python3 /mnt/d/hermes-workspace/scripts/bake_dashboard.py
if %ERRORLEVEL% NEQ 0 (
    echo ⚠️ 烘焙失败，继续启动
)
echo.

echo 启动本地服务器（端口 8080）...
start wsl python3 -m http.server 8080 --directory /mnt/d/hermes-workspace/skills/yudustream
timeout /t 2 >nul

echo 🚀 打开仪表盘...
start chrome http://localhost:8080/dashboard.html

echo.
echo 关闭此窗口即可停止服务器
pause
wsl pkill -f "http.server" >nul 2>&1
