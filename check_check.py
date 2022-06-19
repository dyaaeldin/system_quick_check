import requests
import psutil
import os
import socket

mem_threshold=70
cpu_threshold=70
disk_threshold=70

def check_disk_status():
    disk_status=psutil.disk_usage("/").percent
    print("Disk usage:", disk_status, "%")
    return disk_status > disk_threshold


def get_public_ip():    
    ext_ip=os.popen('curl -s ifconfig.me').readline()
    print("Public IP:", ext_ip)

def check_the_cpu_usage():
    l1, l2, l3 = psutil.getloadavg()
    cpu_usage = (l3/os.cpu_count()) * 100
    print("CPU usage:", cpu_usage, "%")
    return cpu_usage > cpu_threshold

def check_mem_usage():
    mem_usage = 100 - psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    print ("MEM usage:", mem_usage, "%")
    return mem_usage > mem_threshold 

def ip_info():
    hostname=socket.gethostname()
    ip_addr=socket.gethostbyname(hostname)
    print("Priv IP:", ip_addr)

def print_hashes(word):
    print(f"============={word}==============")

def main(): 
    print_hashes("ip")
    ip_info()
    get_public_ip()
    print_hashes("==") 
    
    if check_disk_status() or check_the_cpu_usage() or check_mem_usage():
        print_hashes("==")
        print("Some thing went wrong.")
        print_hashes("==")
    else:
        print_hashes("==") 
        print("All are good!")
main()
