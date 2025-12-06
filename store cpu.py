import psutil

print(f"CPU Percent: {psutil.cpu_percent()}%, RAM: {psutil.virtual_memory()}")

def to_gb(val):
    return round(val / (10** 9), 2)

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory()

print(f"CPU Usage     : {cpu}%")
print(f"Total RAM     : {to_gb(ram.total)} GB")
print(f"Used RAM      : {to_gb(ram.used)} GB")
print(f"Available RAM : {to_gb(ram.available)} GB")
print(f"RAM Usage     : {ram.percent}%")
