# Project 1, ROS Tutorials

__Michigan Tech EE5531 Intro to Robotics, January 15th, 2026__

## About the package(s)

- __iqmattso_package__ - A new CMake package with a "hello world" executable called `iqmattso_node`, following the "create a package" [ROS2 Jazzy Tutorial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html).
- __iqmattso_py_pubsub__ - A Python package with a simple publisher/subscriber (talker/listener) example from the [ROS2 Jazzy Docs](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html#writing-a-simple-publisher-and-subscriber-python), implemented with Python.

## Requirements

The __iqmattso_py_pubsub__ pacakge requires the following dependencies:
- rclpy
- std_msgs

All dependencies can be installed via the following command ran at the root of the workspace (ros2_ws):

```
$ rosdep install -i --from-path src --rosdistro jazzy -y
```

## Instructions

First, create a new ROS2 workspace on an Ubuntu 24.04 PC with ROS2 Jazzy installed:

```
$ mkdir -p ros2_ws/src
```
Then, navigate into the src directory and clone the repo:
```
$ cd ros2_ws/src
$ git clone git@github.com:iqmattso/EE5531-iqmattso-project1.git
```
Colcon build the ROS2 packages, and source the workspace:
```
$ cd ros2_ws
$ colcon build
$ source install/setup.bash
```

Now, to verify the __iqmattso_package__ is working and setup correctly, run the `iqmattso_node`:
```
$ ros2 run iqmattso_package iqmattso_node
```
Which should output the following:
```
hello world iqmattso_package package
```

To test the talker/listener example in the __iqmattso_py_pubsub__ package, source the workspace in two terminals and run the talker and listener simultaneously in two separate terminals:

Terminal 1:
```
$ cd ros2_ws
$ source install/setup.bash
$ ros2 run iqmattso_py_pubsub talker
```
Which should print out logs that print strings "Hello World: 0" where the counter increases with each message published.

Terminal 2:
```
$ cd ros2_ws
$ source install/setup.bash
$ ros2 run iqmattso_py_pubsub listener
```
Which prints out "I heard: "Hello World: 0""

### Alternate talker/listener example:

An alternate pubsub node that publsihes "I can count to: 0" instead of "Hello World: 0" on the `alternate_pubsub` branch.

To run this version of the talker, navigate to the root of the git repo, switch branches, and rebuild the packages with colcon build:

```
$ cd ros2_ws/src/EE5531-iqmattso-project1
$ git checkout alternate_pubsub
$ cd ros2_ws
$ colcon build
$ source install/setup.bash
$ ros2 run iqmattso_py_pubsub talker
```
