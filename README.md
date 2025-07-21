# weemoehelper


Use [pywemo][pywemo] library to maintain Belkin WeMo devices past their expiration date.

## hello

```shell
source ../pywemo/.venv/bin/activate
python hello.py
```

```
Discovering devices
-----
<WeMo Switch "Living Room Reading Lights">
['WiFiSetup', 'timesync', 'basicevent', 'firmwareupdate', 'rules', 'metainfo', 'remoteaccess', 'deviceinfo', 'smartsetup', 'manufacture']
{'DeviceInformation': '24FDEEADBEEFC|WeMo_WW_2.00.11111.PVT-OWRT-SNSV2|1|49154|0|Living Room Reading Lights', 'Payload': 'X-HM://007JKJKJKJK', 'HKSetupState': '0', 'CountdownTime': '0'}
-----
<<< 8-< ... >-8 >>>
```



---
[pywemo]: https://github.com/pywemo/pywemo
