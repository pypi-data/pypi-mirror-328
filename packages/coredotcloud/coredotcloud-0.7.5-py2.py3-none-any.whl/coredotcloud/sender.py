import requests
from datetime import datetime


def send_data(category, api_url, api_key, data, verbose=False):
    """API에 데이터를 리스트 형태로 전송

    Args:
        category: 데이터 카테고리
        api_url: API 엔드포인트 URL
        api_key: API 인증 키
        data: 전송할 데이터
        verbose: 상세 로그 출력 여부 (기본값: False)
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = {"a": api_key, "c": category, "d": data}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(
            api_url, json=payload, headers=headers, timeout=5)
        response.raise_for_status()
        if verbose:
            print(f"[{current_time}] [SUCCESS] 데이터 전송 완료: {payload}")
        else:
            print(f"[{current_time}] [SUCCESS] 데이터 전송 완료")
    except requests.exceptions.ConnectionError:
        print(f"[ERROR] 서버 연결 실패: {api_url}에 연결할 수 없습니다. 네트워크 연결을 확인해주세요.")
    except requests.exceptions.Timeout:
        print(f"[ERROR] 요청 시간 초과: 서버 응답이 5초를 초과했습니다. 잠시 후 다시 시도해주세요.")
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code == 400:
            print(f"[ERROR] 잘못된 요청: 전송된 데이터가 올바르지 않습니다. ({e.response.text})")
        elif status_code == 401 or status_code == 403:
            print(f"[ERROR] 인증 실패: API 키가 유효하지 않거나 권한이 없습니다.")
        elif status_code == 404:
            print(f"[ERROR] 잘못된 API URL: {api_url}을 찾을 수 없습니다.")
        elif status_code >= 500:
            print(f"[ERROR] 서버 오류: 서버에서 처리 중 문제가 발생했습니다. 잠시 후 다시 시도해주세요.")
        else:
            print(f"[ERROR] HTTP 오류 발생: {e}")
    except Exception as e:
        print(f"[ERROR] 예기치 않은 오류 발생: {str(e)}")
