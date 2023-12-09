import platform
import psutil


def system_information():
    print("Betriebssystem:", platform.system())
    print("Betriebssystem-Version:", platform.release())
    print("Betriebssystem-Detail:", platform.version())
    print("Architektur:", platform.machine())
    print("Hostname:", platform.node()) 
    print("Prozessor:", platform.processor())
    print("Physische Kerne:", psutil.cpu_count(logical=False))
    print("Gesamte Kerne:", psutil.cpu_count(logical=True))
    print("CPU-Frequenz:", psutil.cpu_freq().current)
    print("Gesamter RAM:", convert_to_gb(psutil.virtual_memory().total))
    print("Verfügbarer RAM:", convert_to_gb(psutil.virtual_memory().available))
    print("RAM-Nutzung:", psutil.virtual_memory().percent)
    print("Speicherplatznutzung:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"  Laufwerk: {partition.device}")
        print(f"  Mountpoint: {partition.mountpoint}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # dies kann passieren, wenn das Laufwerk gerade nicht gemountet ist
            continue
        print(f"  Gesamtspeicherplatz: {convert_to_gb(partition_usage.total)} GB")
        print(f"  Verwendeter Speicherplatz: {convert_to_gb(partition_usage.used)} GB")
        print(f"  Freier Speicherplatz: {convert_to_gb(partition_usage.free)} GB")
        print(f"  Prozentsatz der Nutzung: {partition_usage.percent}%")
        print()

def convert_to_gb(bytes):
    return round(bytes / (1024**3), 2)

system_information()
