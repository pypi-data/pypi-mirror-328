import time
from coredotcloud.config import load_config
from coredotcloud.collector import get_system_data
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

    while True:
        data = get_system_data()
        send_data(api_url, api_key, data)
        time.sleep(30)


if __name__ == "__main__":
    main()
