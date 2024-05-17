import os
from RPLCD.i2c import CharLCD
import time

# Initialize LCD
    
lcd=CharLCD(i2c_expander='PCF8574',address=0x27,port=1,cols=16,rows=2,dotsize=8)
def get_faces_from_camera_tkinter():
    os.system('python get_faces_from_camera_tkinter.py')

def features_extraction_to_csv():
    os.system('python features_extraction_to_csv.py')

def attendance_taker():
    os.system('python attendance_taker.py')

def main():
    # Initialize LCD
    lcd = CharLCD('PCF8574', 0x27)
    
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Select option:")

    options = [
        "1. Get Faces",
        "2. Features Extraction",
        "3. Attendance Taker"
    ]

    for option in options:
        lcd.cursor_pos = (options.index(option) + 1, 0)
        lcd.write_string(option)

    choice = input("Enter the number of the option you want to run: ")

    if choice == '1':
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Option 1 selected")
        get_faces_from_camera_tkinter()
    elif choice == '2':
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Option 2 selected")
        features_extraction_to_csv()
    elif choice == '3':
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Option 3 selected")
        attendance_taker()
    else:
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Invalid choice")

if __name__ == "__main__":
    main()