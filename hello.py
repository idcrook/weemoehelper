#

import pywemo
print("Discovering devices")
devices = pywemo.discover_devices()
for device in devices:
    print("-----")
    print(device)
    print(device.list_services())
    print(device.deviceinfo.GetDeviceInformation())
