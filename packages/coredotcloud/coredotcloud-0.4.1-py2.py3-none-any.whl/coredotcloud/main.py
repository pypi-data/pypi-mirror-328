import time
from coredotcloud.config import load_config
from coredotcloud.collector import get_system_info, get_runtime_data
from coredotcloud.sender import send_data


def main():
    """시스템 모니터링 실행"""
    config = load_config()
    api_url = config["API_URL"]
    api_key = config["API_KEY"]

    if not api_key or api_key == "your-api-key":
        print("[ERROR] API_KEY를 설정해주세요.")
        return

    print("[INFO] 시스템 모니터링 시작...")

    # 🚀 최초 실행 시 전체 시스템 정보 전송
    initial_data = {
        "a": api_key,
        "c": "info",
        "d": get_system_info()
    }
    send_data(api_url, api_key, initial_data)

    while True:
        runtime_data = {
            "a": api_key,
            "c": "d",
            "d": get_runtime_data()
        }
        send_data(api_url, api_key, runtime_data)
        time.sleep(30)


if __name__ == "__main__":
    main()
