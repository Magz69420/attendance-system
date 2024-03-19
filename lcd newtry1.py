from RPLCD.i2c import CharLCD
import time


def addnum():
    # Initialize LCD
    lcd=CharLCD(i2c_expander='PCF8574',address=0x27,port=1,cols=16,rows=2,dotsize=8)
    lcd.clear()
    lcd.write_string('adding machine')
    lcd.crlf()
    time.sleep(2)

    # Get input from the user
    fnum = int(input("Enter first number: "))
    snum = int(input("Enter second number: "))
    
    # Calculate sum
    sum_result = fnum + snum
    
    # Display input values and sum on LCD
    lcd.clear()
    lcd.write_string("Num1: {}".format(fnum))
    lcd.crlf()
    time.sleep(2)
    lcd.write_string("Num2: {}".format(snum))
    lcd.crlf()
    time.sleep(2)
    lcd.clear()
    lcd.write_string("Sum: {}".format(sum_result))
    time.sleep(2)

    # Print the result to the console as well
    print("The sum of {} and {} is {}".format(fnum, snum, sum_result))
    lcd.clear()
    lcd.write_string('Thankyou')
    lcd.crlf()
    time.sleep(2)

# Function call
addnum()
