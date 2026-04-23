SmartCart Supermarket Robot Simulation (ROS + Docker)
📌 Project Overview

SmartCart is a ROS-based supermarket guide robot simulation designed to demonstrate autonomous navigation in a structured indoor environment. The system runs in a simulated supermarket environment and combines global path planning, local navigation, obstacle avoidance, and adaptive motion control.

The project is implemented using ROS Noetic inside a Docker-based virtual environment and simulates real-world robotic behavior using algorithms commonly used in autonomous systems.

🎯 Objectives
Develop a supermarket navigation robot in simulation
Implement global path planning for route optimization
Enable local navigation with dynamic obstacle avoidance
Demonstrate robot movement in a structured environment
Introduce an innovative adaptive speed control mechanism
🤖 Key Features
🗺️ Global Path Planning
Implements A* algorithm
Computes optimal path from start to goal
🚧 Local Navigation
DWA-inspired motion control logic
Real-time velocity adjustment
⚠️ Obstacle Avoidance
Detects simulated dynamic obstacles
Adjusts speed and movement accordingly
🏬 Supermarket Simulation
Custom Gazebo world representing supermarket aisles and shelves
🤖 Robot Model
Custom-designed robot:
Height: 60 cm
Radius: 50 cm
⭐ Innovation Feature
Adaptive speed control:
Faster movement in wide aisles
Slower movement in narrow aisles
🧠 Technologies Used
ROS Noetic
Python 3
Gazebo Simulator
Docker (for environment isolation)
URDF (robot modeling)
Catkin build system
📁 Project Structure
supermarket_robot/
├── launch/            # ROS launch files
├── urdf/              # Robot model (URDF)
├── worlds/            # Gazebo supermarket environment
├── scripts/           # Python control + planning scripts
├── CMakeLists.txt
├── package.xml
└── README.md
🖥️ System Requirements
🟢 Recommended OS
Ubuntu 20.04 LTS
🟡 Alternative (Windows users)
Windows 10/11 with Docker Desktop
WSL2 (optional)
📦 Required Software
ROS Noetic Desktop Full
Gazebo Simulator
Python 3.x
Catkin Tools
Docker (optional but recommended for Windows users)
Git (optional)
⚙️ Installation Guide
1. Install ROS (Ubuntu users)
sudo apt update
sudo apt install ros-noetic-desktop-full
2. Setup Catkin Workspace
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
3. Add Project
cd ~/catkin_ws/src
cp -r supermarket_robot ~/catkin_ws/src/
4. Build Project
cd ~/catkin_ws
catkin_make
source devel/setup.bash
🚀 Running the Project
▶ Start Robot Controller
rosrun supermarket_robot robot_controller.py
▶ Run Global Planner (A*)
python3 astar_planner.py
▶ Launch Simulation World
roslaunch supermarket_robot spawn_robot.launch
🐳 Docker Setup (Windows Users)
Build Image
docker build -t supermarket_ros .
Run Container
docker run -it --rm --net=host supermarket_ros
🧪 System Behavior
Robot navigates supermarket environment autonomously
Computes shortest path using A*
Adjusts movement using local navigation logic
Avoids obstacles dynamically
Adjusts speed based on aisle width
⭐ Innovation Highlight

The robot implements a context-aware speed control system:

Wide aisles → higher speed for efficiency
Narrow aisles → reduced speed for safety

This simulates real-world warehouse/supermarket navigation behavior.

⚠️ Known Limitations
Uses simulated obstacle detection (not real sensors)
Simplified DWA implementation (not full ROS Nav Stack)
Single supermarket scenario by default
📌 Future Improvements
Integration with ROS Navigation Stack (move_base/Nav2)
Real sensor simulation (LiDAR-based mapping)
Multiple supermarket scenarios
Enhanced SLAM-based mapping
👨‍💻 Author

Kangethe Alex
ROS Supermarket Robot Simulation Project

🏆 Summary

This project demonstrates core robotics concepts including:

Path planning
Autonomous navigation
Obstacle avoidance
Simulation-based robot control

It provides a strong foundation for understanding real-world autonomous robotic systems in structured environments.s
