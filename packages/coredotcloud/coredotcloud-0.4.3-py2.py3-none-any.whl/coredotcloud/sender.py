import requests


def send_data(category, api_url, api_key, data):
    """API에 데이터를 리스트 형태로 전송"""
    payload = {"a": api_key, "c": category, "d": data}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(
            api_url, json=payload, headers=headers, timeout=5)
        response.raise_for_status()
        print(f"[SUCCESS] 데이터 전송 완료: {payload}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] 데이터 전송 실패: {e}")
