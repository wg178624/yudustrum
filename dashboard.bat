@echo off
chcp 65001 >nul
wsl python3 /mnt/d/hermes-workspace/scripts/bake_dashboard.py >nul 2>&1
start chrome http://localhost:8080/dashboard.html
