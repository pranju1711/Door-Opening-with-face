from pyfirmata import Arduino, SERVO, util
from time import sleep

PORT = "COM3"
PIN = 9

board = Arduino(PORT)
board.digital[PIN].mode = SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(angle)
   
def doorAutomate(val):
    if val == 0:
        rotateServo(PIN, 180)  # Door open position
        print("🔓 Door Opening...")

    elif val == 1:
        rotateServo(PIN, 40)  # Door closed position
        print("🔒 Door Closing...")

    else:
        print("⚠️ Invalid input. Use 0 (open) or 1 (close).")
