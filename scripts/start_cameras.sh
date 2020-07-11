#!/bin/bash
roslaunch genicam_cvb example.launch CAM:=1
sleep 5
roslaunch genicam_cvb example.launch CAM:=2
sleep 5
roslaunch genicam_cvb example.launch CAM:=3
sleep 5
roslaunch genicam_cvb example.launch CAM:=4
