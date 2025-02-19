import os
import sys
import time
import signal
import subprocess
from coredotcloud.config import load_config
from coredotcloud.collector import get_system_info, get_runtime_data
from coredotcloud.sender import send_data

PID_FILE = "/tmp/coredotcloud.pid"


def write_pid(pid):
    """현재 프로세스의 PID를 파일에 저장"""
    with open(PID_FILE, "w") as f:
        f.write(str(pid))


def remove_pid():
    """PID 파일 삭제"""
    if os.path.exists(PID_FILE):
        os.remove(PID_FILE)


def read_pid():
    """저장된 PID 읽기"""
    if os.path.exists(PID_FILE):
        with open(PID_FILE, "r") as f:
            return int(f.read().strip())
    return None


def is_running():
    """프로세스가 실행 중인지 확인"""
    pid = read_pid()
    if pid:
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False
    return False


def stop_daemon():
    """실행 중인 데몬 종료"""
    pid = read_pid()
    if pid:
        try:
            os.kill(pid, signal.SIGTERM)
            print(f"[INFO] Daemon (PID {pid}) 종료")
        except ProcessLookupError:
            print("[WARNING] 프로세스가 실행 중이 아닙니다.")
    remove_pid()


def monitor():
    """시스템 모니터링 실행 (데몬)"""
    config = load_config()
    api_url = config["API_URL"]
    api_key = config["API_KEY"]

    if not api_key or api_key == "your-api-key":
        print("[ERROR] API_KEY를 설정해주세요.")
        return

    print("[INFO] coredotcloud 데몬 실행 중...")

    # PID 기록
    write_pid(os.getpid())

    # 🚀 최초 실행 시 전체 시스템 정보 전송
    send_data("info", api_url, api_key, get_system_info())

    while True:
        send_data("d", api_url, api_key, get_runtime_data())
        time.sleep(30)


def start_daemon():
    """데몬 시작"""
    if is_running():
        print("[ERROR] 이미 실행 중입니다.")
        sys.exit(1)

    print("[INFO] coredotcloud 데몬 시작...")

    # `subprocess.Popen`을 사용하여 백그라운드 실행
    process = subprocess.Popen([sys.executable, "-c", "from coredotcloud.main import monitor; monitor()"],
                               stdout=open("/dev/null", "w"),
                               stderr=open("/dev/null", "w"),
                               stdin=open("/dev/null", "r"),
                               start_new_session=True)

    write_pid(process.pid)
    time.sleep(1)

    if is_running():
        print(f"[INFO] Daemon 실행 성공 (PID {process.pid})")
    else:
        print("[ERROR] 데몬 실행 실패")


def main():
    """CLI 실행"""
    if len(sys.argv) == 1:
        print("사용법: coredotcloud [start|stop|status|run]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "start":
        start_daemon()
    elif command == "stop":
        stop_daemon()
    elif command == "status":
        if is_running():
            print(f"[INFO] Daemon 실행 중 (PID {read_pid()})")
        else:
            print("[INFO] Daemon 실행 안됨")
    elif command == "run":
        monitor()  # 포그라운드 실행
    else:
        print("사용법: coredotcloud [start|stop|status|run]")
