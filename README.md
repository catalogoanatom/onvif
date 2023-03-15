# onvif
onvif scripts
https://www.onvif.org/onvif/ver10/device/wsdl/devicemgmt.wsdl
https://stepik.org/lesson/57505/step/1

## need link to  
ln -s /etc/onvif/wsdl

onvif-cli --host  192.168.1.18 --port 8899 -u admin -a CAMPASSWORD -w /etc/onvif/wsdl

cmd press tab

### ex:
cmd devicemgmt GetDeviceInformation

