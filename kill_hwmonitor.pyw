"""
自动监控并关闭 HwMonitor64.exe（后台静默版本）
使用 .pyw 扩展名运行时不会弹出命令行窗口
"""

import psutil
import time
import logging

TARGET_PROCESS = "HwMonitor64.exe"
CHECK_INTERVAL = 2
LOG_FILE = r"D:\Claude code\程序\kill_log.txt"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8",
)


def kill_target():
    for proc in psutil.process_iter(["pid", "name", "exe"]):
        try:
            if proc.info["name"] and proc.info["name"].lower() == TARGET_PROCESS.lower():
                target_path = r"C:\Users\16833\AppData\Local\GamePP\Apps\8fb708e5972662062da26a2bb4753a23\5.6.63.420\win32\Hardware\HwMonitor64.exe"
                exe_path = (proc.info["exe"] or "").lower()
                if exe_path == target_path.lower():
                    proc.kill()
                    logging.info(f"已终止进程: {TARGET_PROCESS} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def main():
    logging.info("监控已启动（后台模式）")
    while True:
        kill_target()
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
