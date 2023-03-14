#!/usr/bin/env python 
from onvif import ONVIFCamera
import datetime
import secret

dt=datetime.datetime.now()

camera_ip = secret.ip
camera_port = "8899"
wsdl_path = "/etc/onvif/wsdl"

cam = ONVIFCamera(camera_ip, camera_port, 'admin', secret.admin_password, wsdl_path)
time_request = cam.devicemgmt.create_type('SetSystemDateAndTime')
time_request.DateTimeType = "Manual"
time_request.TimeZone.TZ = 'MSK+00:00:00'
time_request.DaylightSavings = True
time_request.UTCDateTime.Date.Year = dt.year
time_request.UTCDateTime.Date.Month = dt.month
time_request.UTCDateTime.Date.Day = dt.day
time_request.UTCDateTime.Time.Hour = dt.hour
time_request.UTCDateTime.Time.Minute = dt.minute
time_request.UTCDateTime.Time.Second = dt.second
cam.devicemgmt.SetSystemDateAndTime(time_request)
