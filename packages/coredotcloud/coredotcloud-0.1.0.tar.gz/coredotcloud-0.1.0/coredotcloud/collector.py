import psutil
import time


def get_system_data():
    """시스템 정보를 리스트로 반환"""
    cpu_usage = psutil.cpu_percent(interval=1)  # CPU 사용률 (%)

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

    return [
        cpu_usage,     # CPU 사용률 (%)
        memory_total,  # 총 메모리 (GB)
        memory_used,   # 사용 중인 메모리 (GB)
        memory_percent,  # 메모리 사용률 (%)
        disk_total,    # 총 디스크 크기 (GB)
        disk_used,     # 사용 중인 디스크 (GB)
        disk_percent,  # 디스크 사용률 (%)
        rx_speed,      # 네트워크 수신 속도 (KB/s)
        tx_speed       # 네트워크 송신 속도 (KB/s)
    ]
