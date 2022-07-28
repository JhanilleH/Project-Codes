#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
 
din1 = 8
din2 = 11
din3 = 7
din4 = 10

GPIO_TRIGGER = 2
GPIO_ECHO = 20

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002
 
step_count = 1638 # 5.625*(1/64) per step, 4096 steps is 360°
 
direction = False # True for clockwise, False for counter-clockwise
 
# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]
 
# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings(False)
GPIO.setup( din1, GPIO.OUT )
GPIO.setup( din2, GPIO.OUT )
GPIO.setup( din3, GPIO.OUT )
GPIO.setup( din4, GPIO.OUT )
 
# initializing
GPIO.output( din1, GPIO.LOW )
GPIO.output( din2, GPIO.LOW )
GPIO.output( din3, GPIO.LOW )
GPIO.output( din4, GPIO.LOW )
 
global motor_pins
global motor_step_counter 

motor_pins = [din1,din2,din3,din4]
motor_step_counter = 0 ;

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

STATE = 0

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
def cleanup():
    GPIO.output( din1, GPIO.LOW )
    GPIO.output( din2, GPIO.LOW )
    GPIO.output( din3, GPIO.LOW )
    GPIO.output( din4, GPIO.LOW )
    GPIO.cleanup()


motor_pins = [din1,din2,din3,din4]
                
def forward():
    motor_step_counter = 0 
    i = 0
    for i in range(step_count):
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction==True:
            motor_step_counter = (motor_step_counter - 1) % 8
        elif direction==False:
            motor_step_counter = (motor_step_counter + 1) % 8
        else: # defensive programming
            print( "uh oh... direction should *always* be either True or False" )
            cleanup()
            exit( 1 )
        time.sleep( step_sleep )
    



def back():
    motor_step_counter = 0 
    i = 0
    for i in range(step_count):
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction==False:
            motor_step_counter = (motor_step_counter - 1) % 8
        elif direction==True:
            motor_step_counter = (motor_step_counter + 1) % 8
        else: # defensive programming
            print( "uh oh... direction should *always* be either True or False" )
            cleanup()
            exit( 1 )
        time.sleep( step_sleep )
    

if __name__ == '__main__':

    while True:
        dist = distance()
        print ("Measured Distance = %.1f cm" % dist)
        
        if dist > 4:
            continue

        if STATE == 0:
            forward()
        else:
            back()
        
        STATE = not STATE