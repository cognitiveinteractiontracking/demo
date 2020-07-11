#!/bin/bash

set -e
if [[ $1 == "" ]]; then
	echo "ERROR: Specify absolute bag file location"
	exit
fi
if [[ $2 == "" ]]; then
	echo "ERROR: Specify TOPIC name (e.g. /my/topic) which publishes image data"
	exit
fi
if [[ $3 == "" ]]; then
	echo "ERROR: Specify FPS for the resulting video"
	exit
fi
if [[ $4 == "" ]]; then
	echo "ERROR: Specify the final resolution"
	echo "4x3 (480p) ratio: 640:480"
	echo "5x4 ratio: 2560:2048 or 1280:1024 or 640:512"
	exit
fi
if [[ $5 == "" ]]; then
	echo "ERROR: Specify temporary folder for images"
	exit
fi

F=$1
TOPIC="$2"
# Workfolder
TMP="$5"
W="${TMP}/${F}.images/${TOPIC}"
C=$PWD
rm -rf $W
mkdir -p $W

ENC="bgr8"
RATE=$3
FORMAT="jpg" # 'jpg' ,'png', 'pgm' 

# Start an image saver for every image_raw stream
echo "Store images to $W"

# Extract every image
rosrun demo bag_topic_to_image.py $W $F $TOPIC 0 $FORMAT

# Convert images to video
RATIO=$4
echo "ffmpeg -y -framerate $RATE -i ${W}/%06d.jpg -c:v libx264 -vf scale=$RATIO $F$(echo $TOPIC | tr '/' '_').mp4"
ffmpeg -y -framerate $RATE -i ${W}/%06d.jpg -c:v libx264 -vf scale=$RATIO $F$(echo $TOPIC | tr '/' '_').mp4
