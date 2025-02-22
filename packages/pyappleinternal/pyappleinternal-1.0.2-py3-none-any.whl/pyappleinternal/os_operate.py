import os
from pyappleinternal.lockdown import create_using_usbmux
from pyappleinternal.services.crash_reports import CrashReportsManager
from pyappleinternal.services.afc import AfcService
from pyappleinternal.services.diagnostics import DiagnosticsService
from pyappleinternal.SSHTransports import SSHTransports
from pyappleinternal.copyUnrestricted import copyUnrestricted
import platform
from pathlib import Path

if 'arm' in platform.machine().lower():
    import zeroconf._utils.ipaddress
    import zeroconf._handlers.answers

class osdevice():
    def __init__(self,udid,internal=False):
        super().__init__()
        self.udid=udid
        self.internal=internal
        self.init()
    
    def init(self):
        self.ecid=self.udid.split("-")[1]
        self.copyUnrestricted=copyUnrestricted(self.udid,self.internal)
        if self.internal==False:
            self.info=self.get_device_info()
            self.set_device_info(self.info)
        self.ssh_client=SSHTransports(self.udid)
    
    def set_device_info(self,info):
        self.mlbsn=info.get("device_info",{}).get("MLBSerialNumber","")
        self.sn=info.get("device_info",{}).get("SerialNumber",'') if info.get("device_info",{}).get("SerialNumber",'')!='' else self.mlbsn
        self.battery_level=info.get("batt",{}).get("CurrentCapacity","")
        self.hwmodel=info.get("device_info",{}).get("HardwareModel","")
        self.os_ver=info.get("device_info",{}).get("BuildVersion","")

    def shutdown(self):
        try:
            with create_using_usbmux(self.udid) as lockdown:
                ds = DiagnosticsService(lockdown)
                ds.shutdown()
            lockdown.close()
        except Exception as e:pass

    def enter_recovery(self):
        try:
            with create_using_usbmux(self.udid) as lockdown:
                lockdown.enter_recovery()
            lockdown.close()
        except Exception as e:pass

    def reboot(self):
        try:
            with create_using_usbmux(self.udid) as lockdown:
                ds = DiagnosticsService(lockdown)
                ds.restart()
            lockdown.close()
        except Exception as e:pass

    def sysdiagnose(self):
        try:
            with create_using_usbmux(self.udid) as lockdown:
                cr = CrashReportsManager(lockdown)
                cr.pull(f"{os.path.expanduser(f'~/Desktop/sysdiagnose_{lockdown.udid}')}", erase=True)
            lockdown.close()
        except Exception as e:pass

    def get_batt(self):
        try:
            with create_using_usbmux(self.udid) as lockdown:
                ds = DiagnosticsService(lockdown)
            lockdown.close()
            return ds.get_battery()
        except Exception as e:
            return {}

    def get_device_info(self):
        try:
            result_data = dict()
            with create_using_usbmux(self.udid) as lockdown:
                result_data['batt'] = self.get_batt()
                result_data['device_info'] = lockdown.all_values
            lockdown.close()
            return result_data
        except Exception as e:
            return {}