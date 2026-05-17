@echo off
title 安装开机自启动
echo 正在创建开机自启动计划任务...

schtasks /create /tn "KillHwMonitor64" /tr "\"%~dp0kill_hwmonitor.pyw\"" /sc onlogon /rl highest /f

echo.
echo 已创建计划任务: KillHwMonitor64
echo 每次登录时会自动运行监控程序
echo.
echo 如需删除自启动，运行: schtasks /delete /tn "KillHwMonitor64" /f
pause
