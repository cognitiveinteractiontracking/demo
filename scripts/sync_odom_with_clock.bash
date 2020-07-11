!#/bin/bash

roslaunch demo sync_odom_with_clock.launch
rosrun merge_bags.py cam12345_miele_2018-10-01-11-28-12.sync_aruco.bag cam12345_miele_2018-10-01-11-28-12.sync_aruco_1.bag cam12345_miele_2018-10-01-11-28-12.sync_aruco_2.bag cam12345_miele_2018-10-01-11-28-12.sync_aruco_3.bag cam12345_miele_2018-10-01-11-28-12.sync_aruco_4.bag
