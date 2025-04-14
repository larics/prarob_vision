# prarob_vision
Repository with code for vision lab excercises for Robotics Practicum course

## Dependencies
ROS1/RO22 (checkout your preferred branch), OpenCV

ROS packages: usb_cam, cv_bridge

Install using: apt install ros-<distro>-usb-cam ros-<distro>-cv-bridge

OpenCV Python bindings: apt install python3-opencv

## Run the code
To check that you have a valid connection to the camera, open up one terminal and launch usb_cam package
ROS1: roslaunch usb_cam usb_cam-test.launch, camera stream will be available on topic /usb_cam/image_raw
ROS2: ros2 launch usb_cam camera.launch.py, camera stream will be available on topic /camera1/image_raw