import subprocess
import ipaddress

ip = input("Введи айпи: ")
ipaddress.ip_address(ip)

try:
    res = subprocess.run(["ping", "-n", "1", ip])
    if res.returncode == 0:
        print("ИТОГ: Айпи активный!")
    else:
        print("ИТОГ: Айпи неактивный!")
except:
    print("ИТОГ: Неактив")