# coredotcloud 코어닷클라우드 - 시스템 모니터링 클라이언트

coredotcloud는 CPU, 메모리, 디스크, 네트워크, GPU 사용량 등의 **시스템 정보를 정기적으로 수집**하여 **RESTful API로 전송**하는 Python 패키지입니다.
다중 CPU 및 GPU를 지원하며, **가벼운 JSON 형식의 데이터를 효율적으로 전송**할 수 있도록 설계되었습니다.

CoreDotCloud is a lightweight system monitoring tool that collects CPU, memory, disk, and network usage data and sends it to a predefined RESTful API.

## 🚀 **특징**

-   **CPU, 메모리, 디스크, 네트워크 속도 모니터링**
-   **다중 CPU & 다중 GPU 장비 지원**
-   **설정 파일 (`~/.coredotcloud.json`)을 통해 API 정보 관리**
-   **30초마다 자동으로 데이터 수집 및 전송**
-   **데몬 모드 지원 (`start`, `stop`, `status`, `run`)**
-   **가볍고 빠른 리스트 기반 JSON 데이터 구조**
-   **Python 3.7 이상 지원**

## 📥 **설치 방법**

COREDOTCLOUD는 PyPI에 등록된 Python 패키지입니다.

```sh
pip install coredotcloud
```

설치가 완료되면 `coredotcloud` 명령어를 실행할 수 있습니다.

---

## ⚙️ **설정 파일 생성**

설정 파일은 **사용자의 홈 디렉토리 (`~/.coredotcloud.json`)** 에 위치합니다.
최초 실행 시 자동으로 생성되며, API 키를 입력한 후 사용하면 됩니다.

### **설정 파일 위치**

-   **Linux/macOS**: `~/.coredotcloud.json`
-   **Windows**: `C:\Users\사용자이름\.coredotcloud.json`

### **설정 파일 예시 (`~/.coredotcloud.json`)**

```json
{
    "API_URL": "https://mon.core.today/sentinel/v1",
    "API_KEY": "DKWs8wl"
}
```

| 항목      | 설명                           |
| --------- | ------------------------------ |
| `API_URL` | 데이터를 전송할 API 엔드포인트 |
| `API_KEY` | API 인증을 위한 키             |

---

## ▶ **사용 방법**

### 1️⃣ **설정 파일 확인**

API 키와 URL을 설정했는지 확인하세요.

```sh
nano ~/.coredotcloud.json
```

### 2️⃣ **모니터링 실행**

#### **🔹 데몬 모드 실행**

```sh
coredotcloud start   # 백그라운드에서 실행
coredotcloud status  # 실행 상태 확인
coredotcloud stop    # 백그라운드 프로세스 종료
```

#### **🔹 포그라운드에서 실행**

```sh
coredotcloud run
```

-   `start` → 백그라운드에서 실행 (PID 관리)
-   `stop` → 실행 중인 데몬 종료
-   `status` → 실행 여부 확인
-   `run` → 포그라운드에서 실행

---

## 📡 **전송되는 데이터 형식**

COREDOTCLOUD는 **불필요한 데이터 크기를 줄이기 위해 리스트(JSON 배열) 형태**로 데이터를 전송합니다.
백엔드에서 **인덱스를 기반으로 데이터 항목을 해석**할 수 있습니다.

### **API 요청 예시**

-   **시스템 정보 데이터 (`info`)**

```json
{
    "apikey": "DKWs8wl",
    "category": "info",
    "data": {
        "hostname": "server-01",
        "os": "Linux",
        "os_version": "5.15.0-56-generic",
        "architecture": "x86_64",
        "cpu": { ... },
        "memory": { ... },
        "disk": [...],
        "network": {...},
        "gpu": [{ ... }]
    }
}
```

-   **정기 데이터 (`data`)**

```json
{
    "apikey": "DKWs8wl",
    "category": "data",
    "data": [
        6,  # CPU 개수
        2,  # GPU 개수
        10.0, 15.0, 12.0, 18.0, 22.0, 17.0,  # CPU 사용률
        40.5, 8192, 2048,  # GPU 0 사용률 및 VRAM
        55.2, 4096, 1024,  # GPU 1 사용률 및 VRAM
        500.0, 100.0  # 네트워크 속도
    ]
}
```

-   시스템 정보 데이터

