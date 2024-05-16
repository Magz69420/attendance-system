#!/bin/sh
cd /
cd home/Denji/attendnace-system
sudo python get_faces_from_camera_tkinter.py &
sudo python features_extraction_to_csv.py &
sudo python attendance_taker.py &

exit 0
cd /