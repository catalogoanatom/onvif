from onvif import ONVIFCamera, ONVIFService, ONVIFError
import secret
cam_url="http://"+secret.ip+"/onvif/media"
management_service = ONVIFService(cam_url, u'admin', secret.admin_password, u'/etc/onvif/wsdl/devicemgmt.wsdl')
services = management_service.GetServices({'IncludeCapability': True})

