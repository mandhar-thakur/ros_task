# ROS Turtlesim Session

This package provides scripts to control the Turtlesim simulation.

## Installation

1. **Install the Turtlesim Package**

    ```bash
    sudo apt-get install ros-noetic-turtlesim
    ```

2. **Clone this Repository in a Catkin Workspace**

    ```bash
    mkdir -p ros_ws/src
    cd ros_ws/src
    git clone https://github.com/topguns837/ros_session.git
    ```

3. **Compile the Workspace and Source the Setup File**

    ```bash
    cd ~/ros_ws
    catkin_make
    source devel/setup.bash
    ```

## Instructions to Run the Code

1. **Start ROS Core** (Terminal 1)

    ```bash
    roscore
    ```

2. **Launch Turtlesim** (Terminal 2)

    ```bash
    rosrun turtlesim turtlesim_node
    ```

3. **Run the Move Script** (Terminal 3)

    ```bash
    rosrun ros_session move_rectangle.py
    ```

Follow these instructions to simulate the turtle’s movement in a Rectangle.
