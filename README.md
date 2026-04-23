# 🛒 SmartCart Supermarket Robot Simulation (ROS + Docker)

## 📌 Project Overview
This project is a ROS-based simulation of a supermarket guide robot running inside a Docker-based virtual environment. The robot is designed to navigate a supermarket environment using path planning, obstacle avoidance, and adaptive motion control.

---

## 🤖 Features

- 🗺️ Supermarket environment simulation (Gazebo world)
- 🤖 Custom robot model (60cm height, 50cm radius)
- 🧭 Global path planning using A* algorithm
- 🚧 Local navigation using DWA-style logic (simulated)
- ⚡ Obstacle avoidance system (dynamic interference simulation)
- ⭐ Innovation feature:
  - Robot moves faster in wide aisles
  - Robot slows down in narrow aisles

---

## 🧠 Algorithms Used

- A* Path Planning (global navigation)
- DWA (Dynamic Window Approach – simplified implementation)
- Rule-based obstacle avoidance
- Velocity adaptation control system

---

## 🏗️ System Architecture

- ROS Noetic (core middleware)
- Docker (virtual environment)
- Python (control logic)
- Gazebo world (supermarket simulation)
- URDF (robot modeling)

---

## 🚀 How to Run

### 1. Build workspace
```bash
catkin_make
source devel/setup.bash
