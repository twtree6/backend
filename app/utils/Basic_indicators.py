import json
import os
import platform

import psutil
import subprocess


def os_version():
    """服务器OS版本"""
    cmd = 'cat /etc/issue'
    back = subprocess.getoutput(cmd)
    os_version = back[:-6]
    # return os_version
    return platform.platform()

def kernel_version():
    """服务器内核版本"""
    cmd = 'uname -v'
    back = subprocess.getoutput(cmd)
    kernel_version = back[3:]
    return kernel_version


def server_version():
    """服务器型号"""
    # grep 'DMI' /var/log/dmesg
    try:
        cmd = "dmidecode -s system-product-name"
        server_version = subprocess.getoutput(cmd)
        # return server_version
    except:
        server_version = "Unable to get server_version,there may not be installed dmidecode module!command:apt-get install dmidecode"
    finally:
        return server_version

def bios_version():
    """BIOS版本"""
    try:
        cmd = "dmidecode -s bios-version"
        bios_version = subprocess.getoutput(cmd)
    except:
        bios_version = "Unable to get server_version,there may not be installed dmidecode module!command:apt-get install dmidecode"
    finally:
        return bios_version


def cpu_version():
    """CPU型号"""
    try:
        cmd = "dmidecode -s processor-version"
        cpu_version = subprocess.getoutput(cmd)
    except:
        cpu_version = "Unable to get server_version,there may not be installed dmidecode module!command:apt-get install dmidecode"
    finally:
        return cpu_version

def gpu_info():
    """GPU信息"""
    cmd1 = "lshw -numeric -C display | grep -i 'product'"
    products = subprocess.getoutput(cmd1)
    # 以换行符作为分割 参数 keepends 为 False，不保留换行符，如果为 True，则保留换行符
    products = products.splitlines(keepends=False)
    cmd2 = "lshw -numeric -C display | grep -i 'vendor'"
    vendors = subprocess.getoutput(cmd2)
    vendors = vendors.splitlines(False)
    return [{'product1:': products[0][16:], 'vendor1:': vendors[0][15:]},
            {'product2:': products[1][16:], 'vendor2:': vendors[1][15:]}]

def memory_info():
    """内存信息"""
    cmd = "free -m"
    back= subprocess.getoutput(cmd)
    back1 = back.replace("\\n"," ")
    memory_info = back1.split()
    mem_total = int(memory_info[7])
    mem_used = int(memory_info[8])
    mem_free = int(memory_info[9])
    mem_buff_cache = int(memory_info[11])
    vmem_total = int(memory_info[14])
    vmem_used = int(memory_info[15])
    vmem_free = int(memory_info[16])
    physical_percent = usage_percent(mem_used, mem_total)
    return {
        "men_total": mem_total,
        "mem_used": mem_used,
        "mem_free": mem_free,
        "swap_total": vmem_total,
        "swap_used": vmem_used,
        "swap_free": vmem_free,
        "mem_used_percent(%)":physical_percent
    }

def usage_percent(use, total):
    try:
        ret = (float(use) / total) * 100
    except ZeroDivisionError:
        raise Exception("ERROR - zero division error")
    return ret

def get_gpu():
    try:
        cmd = 'radeontop -d gpu_percent.txt --limit 1'
        os.system(cmd)
        f = open('/root/test/gpu_percent.txt','r')
        file = f.readline()
        gpu_info = file.split()
        gpu_percent =gpu_info[4]
        cmd2 = 'rm -f gpu_percent.txt'
        os.system(cmd2)
    except:
        gpu_percent = "Unable to get server_version,there may not be installed dmidecode module!command:apt-get install dmidecode"
    finally:
        return gpu_percent

def disc_info():
    cmd = 'df -m'
    disc_info = subprocess.getoutput(cmd)
    return disc_info

def main():
    basic_indicators = {}
    os_version = os_version()
    basic_indicators['os_version'] = os_version
    kernel_version = kernel_version()
    basic_indicators['server_kernel_version'] = kernel_version
    server_version = server_version()
    basic_indicators['server_version'] = server_version
    bios_version = bios_version()
    basic_indicators['BIOS_version'] = bios_version
    gpu_info = gpu_info()
    basic_indicators['GPU_info'] = gpu_info
    cpu_version = cpu_version()
    basic_indicators['CPU_version'] = gpu_info
    memory_info = memory_info()
    basic_indicators['disc_info'] = memory_info

    info_json = json.dumps(basic_indicators, sort_keys=False, indent=4, separators=(',', ': '))
    print(basic_indicators)
    print("__________________________")
    print(info_json)

if __name__ == '__main__':

    # basic_indicators = {}
    # os_version = os_version()
    # print(f"OS版本信息：{os_version}")
    # kernel_version = kernel_version()
    # print(f"服务器内核版本：{kernel_version}")
    # server_version = server_version()
    # print(f"服务器型号：{server_version}")
    # bios_version = bios_version()
    # print(f"BIOS版本：{bios_version}")
    # gpu_info = gpu_info()
    # print(f"GPU信息：{gpu_info}")
    # cpu_version = cpu_version()
    # print(f"CPU版本：{cpu_version}")
    # memory_info = memory_info()
    # print(f"内存信息：{memory_info}")



    basic_indicators = {}
    os_version = os_version()
    basic_indicators['os_version'] = os_version
    kernel_version = kernel_version()
    basic_indicators['server_kernel_version']=kernel_version
    server_version = server_version()
    basic_indicators['server_version']=server_version
    bios_version = bios_version()
    basic_indicators['BIOS_version'] = bios_version
    gpu_info = gpu_info()
    basic_indicators['GPU_info']=gpu_info
    cpu_version = cpu_version()
    basic_indicators['CPU_version']=gpu_info
    memory_info = memory_info()
    basic_indicators['disc_info']=memory_info

    info_json = json.dumps(basic_indicators, sort_keys=False, indent=4, separators=(',', ': '))
    # print(basic_indicators)
    print("__________________________")
    print(info_json)