```json
{
    "apikey": "DKWs8wl",
    "category": "info",
    "data": {
        "hostname": "server-01",
        "os": "Linux",
        "os_version": "5.15.0-56-generic",
        "architecture": "x86_64",
        "cpu": {
            "model": "Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz",
            "physical_cores": 8,
            "logical_cores": 16,
            "frequency_mhz": 2300.0,
            "cpu_percent": 5.3
        },
        "memory": {
            "total_gb": 64.0,
            "available_gb": 50.5,
            "used_gb": 13.5,
            "usage_percent": 21.1
        },
        "disk": [...],
        "network": {...},
        "gpu": [
            {
                "name": "NVIDIA Tesla V100",
                "load_percent": 12.5,
                "memory_total_mb": 16384,
                "memory_used_mb": 4096,
                "memory_free_mb": 12288,
                "temperature": 65.0
            }
        ]
    }
}
```

-   예시: CPU 4개, GPU 없음

```json
{
    "apikey": "DKWs8wl",
    "data": [
        14.8,  # 전체 CPU 사용률 (%)
        128.0, # 총 메모리 (GB)
        57.78, # 사용 중인 메모리 (GB)
        46.0,  # 메모리 사용률 (%)
        3721.87, # 총 디스크 크기 (GB)
        10.39,   # 사용 중인 디스크 (GB)
        1.5,     # 디스크 사용률 (%)
        277.0,   # 네트워크 수신 속도 (KB/s)
        8.0,     # 네트워크 송신 속도 (KB/s)
        4,       # CPU 개수
        0,       # GPU 개수
        13.2,    # CPU 0 사용률 (%)
        14.0,    # CPU 1 사용률 (%)
        15.5,    # CPU 2 사용률 (%)
        16.8     # CPU 3 사용률 (%)
    ]
}
```

-   예시: CPU 6개, GPU 2개

```json
{
    "apikey": "DKWs8wl",
    "data": [
        12.5,  # 전체 CPU 사용률 (%)
        64.0,  # 총 메모리 (GB)
        45.0,  # 사용 중인 메모리 (GB)
        70.0,  # 메모리 사용률 (%)
        1000.0, # 총 디스크 크기 (GB)
        500.0,  # 사용 중인 디스크 (GB)
        50.0,   # 디스크 사용률 (%)
        500.0,  # 네트워크 수신 속도 (KB/s)
        100.0,  # 네트워크 송신 속도 (KB/s)
        6,      # CPU 개수
        2,      # GPU 개수
        10.0,   # CPU 0 사용률 (%)
        15.0,   # CPU 1 사용률 (%)
        12.0,   # CPU 2 사용률 (%)
        18.0,   # CPU 3 사용률 (%)
        22.0,   # CPU 4 사용률 (%)
        17.0,   # CPU 5 사용률 (%)
        40.5,   # GPU 0 사용률 (%)
        8192,   # GPU 0 총 VRAM (MB)
        2048,   # GPU 0 사용 중 VRAM (MB)
        55.2,   # GPU 1 사용률 (%)
        4096,   # GPU 1 총 VRAM (MB)
        1024    # GPU 1 사용 중 VRAM (MB)
    ]
}
```

## 🖥️ **수집하는 시스템 정보**

| 항목                | 설명                               |
| ------------------- | ---------------------------------- |
| **CPU 사용률**      | 전체 CPU 사용률 (%)                |
| **개별 CPU 사용률** | 각 CPU 코어별 사용률 (%)           |
| **메모리 용량**     | 총 메모리 (GB)                     |
| **메모리 사용량**   | 사용 중인 메모리 (GB)              |
| **메모리 사용률**   | 메모리 사용률 (%)                  |
| **디스크 용량**     | 총 디스크 크기 (GB)                |
| **디스크 사용량**   | 사용 중인 디스크 (GB)              |
| **디스크 사용률**   | 디스크 사용률 (%)                  |
| **네트워크 속도**   | 최근 1초간 송/수신 속도 (KB/s)     |
| **GPU 사용률**      | GPU 사용률 (%) (GPU가 있으면 추가) |
| **GPU 메모리**      | 총 VRAM (MB) & 사용 중인 VRAM (MB) |

---

## 🛠️ **에러 해결**

### **1️⃣ 설정 파일이 없을 경우**

```sh
[INFO] 설정 파일이 생성되었습니다. ~/.coredotcloud.json 를 수정해주세요.
```

➡ **해결 방법**: 설정 파일을 수정하고 다시 실행하세요.

```sh
nano ~/.coredotcloud.json
```

### **2️⃣ API 전송 실패**

```sh
[ERROR] 데이터 전송 실패: 요청 시간 초과
```

➡ **해결 방법**:

-   인터넷 연결 확인
-   API_URL이 올바른지 확인

### **3️⃣ `GPUtil` 오류 (GPU 정보가 안 나올 경우)**

```sh
ModuleNotFoundError: No module named 'GPUtil'
```

➡ **해결 방법**: `gputil`을 설치하세요.

```sh
pip install gputil
```

---

## 📜 **라이선스**

이 프로젝트는 [MIT 라이선스](LICENSE)를 따릅니다.
