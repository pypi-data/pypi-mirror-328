import json
import os

CONFIG_FILE = os.path.expanduser("~/.coredotcloud.json")


def load_config():
    """설정 파일을 로드합니다. 존재하지 않으면 생성합니다."""
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "API_URL": "https://API_URL/sentinel/v1",
            "API_KEY": "your-api-key"
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f, indent=4)
        print(f"[INFO] 설정 파일이 생성되었습니다. {CONFIG_FILE} 를 수정해주세요.")
        exit(1)

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)
