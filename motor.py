#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

in1 = 17
in2 = 18
in3 = 27
in4 = 22
 
din1 = 8
din2 = 11
din3 = 7
din4 = 10

min1 = 12
min2 = 25
min3 = 23
min4 = 13

GPIO_TRIGGER = 2
GPIO_ECHO = 20

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002

step_countpilldoor = 600 # 5.625*(1/64) per step, 4096 steps is 360°
step_countdoor = 1780 # 5.625*(1/64) per step, 4096 steps is 360°
step_countcontainer = 410 #36°

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

GPIO.setup( min1, GPIO.OUT )
GPIO.setup( min2, GPIO.OUT )
GPIO.setup( min3, GPIO.OUT )
GPIO.setup( min4, GPIO.OUT )

GPIO.setup( in1, GPIO.OUT )
GPIO.setup( in2, GPIO.OUT )
GPIO.setup( in3, GPIO.OUT )
GPIO.setup( in4, GPIO.OUT )
 
# initializing
GPIO.output( din1, GPIO.LOW )
GPIO.output( din2, GPIO.LOW )
GPIO.output( din3, GPIO.LOW )
GPIO.output( din4, GPIO.LOW )

GPIO.output( min1, GPIO.LOW )
GPIO.output( min2, GPIO.LOW )
GPIO.output( min3, GPIO.LOW )
GPIO.output( min4, GPIO.LOW )

GPIO.output( in1, GPIO.LOW )
GPIO.output( in2, GPIO.LOW )
GPIO.output( in3, GPIO.LOW )
GPIO.output( in4, GPIO.LOW )

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

STATE = 0
full = 0
once = 0 #Initialized outside the function in order to reset it to next state

def distance(myStartingTime):
    calculation_starting_time = time.time()
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        calculation_starting_time = time.time()
        if calculation_starting_time - myStartingTime > 1:
            break
            
        StartTime = time.time()
        # print("girl")
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        calculation_starting_time = time.time()
        if calculation_starting_time - myStartingTime > 1:
            break
        StopTime = time.time()
        # print("boy")
 
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

    GPIO.output( min1, GPIO.LOW )
    GPIO.output( min2, GPIO.LOW )
    GPIO.output( min3, GPIO.LOW )
    GPIO.output( min4, GPIO.LOW )

    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()

def pillbase_open():
    try:
        motor_pins = [in1,in2,in3,in4]
        motor_step_counter = 0 
        i = 0
        for i in range(step_countpilldoor):
            for pin in range(0, len(motor_pins)):
                GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
            if direction==False:
                motor_step_counter = (motor_step_counter - 1) % 8
            elif direction==True:
                motor_step_counter = (motor_step_counter + 1) % 8
                    # GPIO.output( led1, GPIO.HIGH )
            else: # defensive programming
                print( "uh oh... direction should *always* be either True or False" )
                cleanup()
                exit( 1 )
            time.sleep( step_sleep )

    except KeyboardInterrupt:
        cleanup()
        exit( 1 )

def pillbase_close():
    try:
        motor_pins = [in1,in2,in3,in4]
        motor_step_counter = 0 
        i = 0
        for i in range(step_countpilldoor):
            for pin in range(0, len(motor_pins)):
                GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
            if direction==True:
                motor_step_counter = (motor_step_counter - 1) % 8
            elif direction==False:
                motor_step_counter = (motor_step_counter + 1) % 8
                    # GPIO.output( led1, GPIO.HIGH )
            else: # defensive programming
                print( "uh oh... direction should *always* be either True or False" )
                cleanup()
                exit( 1 )
            time.sleep( step_sleep )

    except KeyboardInterrupt:
        cleanup()
        exit( 1 )

def turn():
    try:
        motor_pins = [min1,min2,min3,min4]
        motor_step_counter = 0 
        i = 0
        for i in range(step_countcontainer):
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
    
    except KeyboardInterrupt:
        cleanup()
        exit( 1 )

def close():
    try:
        motor_pins = [min1,min2,min3,min4]
        motor_step_counter = 0 
        i = 0
        for i in range(step_countpill):
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
    
    except KeyboardInterrupt:
        cleanup()
        exit( 1 )
                
def forward():
    motor_step_counter = 0 
    motor_pins = [din1,din2,din3,din4]
    i = 0
    for i in range(step_countdoor):
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

def back():
    motor_step_counter = 0 
    motor_pins = [din1,din2,din3,din4]
    i = 0
    for i in range(step_countdoor):
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
    
def motor_maindoor():
    global STATE

    StartTime = time.time()
    dist = distance(StartTime)
    print ("Measured Distance = %.1f cm" % dist)
    
    # if dist > 4:
    #     continue
    if dist < 4 and dist > 0:
        
        if STATE == 0:
            forward()
        else:
            back()
        
        STATE = not STATE

# def motor_maindoorclose():
    
#     global STATE
#     while True:

#         dist = distance()
#         print ("Measured Distance = %.1f cm" % dist)
        
#         # if dist > 4:
#         #     continue
#         if dist < 4:
            
#             if STATE == 0:
#                 forward()
#             else:
#                 back()
                
#             STATE = not STATE
#             break

def motor_center():
    global once #Global variable so it can be changed outside the function when restting

    if once == 0:
        turn()
        once=1

def motor_pillbase():
    global full 

    if full == 0:
        pillbase_open()
        full=1
    elif full == 1:
        pillbase_close()
        full = 2
    
if __name__ == '__main__':

    # while True:
        motor_maindoor()
    # motor_maindoorclose()
        motor_center()
        motor_pillbase()