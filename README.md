# The demo package

This package contains various launch scripts to run the tracking.

## Launch files overview

### Live Tracking

file | note 
--- | ---
start_cameras.launch | Start all cameras (1,2,3,4,5)
start_aruco3_tracking.launch | Start tracking of common markers (small ones) based on [aruco](https://docs.opencv.org/trunk/d5/dae/tutorial_aruco_detection.html) version 3
start_aruco3_calibration.launch | Start tracking of calibration markers (big ones) based on [aruco](https://docs.opencv.org/trunk/d5/dae/tutorial_aruco_detection.html) version 3
start_artoolkit5_all.launch | Start tracking based on [ARToolkit](https://github.com/artoolkit/ARToolKit5) version 5
start_localization.launch | Start fusion of tracking
master_sync_cam_publish.launch | Running multimaster server

### Demonstrations

file | note 
--- | --- 
vacuum_robot_single_camera_kalman_test_play.launch | MIELE RX1 cleaning an occluded area under one camera
vacuum_robot_single_camera_kalman_test_record.launch | Recording for `vacuum_robot_single_camera_kalman_test_play.launch`
vacuum_robot_all_camera_kalman_test_play.launch | MIELE RX1 cleaning a free area under all cameras
vacuum_robot_all_camera_kalman_test_record.launch | Recording for `vacuum_robot_all_camera_kalman_test_play.launch`
free_style_all_camera_kalman_test_play.launch | Running around with a marker under all cameras (HINT: runs very slow from HDD)

![vacuum_robot_single_camera_kalman_test_play](https://github.com/cognitiveinteractiontracking/demo/raw/master/images/vacuum_robot_single_camera_kalman_test_play.png "vacuum_robot_single_camera_kalman_test_play")

![vacuum_robot_all_camera_kalman_test_play](https://github.com/cognitiveinteractiontracking/demo/raw/master/images/vacuum_robot_all_camera_kalman_test_play.png "vacuum_robot_all_camera_kalman_test_play")

### Further Examples

file | note 
--- | --- 
calibration_record.launch | relates to [calibration](https://github.com/cognitiveinteractiontracking/calibration#citrack-calibration)
hector_mapping.launch | Example for Hector mapping with a AMiRO in the CITRack
image_saver.launch | Example for saving a few images from a camera's topic

### Evaluation (depricated)

These are some evaluation files for recording and playing back tracking data.

file | note 
--- | --- 
ros_bag_play.launch | Messy launch file for playing back various recordings for trackers
ros_bag_record.launch | Messy launch file for recording trackers
tracking_record.launch | Records all tracker outputs
vicon.launch | Vicon launch file which was once used for evaluation of CITrack

## Run the tracking

- Start Kameras: TBD
- Run the TF tree of the cameras
  - Optional calibration: https://github.com/cognitiveinteractiontracking/calibration#citrack-calibration
  - Run the TFs: `roslaunch demo tf_camera.launch`
  - Load the current claibration (program should exit immediately): `roslaunch calibration calibration_load.launch`
- Start tracking: `roslaunch demo start_aruco3_tracking.launch` (Hint: `gui:=0` reduces CPU load)
- Run the fusion: `roslaunch demo start_localization.launch`
- Run multimaster: `master_sync_cam_publish.launch`
