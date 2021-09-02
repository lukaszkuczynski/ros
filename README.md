# ROS projects
This is repo to gather ROS - Robot Operating System - projects.


## rpi test with servo
Raspberry PI with servo SG90 was installed.
Image from Ubiquity with Ubuntu 16 has been put to the SD card (https://www.ubiquityrobotics.com/raspberry-pi-images/)

When a server for servo is running on RPi

```
rosrun rpi_luk_ros_tutorials servo_server.py 
```

We can steer it with basic commands from any machine that has ROS installed and can connect via network. F.e. from my local PC I was able to reach it. To make it you have to change `ROS_MASTER_URI` as indicated in 

First it's good to check if topic is visible
```
rostopic list
```
you should seee `/servo_position` among others.

Then to move servo if a server is running just send some String commands, like `left`, `neutral` or `right`, f.e.

```
rostopic pub /servo_position std_msgs/String "data: 'right'"
```