from RPLCD.i2c import CharLCD
import time

# Initialize LCD
    
lcd=CharLCD(i2c_expander='PCF8574',address=0x27,port=1,cols=16,rows=2,dotsize=8)
lcd.clear()
lcd.write_string('Welcome class')
lcd.crlf()
time.sleep(2)

lcd.clear()
lcd.close(clear=True)
lcd.crlf()
