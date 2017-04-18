#!/bin/bash
roslaunch sense example.launch CAM:=1
sleep 5
roslaunch sense example.launch CAM:=2
sleep 5
roslaunch sense example.launch CAM:=3
sleep 5
roslaunch sense example.launch CAM:=4