# -
运行游戏加加时，会造成电脑卡顿。本项旨在解决这一问题。
#Kill HwMonitor64

自动监控并关闭 HwMonitor64.exe 的小工具。当目标进程启动时，本程序会自动检测并终止它。

##功能

- 每 2 秒自动扫描系统进程
- 检测到 HwMonitor64.exe 运行时自动终止
- 支持后台静默运行（无窗口）
- 支持设置开机自启动
- 自动记录操作日志

## 运行环境

- Windows 10 / 11
- Python 3.8+
- psutil 库（`pip install psutil`）

## 使用方法

### 手动启动（带窗口）

双击 `启动监控.bat`，在弹出的窗口中按 Ctrl+C 停止。

### 后台静默运行

双击 `kill_hwmonitor.pyw`，无窗口运行。通过任务管理器结束 pythonw.exe 来停止。

### 开机自启动

右键以管理员身份运行 `安装开机自启.bat`。

卸载自启动：
```
schtasks /delete /tn "KillHwMonitor64" /f
```

## 配置

修改 `kill_hwmonitor.py` 中的以下参数：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `CHECK_INTERVAL` | 2 | 检查间隔（秒） |
| `TARGET_PROCESS` | HwMonitor64.exe | 目标进程名 |

## 性能影响

| 资源 | 占用 |
|------|------|
| CPU | 0.05%~0.2% |
| GPU | 0% |
| 内存 | 20~30 MB |

## 许可证

[MIT License](LICENSE)
