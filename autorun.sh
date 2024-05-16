#!/bin/sh
cd /
cd home/Denji/attendnace-system
sudo get_faces_from_camera_tkinter.py &
sudo features_extraction_to_csv.py &
attendance_taker.py

exit 0
cd /