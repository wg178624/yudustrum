@echo off
echo 🕊️ 羽渡尘 仪表盘启动中...
cd /d D:\hermes-workspace\skills\yudustream
start python3 -m http.server 8080
timeout /t 2 >nul
start chrome http://localhost:8080/dashboard.html
echo ✅ 仪表盘已打开
echo 关闭命令窗口即可停止服务器
pause
