
import platform
import pynvml
import wmi
import json

def os_version():
    os = platform.system()
    return os

def kernel_version():
    # Pc = wmi.WMI()
    # os_info = Pc.Win32_OperatingSystem()[0]
    # core = os_info.Version
    # return core
    return 1

def server_version():
    return 1

def cpu_version():
    cpu = platform.machine()
    return cpu

def bios_version():
    # Pc = wmi.WMI()
    # bios = Pc.Win32_BIOS()[0]
    # return  bios.Version
    return 1

def gpu_version():
    # gpu_type = {}
    # pynvml.nvmlInit()  # 初始化
    # deviceCount = pynvml.nvmlDeviceGetCount()  # 几块显卡
    # for i in range(deviceCount):
    #     handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    #     type = pynvml.nvmlDeviceGetName(handle)
    #     gpu_type["Device" + str(i)] = type
    #
    # pynvml.nvmlShutdown()  # 关闭
    # return  gpu_type
    return  1


def ram():
    return 1

def gpu_driver():
    # pynvml.nvmlInit()  # 初始化
    # GpuDeriveInfo = pynvml.nvmlSystemGetDriverVersion()
    # pynvml.nvmlShutdown()  # 关闭
    # return GpuDeriveInfo
    return 1



def get_basic_indicators():
    basic_indicators = {}
    basic_indicators['os_version'] = os_version()
    basic_indicators['server_kernel_version'] = kernel_version()
    basic_indicators['server_version'] = server_version()
    basic_indicators['BIOS_version'] = bios_version()
    basic_indicators['GPU_version'] = gpu_version()
    basic_indicators['CPU_version'] = cpu_version()
    basic_indicators['memory_info'] = ram()
    basic_indicators['GPU_driver'] = gpu_driver()
    info_json = json.dumps(basic_indicators, sort_keys=False, indent=4, separators=(',', ': '))
    return info_json

if __name__ == '__main__':

    # basic_indicators = {}
    # os_version = os_version()
    # basic_indicators['os_version'] = os_version
    # kernel_version = kernel_version()
    # basic_indicators['kernel_version'] = kernel_version
    # server_version = server_version()
    # basic_indicators['server_version'] = server_version
    # bios_version = bios_version()
    # basic_indicators['BIOS_version'] = bios_version
    # gpu_version = gpu_version()
    # basic_indicators['GPU_version'] = gpu_version
    # cpu_version = cpu_version()
    # basic_indicators['CPU_version'] = cpu_version
    # memory_info = ram()
    # basic_indicators['ram'] = memory_info
    # print(basic_indicators)
    # info_json = json.dumps(basic_indicators, sort_keys=False, indent=4, separators=(',', ': '))
    # print("__________________________")
    # print(info_json)
    print(get_basic_indicators())


