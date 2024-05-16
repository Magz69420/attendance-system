#!/bin/bash

cd /home/Denji/attendance-system/

# Run first script
echo "Running get_faces_from_camera_tkinter.py..."
python3 /home/Denji/attendance-system/get_faces_from_camera_tkinter.py
echo "get_faces_from_camera_tkinter.py finished."

# Run second script
echo "Running features_extraction_to_csv.py..."
python3 /home/Denji/attendance-system/features_extraction_to_csv.py
echo "features_extraction_to_csv.py finished."

# Run third script
echo "Running attendance_taker.py..."
python3 /home/Denji/attendance-system/attendance_taker.py
echo "attendance_taker.py finished."

