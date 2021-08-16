import clr
from System import Reflection

Reflection.Assembly.LoadFile("C:\\Program Files\\Microsoft SDKs\\Kinect\\v2.0_1409\\Assemblies\\Microsoft.Kinect.dll")

from k2py.kinectsensor import KinectSensor
import time

sensor = KinectSensor.get_default()

sensor.open()
time.sleep(5)
print(f"GOT DEFUALT KINECT 2.0: {sensor.unique_kinect_id}")
sensor.close()