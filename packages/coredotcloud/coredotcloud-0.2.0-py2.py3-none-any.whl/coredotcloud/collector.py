import psutil
import time

try:
    import GPUtil
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False


def get_system_data():
    """시스템 정보를 리스트로 반환 (CPU 및 GPU 개별 정보 포함)"""
    # 전체 CPU 사용률 (%)
    cpu_usage = psutil.cpu_percent(interval=1)

    # 개별 CPU 사용률 (%)
    per_cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    cpu_count = len(per_cpu_usage)  # CPU 개수

    # 메모리 정보
    mem_info = psutil.virtual_memory()
    memory_total = round(mem_info.total / (1024 ** 3), 2)  # 총 메모리 (GB)
    memory_used = round(mem_info.used / (1024 ** 3), 2)    # 사용 메모리 (GB)
    memory_percent = mem_info.percent                      # 메모리 사용률 (%)

    # 디스크 정보
    disk_info = psutil.disk_usage("/")
    disk_total = round(disk_info.total / (1024 ** 3), 2)  # 총 디스크 (GB)
    disk_used = round(disk_info.used / (1024 ** 3), 2)    # 사용 디스크 (GB)
    disk_percent = disk_info.percent                      # 디스크 사용률 (%)

    # 네트워크 속도 (1초간 변화량 측정)
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()
    rx_speed = round((net2.bytes_recv - net1.bytes_recv) / 1024, 2)  # KB/s
    tx_speed = round((net2.bytes_sent - net1.bytes_sent) / 1024, 2)  # KB/s

    # GPU 정보 (있다면 추가)
    gpu_data = []
    if GPU_AVAILABLE:
        gpus = GPUtil.getGPUs()
        gpu_count = len(gpus)
        for gpu in gpus:
            gpu_data.extend([
                gpu.load * 100,            # GPU 사용률 (%)
                round(gpu.memoryTotal, 2),  # 총 VRAM (MB)
                round(gpu.memoryUsed, 2)   # 사용 중인 VRAM (MB)
            ])
    else:
        gpu_count = 0

    # 최종 데이터 리스트 생성
    return [
        cpu_usage,     # 전체 CPU 사용률 (%)
        memory_total,  # 총 메모리 (GB)
        memory_used,   # 사용 중인 메모리 (GB)
        memory_percent,  # 메모리 사용률 (%)
        disk_total,    # 총 디스크 크기 (GB)
        disk_used,     # 사용 중인 디스크 (GB)
        disk_percent,  # 디스크 사용률 (%)
        rx_speed,      # 네트워크 수신 속도 (KB/s)
        tx_speed,      # 네트워크 송신 속도 (KB/s)
        cpu_count,     # CPU 개수
        *per_cpu_usage,  # 개별 CPU 사용률 리스트
        gpu_count,     # GPU 개수
        *gpu_data      # GPU 사용률 및 메모리 리스트
    ]
