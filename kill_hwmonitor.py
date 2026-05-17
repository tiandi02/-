"""
自动监控并关闭 HwMonitor64.exe
当目标进程启动时自动识别并终止
"""

import psutil
import time
import logging
from datetime import datetime

TARGET_PROCESS = "HwMonitor64.exe"
CHECK_INTERVAL = 2  # 检查间隔（秒）

LOG_FILE = r"D:\Claude code\程序\kill_log.txt"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8",
)


def kill_target():
    """查找并终止目标进程，返回是否成功"""
    found = False
    for proc in psutil.process_iter(["pid", "name", "exe"]):
        try:
            if proc.info["name"] and proc.info["name"].lower() == TARGET_PROCESS.lower():
                target_path = r"C:\Users\16833\AppData\Local\GamePP\Apps\8fb708e5972662062da26a2bb4753a23\5.6.63.420\win32\Hardware\HwMonitor64.exe"
                exe_path = (proc.info["exe"] or "").lower()
                if exe_path == target_path.lower():
                    proc.kill()
                    msg = f"已终止进程: {TARGET_PROCESS} (PID: {proc.info['pid']})"
                    print(msg)
                    logging.info(msg)
                    found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return found


def main():
    print(f"正在监控: {TARGET_PROCESS}")
    print(f"检查间隔: {CHECK_INTERVAL}秒")
    print(f"日志文件: {LOG_FILE}")
    print("按 Ctrl+C 停止监控\n")
    logging.info("监控已启动")

    try:
        while True:
            kill_target()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n监控已停止")
        logging.info("监控已停止")


if __name__ == "__main__":
    main()
