# How to convert

- Extract images: rosrun demo bag_to_image.py <folder> <bagfile> <topic> 0 jpg
- Check frame rate via `rosbag play <bagfile>` and `rostopic hz <topic>`
- Choose scale (5x4): 2560x2048 or 1280x1024 or 640x512
- Convert: ffmpeg -framerate 20 -i /<folder>/<topic>-%06d.jpg -c:v libx264 -vf scale=640:512 <bagfile>_<topic>.mp4
