import random
import time

robot_speed = 1.0

while True:
    obstacle = random.choice([True, False, False])

    if obstacle:
        print("Obstacle detected → slowing down")
        robot_speed = 0.2
    else:
        robot_speed = 1.0

    print("Current speed:", robot_speed)
    time.sleep(1)
