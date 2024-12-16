import psutil
import logging

# Configure logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 90  # in percentage

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU Usage: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        logging.warning(f"High Memory Usage: {memory.percent}%")
    return memory.percent

def check_disk_space():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        logging.warning(f"Low Disk Space: {disk.percent}% used")
    return disk.percent

def monitor_system():
    cpu = check_cpu_usage()
    memory = check_memory_usage()
    disk = check_disk_space()

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

if __name__ == "__main__":
    monitor_system()
