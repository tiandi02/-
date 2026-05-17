@echo off
title HwMonitor64 自动关闭监控
echo 正在启动监控程序...
python "%~dp0kill_hwmonitor.py"
pause
