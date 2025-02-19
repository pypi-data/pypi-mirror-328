import psutil
import platform
import time

try:
    import GPUtil
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False


def get_cpu_info():
    """CPU 상세 정보 수집"""
    return {
        "model": platform.processor(),
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "frequency_mhz": psutil.cpu_freq().max,
        "cpu_percent": psutil.cpu_percent(interval=1)
    }


def get_memory_info():
    """메모리 상세 정보 수집"""
    mem_info = psutil.virtual_memory()
    return {
        "total_gb": round(mem_info.total / (1024 ** 3), 2),
        "available_gb": round(mem_info.available / (1024 ** 3), 2),
        "used_gb": round(mem_info.used / (1024 ** 3), 2),
        "usage_percent": mem_info.percent
    }


def get_disk_info():
    """디스크 상세 정보 수집"""
    partitions = psutil.disk_partitions()
    disk_data = []

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_data.append({
            "device": partition.device,
            "mountpoint": partition.mountpoint,
            "filesystem": partition.fstype,
            "total_gb": round(usage.total / (1024 ** 3), 2),
            "used_gb": round(usage.used / (1024 ** 3), 2),
            "free_gb": round(usage.free / (1024 ** 3), 2),
            "usage_percent": usage.percent
        })

    return disk_data


def get_network_info():
    """네트워크 인터페이스 및 IP 정보 수집"""
    net_info = psutil.net_if_addrs()
    interfaces = {}

    for interface, addresses in net_info.items():
        interfaces[interface] = [
            {"family": str(addr.family), "address": addr.address} for addr in addresses]

    return interfaces


def get_network_speed():
    """네트워크 속도 측정"""
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()
    return {
        "rx_speed_kb": round((net2.bytes_recv - net1.bytes_recv) / 1024, 2),
        "tx_speed_kb": round((net2.bytes_sent - net1.bytes_sent) / 1024, 2)
    }


def get_gpu_info():
    """GPU 상세 정보 수집 (여러 개 가능)"""
    gpu_data = []

    if GPU_AVAILABLE:
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            gpu_data.append({
                "name": gpu.name,
                "load_percent": gpu.load * 100,
                "memory_total_mb": round(gpu.memoryTotal, 2),
                "memory_used_mb": round(gpu.memoryUsed, 2),
                "memory_free_mb": round(gpu.memoryFree, 2),
                "temperature": gpu.temperature
            })

    return gpu_data


def get_system_info():
    """시스템 전체 정보 (최초 실행 시 전송)"""
    return {
        "hostname": platform.node(),
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture()[0],
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "network": get_network_info(),
        "gpu": get_gpu_info()
    }


def get_runtime_data():
    """정기 데이터 수집
    시스템 정보를 리스트로 반환 (CPU 및 GPU 개별 정보 포함)"""
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
            # GPU 온도를 안전하게 가져옴 (속성이 없거나 None인 경우 0으로 처리)
            temperature = getattr(gpu, 'temperature', 0) or 0

            gpu_data.extend([
                gpu.load * 100,            # GPU 사용률 (%)
                round(gpu.memoryTotal, 2),  # 총 VRAM (MB)
                round(gpu.memoryUsed, 2),   # 사용 중인 VRAM (MB)
                temperature            # GPU 온도 (°C)
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
        gpu_count,     # GPU 개수
        *per_cpu_usage,  # 개별 CPU 사용률 리스트
        *gpu_data      # GPU 사용률 및 VRAM 정보 리스트
    ]
