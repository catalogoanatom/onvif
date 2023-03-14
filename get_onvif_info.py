#!/usr/bin/env python
from onvif import ONVIFCamera, ONVIFService, ONVIFError
import secret

camera = ONVIFCamera(secret.ip, 8899, u'admin', secret.admin_password, u'/etc/onvif/wsdl/')

response = camera.devicemgmt.GetDeviceInformation()
print(response)

response = camera.devicemgmt.GetServices()
print(response)

response = camera.devicemgmt.GetSystemDateAndTime()
print(response)



