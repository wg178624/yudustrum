@echo off
chcp 65001 >nul

rem 检查后端是否已在运行
wsl curl -s -o nul -w "%%{http_code}" http://localhost:8080/api/refresh 2>nul | find "200" >nul
if %ERRORLEVEL% NEQ 0 (
    wsl python3 /mnt/d/hermes-workspace/server.py > nul 2>&1 &
    timeout /t 2 >nul
)

start chrome http://localhost:8081/dashboard.html
