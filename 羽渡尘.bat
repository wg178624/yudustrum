@echo off
chcp 65001 >nul
echo 🕊️ 羽渡尘
echo ===================
echo.

rem 检查后端是否已在运行
wsl curl -s -o nul -w "%%{http_code}" http://localhost:8080/api/refresh 2>nul | find "200" >nul
if %ERRORLEVEL%==0 (
    echo 后端已在运行（http://localhost:8080）
) else (
    echo 启动后端服务...
    start wsl python3 /mnt/d/hermes-workspace/server.py
    timeout /t 2 >nul
)

echo.
echo 🚀 打开仪表盘...
start chrome http://localhost:8080/dashboard.html
echo.
echo 点击刷新按钮即可实时烘焙数据
echo 关闭此窗口不会停止后端，后端在WSL后台持续运行
echo 如需停止后端，运行: wsl pkill -f server.py
echo.
pause
