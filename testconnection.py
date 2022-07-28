import os
import time
import datetime 
import motor
import pyrebase

from gtts import gTTS
import mysql.connector
import RPi.GPIO as GPIO
from mysql.connector import Error

# # The following code tests Pythons connection to mySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="USERS",
  password="engine451q",
  database="USERS"
)

# cursor = mydb.cursor()

# data = ()
# now = datetime.datetime.now()
# x = now.replace(second=0, microsecond=0) #Replace second and millisecond

# medText = 'Its time to take your medication!'
# medPass = 'Your medication time has passed'
# # medName1 = (f"Youre taking your: {mname1} pills" )

# medNo = 'Its not time to take your medication'
# medAlert = 'Your next medication will be ready in 30 minutes'
# medAlertError = 'You did not take your medication. Please take your medication'

# language = 'en'

# loop = 2
# delay = 1   # 1s
# led1 = 6
# led2 = 19

# beam = 16
# cont_beam = 26
# beam_sensor = False

# beam_time = datetime.datetime.now() #Captures the time, pills were removed from dispenser
# beam_time2 = datetime.datetime.now()
# beam_time3 = datetime.datetime.now()
# beam_time4 = datetime.datetime.now()
# beam_time5 = datetime.datetime.now()
# beam_time6 = datetime.datetime.now()
# beam_time7 = datetime.datetime.now()
# beam_time8 = datetime.datetime.now()
# beam_time9 = datetime.datetime.now()
# beam_time10 = datetime.datetime.now()


# looperror = 5
# buzzerPin = 5 
# delayerror = 0.5

# GPIO.setmode( GPIO.BCM )
# GPIO.setwarnings(False)

# GPIO.setup( led1, GPIO.OUT )
# GPIO.setup( led2, GPIO.OUT )
# GPIO.output( led1, GPIO.LOW )
# GPIO.output( led2, GPIO.LOW )
 
# GPIO.setup(buzzerPin, GPIO.OUT)
# GPIO.output(buzzerPin, GPIO.LOW)

# GPIO.setup(beam, GPIO.IN,pull_up_down=GPIO.PUD_UP)
# GPIO.setup(cont_beam, GPIO.IN,pull_up_down=GPIO.PUD_UP)
firebaseConfig = {
  "apiKey": "AIzaSyBx1EVwIxt_Q24m8VzRVxAYzKuPcPrKyFY",
  "authDomain": "automaticpilldispenser-bc076.firebaseapp.com",
  "databaseURL": "https://automaticpilldispenser-bc076-default-rtdb.firebaseio.com",
  "projectId": "automaticpilldispenser-bc076",
  "storageBucket": "automaticpilldispenser-bc076.appspot.com",
  "messagingSenderId": "719362689144",
  "appId": "1:719362689144:web:c0e984b70410089371058d",
  "measurementId": "G-JF1GPL2QSR"
}

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

alert = ("It's time to take your medication")

alert_data= {
    "Warnings": alert,
}

alert2 = ("Medication has not been taken")

warning_data= {
    "Warnings": alert2,
}


def led_alarm():
    GPIO.output(led1, GPIO.HIGH) # Turn on
    myobj = gTTS(text=medAlertError, lang=language, slow=False)
    myobj.save("error.mp3")
    os.system("mpg321 error.mp3")
    time.sleep(1) # Sleep for 1 second
    GPIO.output(led1, GPIO.LOW) # Turn off
    time.sleep(1) # Sleep for 1 second

def beam_broken():
    if GPIO.input(beam)==beam_sensor:
        return False
    else:
       return True

def beam_brokenop():
    if GPIO.input(beam)==beam_sensor:
        return True
    else:
       return False

def beam_broken2():
    if GPIO.input(cont_beam)==beam_sensor:
        return False
    else:
       return True
def main():
    for i in range(loop):
        GPIO.output(buzzerPin, GPIO.HIGH)  # output 3.3 V from GPIO pin
        time.sleep(delay)   # delay for 1s
        GPIO.output(buzzerPin , GPIO.LOW)  # output 0 V from GPIO pin
        time.sleep(delay)   # delay for 1s

def buzzError():
    for i in range(looperror):
        GPIO.output(buzzerPin, GPIO.HIGH)  # output 3.3 V from GPIO pin
        time.sleep(delayerror)   # delay for 1s
        GPIO.output(buzzerPin , GPIO.LOW)  # output 0 V from GPIO pin
        time.sleep(delayerror)   # delay for 1s

# def get_datauser(username):
#   try:
#     name = "SELECT username FROM currentuser WHERE username=%s"
#     user = (username,)
#     cursor.execute(name,user)
#     for (username) in cursor:
#       current_user = (name)
#   except database.Error as e:
#     print (f"Error retrieving entry from database: {e}")
# get_data("")


# print(result)
# while True:

def get_data(container):
    try:
      #  Getting the user
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
          new = l.strip('(),') #Removes square brackets from incoming data
          # print(new)
      # name = database.child("Automatic_Pill_DispenserUser").set(result)

      # Get medication schedule
      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container, new)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames, user) in cursor:
        global date1
        date1 = (scheduled_pilldate)
        current_person = (user)
        # print(current)
      # schedule = database.child("Automatic_Pill_DispenserSchedule").set(schresult)  
      medPill = (f"Youll be taking medication for your: {mednames}")
      
    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")

    try:
      # If time < 30mins away, remind the user to take the medicine
      if x == (date1 - datetime.timedelta(minutes = 30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass

    if date1 == x:
      alert = database.child("Automatic_Pill_DispenserAlerts1").set(alert_data)
      # If the time is the specified time, tell the user to take the medicine
      GPIO.output(led1, GPIO.HIGH )
      main()
      medText = (f"{current_person} Its time to take your medication!")
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medNames.mp3")
      os.system("mpg321 medNames.mp3")

      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output(led2, GPIO.HIGH)  

      if beam_broken2():
        # Check if pill is in the container
        global beam_time, full
        full=0

        # Open the door to let out the pill
        if full == 0:
          motor.pillbase_open()
          full=1
        elif full == 1:
          motor.pillbase_close()
          full = 2

        global mins, totalSecs
        global A, secs

        A, mins, totalSecs, secs = 0, 0, 0, 0
        startTime = time.time()
          
        while beam_broken():
          # Calculate the time passing
          totalSecs = time.time() - startTime
          mins = totalSecs//60
          secs = int(totalSecs%60)

          if beam_broken():
            # print("Beam Broken")
            # main()
            if mins >= 1 and A==0:
              error = database.child("Automatic_Pill_DispenserError1").set(warning_data)
              A = 1 #A is true if the beam is broken
              led_alarm()
              # schedule.every(1).minutes.do(led_alarm())
              # schedule.run_pending()
            motor.motor_maindoor()
            if full == 0:
              motor.pillbase_open()
              full=1
            elif full == 1:
              motor.pillbase_close()
              full = 2

          else:
            # print("Beam not broken")
            # motor.motor_maindoor()
            beam_time = datetime.datetime.now()
            # print(beam_time)
            break   
        GPIO.output(led2, GPIO.LOW) # Turn off 
      
        motor.turn()
        move = 0
        while move == 0:
          global average
          average = 0
          for num in range(4):
              StartTime = time.time()
              dist = motor.distance(StartTime)
              average = average + dist

          dist = average/4
          print ("Measured Distance = %.1f cm" % dist)

          if dist < 4 and dist > 0:
            motor.back()
            move = 1

        if A == 1: #if the beam is broken 

          diff = beam_time-date1
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medhistory = "Medication was not taken on schedule"
          query_in = "INSERT INTO medhistory(initialdate, date, datedifference, mednottaken, user) VALUES(%s, %s, %s, %s, %s)"
          values = (date1, beam_time, datediff, medhistory, new)

          cursor.execute(query_in, values)

          mydb.commit()
          A = 0 #reset the value
        else:
          diff = beam_time-date1
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medsettings = "Medication was taken on schedule"
          query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken, user) VALUES(%s, %s, %s, %s, %s)"
          values = (date1, beam_time, datediff, medsettings, new)

          cursor.execute(query_med, values)

          mydb.commit()

        # medrecord1 = database.child("Automatic_Pill_DispenserRecord1").set(med_rec1result)
        # medrecord2 = database.child("Automatic_Pill_DispenserRecord2").set(med_rec2result)
        # history = database.child("Automatic_Pill_DispenserHistory").set(hisresult)  
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))
# get_data("1")

def get_data2(container):
    try:
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
          new = l.strip('(),') #Removes square brackets from incoming data
          # print(new)

      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container,new)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames, user) in cursor:
        global date2
        date2 = (scheduled_pilldate)
        current_person=(user)
        
      medPill = (f"Youll be taking medication for your: {mednames}")
      
    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")
  
    try:
      if x == (date2 + datetime.timedelta(minutes = -30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass

    if date2 == x:
      alert = database.child("Automatic_Pill_DispenserAlerts2").set(alert_data)
      GPIO.output( led1, GPIO.HIGH )
      main()
      medText = (f"{current_person} Its time to take your medication!")
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medNames2.mp3")
      os.system("mpg321 medNames2.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time2, full
        full=0

        if full == 0:
          motor.pillbase_open()
          full=1
        elif full == 1:
          motor.pillbase_close()
          full = 2

        global mins, totalSecs
        global A, secs

        A, mins, totalSecs, secs = 0, 0, 0, 0
        startTime = time.time()
          
        while beam_broken:
          # Calculate the time passing
          totalSecs = time.time() - startTime
          mins = totalSecs//60
          secs = int(totalSecs%60)

          if beam_broken():
            motor.motor_maindoor()
            # print("Beam Broken")
              # main()
            if mins >= 1 and A==0:
              error = database.child("Automatic_Pill_DispenserError1").set(warning_data)
              A = 1 #A is true if the beam is broken
              led_alarm()
            motor.motor_maindoor()

            if full == 0:
              motor.pillbase_open()
              full=1
            elif full == 1:
              motor.pillbase_close()
              full = 2

          else:
            beam_time2 = datetime.datetime.now()
            print(beam_time2)
            break
        GPIO.output(led2, GPIO.LOW) # Turn off

        motor.turn()
        move = 0
        while move == 0:
          global average
          average = 0
          for num in range(4):
              StartTime = time.time()
              dist = motor.distance(StartTime)
              average = average + dist

          dist = average/4
          print ("Measured Distance = %.1f cm" % dist)

          if dist < 4 and dist > 0:
            motor.back()
            move = 1
         
        if A == 1: #if the beam is broken 
          diff = beam_time2-date2
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medhistory = "Medication was not taken on schedule"
          query_in = "INSERT INTO medhistory(initialdate, date, datedifference, mednottaken) VALUES(%s, %s, %s, %s)"
          values = (date2, beam_time2, datediff, medhistory)

          cursor.execute(query_in, values)

          mydb.commit()
          A = 0 #reset the value
        else:
          diff = beam_time2-date2
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medsettings = "Medication was taken on schedule"
          query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken) VALUES(%s, %s, %s, %s)"
          values = (date2, beam_time2, datediff, medsettings)

          cursor.execute(query_med, values)

          mydb.commit()
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))

# get_data2("2")

def get_data3(container):
    try:
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
        new = l.strip('(),') #Removes square brackets from incoming data
        # print(new)

      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container,new)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames, user) in cursor:
        global date3
        date3 = (scheduled_pilldate)
        current_person = (user)
        
      medPill = (f"Youll be taking medication for your: {mednames}")

    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")

    try:
      if x == (date3 + datetime.timedelta(minutes = 30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass

    if date3 == x:
      error = database.child("Automatic_Pill_DispenserError3").set(warning_data)
      GPIO.output( led1, GPIO.HIGH )
      main()
      medText = (f"{current_person} Its time to take your medication!")
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName3.mp3")
      os.system("mpg321 medName3.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time3, full

        full=0

        # Open the door to let out the pill
        if full == 0:
          motor.pillbase_open()
          full=1
        elif full == 1:
          motor.pillbase_close()
          full = 2

        global mins, totalSecs
        global A, secs

        A, mins, totalSecs, secs = 0, 0, 0, 0
        startTime = time.time()
        
        while beam_broken():
          # Calculate the time passing
          totalSecs = time.time() - startTime
          mins = totalSecs//60
          secs = int(totalSecs%60)

          if beam_broken():

            if mins >= 1 and A==0:
              error = database.child("Automatic_Pill_DispenserError3").set(warning_data)
              A = 1 #A is true if the beam is broken
              led_alarm()
            motor.motor_maindoor()

            # Open the door to let out the pill
            if full == 0:
              motor.pillbase_open()
              full=1
            elif full == 1:
              motor.pillbase_close()
              full = 2

          else:
            beam_time3 = datetime.datetime.now()
            print(beam_time3)
            break
        GPIO.output(led2, GPIO.LOW) # Turn off

        motor.turn()
        move = 0
        while move == 0:
          global average
          average = 0
          for num in range(4):
              StartTime = time.time()
              dist = motor.distance(StartTime)
              average = average + dist

          dist = average/4
          print ("Measured Distance = %.1f cm" % dist)

          if dist < 4 and dist > 0:
            motor.back()
            move = 1

      if A == 1: #if the beam is broken 
        diff = beam_time3-date3
        seconds = diff.total_seconds() #returns the total number of seconds
        newtime = seconds
        day = newtime // (24 * 3600)
        newtime = newtime % (24 * 3600)
        hour = newtime // 3600
        newtime %= 3600
        minutes = newtime // 60
        newtime %= 60
        seconds = newtime
        datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

        medhistory = "Medication was not taken on schedule"
        query_in = "INSERT INTO medhistory(initialdate, date, datedifference, mednottaken) VALUES(%s, %s, %s, %s)"
        values = (date3, beam_time3, datediff, medhistory)

        cursor.execute(query_in, values)

        mydb.commit()
        A = 0 #reset the value
      else:
        diff = beam_time3-date3
        seconds = diff.total_seconds() #returns the total number of seconds
        newtime = seconds
        day = newtime // (24 * 3600)
        newtime = newtime % (24 * 3600)
        hour = newtime // 3600
        newtime %= 3600
        minutes = newtime // 60
        newtime %= 60
        seconds = newtime
        datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

        medsettings = "Medication was taken on schedule"
        query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken) VALUES(%s, %s, %s, %s)"
        values = (date3, beam_time3, datediff, medsettings)

        cursor.execute(query_med, values)
      
        mydb.commit()
      print("The beam was broken for {} minutes {} seconds".format(mins, secs))

# get_data3("3")

def get_data4(container):
    try:
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
          new = l.strip('(),') #Removes square brackets from incoming data
          # print(new)

      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container,new)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames, user) in cursor:
        global date4
        date4 = (scheduled_pilldate)
        current_person = (user)

      medPill = (f"Youll be taking medication for your: {mednames}")

    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")

    try:
      if x == (date4 + datetime.timedelta(minutes = -30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass

    if date4 == x:
      alert = database.child("Automatic_Pill_DispenserAlerts4").set(alert_data)
      GPIO.output( led1, GPIO.HIGH )
      main()
      medText = (f"{current_person} Its time to take your medication!")
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName4.mp3")
      os.system("mpg321 medName4.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time4, full

        full=0

        # Open the door to let out the pill
        if full == 0:
          motor.pillbase_open()
          full=1
        elif full == 1:
          motor.pillbase_close()
          full = 2

        global mins, totalSecs
        global A, secs

        A, mins, totalSecs, secs = 0, 0, 0, 0
        startTime = time.time()
          
        while beam_broken():
            # Calculate the time passing
            totalSecs = time.time() - startTime
            mins = totalSecs//60
            secs = int(totalSecs%60)

            if beam_broken():
                
                # main()
                if mins >= 1 and A==0:
                  error = database.child("Automatic_Pill_DispenserError4").set(warning_data)
                  A = 1 #A is true if the beam is broken
                  led_alarm()
                motor.motor_maindoor()
                if full == 0:
                  motor.pillbase_open()
                  full=1
                elif full == 1:
                  motor.pillbase_close()
                  full = 2

            else:
              beam_time4 = datetime.datetime.now()
              break
        GPIO.output(led2, GPIO.LOW) # Turn off

        motor.turn()
        move = 0
        while move == 0:
          global average
          average = 0
          for num in range(4):
              StartTime = time.time()
              dist = motor.distance(StartTime)
              average = average + dist

          dist = average/4
          print ("Measured Distance = %.1f cm" % dist)

          if dist < 4 and dist > 0:
            motor.back()
            move = 1

        if A == 1: #if the beam is broken 
          diff = beam_time4-date4
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medhistory = "Medication was not taken on schedule"
          query_in = "INSERT INTO medhistory(initialdate, date, datedifference, mednottaken) VALUES(%s, %s, %s, %s)"
          values = (date4, beam_time4, datediff, medhistory)

          cursor.execute(query_in, values)

          mydb.commit()
          A = 0 #reset the value
        else:
          diff = beam_time4-date4
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medsettings = "Medication was taken on schedule"
          query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken) VALUES(%s, %s, %s, %s)"
          values = (date4, beam_time4, datediff, medsettings)

          cursor.execute(query_med, values)

          mydb.commit()
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))

# get_data4("4")

def get_data5(container):
    try:
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
          new = l.strip('(),') #Removes square brackets from incoming data
          # print(new)

      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container,new)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames, user) in cursor:
        global date5
        date5 = (scheduled_pilldate)
        current_person = (user)
        
      medPill = (f"Youll be taking medication for your: {mednames}")

    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")

    try:
      if x == (date5 + datetime.timedelta(minutes = -30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass

    if date5 == x:
      alert = database.child("Automatic_Pill_DispenserAlerts5").set(alert_data)
      GPIO.output( led1, GPIO.HIGH )
      main()
      medText = (f"{current_person} Its time to take your medication!")
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName5.mp3")
      os.system("mpg321 medName5.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )
      
      if beam_broken2():
        global beam_time5, full

        full=0

        # Open the door to let out the pill
        if full == 0:
          motor.pillbase_open()
          full=1
        elif full == 1:
          motor.pillbase_close()
          full = 2
        
        global mins, totalSecs
        global A, secs

        A, mins, totalSecs, secs = 0, 0, 0, 0
        startTime = time.time()
          
        while beam_broken:
          # Calculate the time passing
          totalSecs = time.time() - startTime
          mins = totalSecs//60
          secs = int(totalSecs%60)

          if beam_broken():

            if mins >= 1 and A==0:
              error = database.child("Automatic_Pill_DispenserError5").set(warning_data)
              A = 1 #A is true if the beam is broken
              led_alarm()
            motor.motor_maindoor()
            if full == 0:
              motor.pillbase_open()
              full=1
            elif full == 1:
              motor.pillbase_close()
              full = 2

          else:
            beam_time5 = datetime.datetime.now()
            print(beam_time5)
            break
        GPIO.output(led2, GPIO.LOW) # Turn off

        motor.turn()
        move = 0
        while move == 0:
          global average
          average = 0
          for num in range(4):
              StartTime = time.time()
              dist = motor.distance(StartTime)
              average = average + dist

          dist = average/4
          print ("Measured Distance = %.1f cm" % dist)

          if dist < 4 and dist > 0:
            motor.back()
            move = 1
        
        if A == 1: #if the beam is broken 
          diff = beam_time5-date5
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medhistory = "Medication was not taken on schedule"
          query_in = "INSERT INTO medhistory(initialdate, date, datedifference, mednottaken) VALUES(%s, %s, %s, %s)"
          values = (date5, beam_time5, datediff, medhistory)

          cursor.execute(query_in, values)

          mydb.commit()
          A = 0 #reset the value
        else:
          diff = beam_time5-date5
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medsettings = "Medication was taken on schedule"
          query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken) VALUES(%s, %s, %s, %s)"
          values = (date5, beam_time5, datediff, medsettings)

          cursor.execute(query_med, values)

          mydb.commit()
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))
        
# get_data5("5")

def get_data6(container):
    try:
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
          new = l.strip('(),') #Removes square brackets from incoming data
          # print(new)

      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container,new)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames,user) in cursor:
        global date6
        date6 = (scheduled_pilldate)
        current_person = (user)

      medPill = (f"Youll be taking medication for your: {mednames}")

    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")

    try:
      if x == (date6 + datetime.timedelta(minutes = -30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass

    if date6 == x:
      alert = database.child("Automatic_Pill_DispenserAlerts6").set(alert_data)
      GPIO.output( led1, GPIO.HIGH )
      main()
      medText = (f"{current_person} Its time to take your medication!")
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName6.mp3")
      os.system("mpg321 medName6.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time6, full

        full=0

        # Open the door to let out the pill
        if full == 0:
          motor.pillbase_open()
          full=1
        elif full == 1:
          motor.pillbase_close()
          full = 2
  
        global mins, totalSecs
        global A, secs

        A, mins, totalSecs, secs = 0, 0, 0, 0
        startTime = time.time()
          
        while beam_broken:
            # Calculate the time passing
            totalSecs = time.time() - startTime
            mins = totalSecs//60
            secs = int(totalSecs%60)

            if beam_broken():
              # main()
              if mins >= 1 and A==0:
                error = database.child("Automatic_Pill_DispenserError6").set(warning_data)
                A = 1 #A is true if the beam is broken
                led_alarm()
              motor.motor_maindoor()
              if full == 0:
                motor.pillbase_open()
                full=1
              elif full == 1:
                motor.pillbase_close()
                full = 2

            else:
              # print("Beam not broken")
              beam_time6 = datetime.datetime.now()
              print(beam_time6)
              break
        GPIO.output(led2, GPIO.LOW) # Turn off

        motor.turn()
        move = 0
        while move == 0:
          global average
          average = 0
          for num in range(4):
              StartTime = time.time()
              dist = motor.distance(StartTime)
              average = average + dist

          dist = average/4
          print ("Measured Distance = %.1f cm" % dist)

          if dist < 4 and dist > 0:
            motor.back()
            move = 1

        if A == 1: #if the beam is broken 
          diff = beam_time6-date6
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medhistory = "Medication was not taken on schedule"
          query_in = "INSERT INTO medhistory(initialdate, date, datedifference, mednottaken) VALUES(%s, %s, %s, %s)"
          values = (date6, beam_time6, datediff, medhistory)

          cursor.execute(query_in, values)

          mydb.commit()
          A = 0 #reset the value
        else:
          diff = beam_time6-date6
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medsettings = "Medication was taken on schedule"
          query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken) VALUES(%s, %s, %s, %s)"
          values = (date6, beam_time6, datediff, medsettings)

          cursor.execute(query_med, values)

          mydb.commit()
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))


# get_data6("6")

def get_data7(container):
    try:
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
          new = l.strip('(),') #Removes square brackets from incoming data
          # print(new)

      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container,new)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames,user) in cursor:
        global date7
        date7 = (scheduled_pilldate)
        current_person = (user)
        
      medPill = (f"Youll be taking medication for your: {mednames}")

    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")

    try:
      if x == (date7 + datetime.timedelta(minutes = -30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass

    if date7 == x:
      alert = database.child("Automatic_Pill_DispenserAlerts1").set(alert_data)
      GPIO.output( led1, GPIO.HIGH )
      main()
      medText = (f"{current_person} Its time to take your medication!")
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName7.mp3")
      os.system("mpg321 medName7.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time7, full

        full=0

        # Open the door to let out the pill
        if full == 0:
          motor.pillbase_open()
          full=1
        elif full == 1:
          motor.pillbase_close()
          full = 2

        global mins, totalSecs
        global A, secs

        A, mins, totalSecs, secs = 0, 0, 0, 0
        startTime = time.time()
          
        while beam_broken:
          # Calculate the time passing
          totalSecs = time.time() - startTime
          mins = totalSecs//60
          secs = int(totalSecs%60)

          if beam_broken():
            motor.motor_maindoor()
            # main()
            if mins >= 1 and A==0:
              error = database.child("Automatic_Pill_DispenserError7").set(warning_data)
              A = 1 #A is true if the beam is broken
              led_alarm()
            motor.motor_maindoor()
            if full == 0:
              motor.pillbase_open()
              full=1
            elif full == 1:
              motor.pillbase_close()
              full = 2

          else:
            beam_time7 = datetime.datetime.now()
            break
        GPIO.output(led2, GPIO.LOW) # Turn off

        motor.turn()
        move = 0
        while move == 0:
          global average
          average = 0
          for num in range(4):
              StartTime = time.time()
              dist = motor.distance(StartTime)
              average = average + dist

          dist = average/4
          print ("Measured Distance = %.1f cm" % dist)

          if dist < 4 and dist > 0:
            motor.back()
            move = 1

        if A == 1: #if the beam is broken 
          diff = beam_time7-date7
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medhistory = "Medication was not taken on schedule"
          query_in = "INSERT INTO medhistory(initialdate, date, datedifference, mednottaken) VALUES(%s, %s, %s, %s)"
          values = (date7, beam_time7, datediff, medhistory)

          cursor.execute(query_in, values)

          mydb.commit()
          A = 0 #reset the value
        else:
          diff = beam_time7-date7
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medsettings = "Medication was taken on schedule"
          query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken) VALUES(%s, %s, %s, %s)"
          values = (date7, beam_time7, datediff, medsettings)

          cursor.execute(query_med, values)

          mydb.commit()
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))

# get_data7("7")

def get_data8(container):
    try:
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
          new = l.strip('(),') #Removes square brackets from incoming data
          # print(new)

      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container,new)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames, user) in cursor:
        global date8
        date8 = (scheduled_pilldate)
        current_person = (user)
        
      medPill = (f"Youll be taking medication for your: {mednames}")

    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")

    try:
      if x == (date8 + datetime.timedelta(minutes = -30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass

    if date8 == x:
      alert = database.child("Automatic_Pill_DispenserAlerts8").set(alert_data)
      GPIO.output( led1, GPIO.HIGH )
      main()
      medText = (f"{current_person} Its time to take your medication!")
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName8.mp3")
      os.system("mpg321 medName8.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time8, full
        
        full=0

        # Open the door to let out the pill
        if full == 0:
          motor.pillbase_open()
          full=1
        elif full == 1:
          motor.pillbase_close()
          full = 2
        
        global mins, totalSecs
        global A, secs

        A, mins, totalSecs, secs = 0, 0, 0, 0
        startTime = time.time()
          
        while beam_broken():
            # Calculate the time passing
            totalSecs = time.time() - startTime
            mins = totalSecs//60
            secs = int(totalSecs%60)

            if beam_broken():
              # print("Beam Broken")
              # main()
              if mins >= 1 and A==0:
                error = database.child("Automatic_Pill_DispenserError8").set(warning_data)
                A = 1 #A is true if the beam is broken
                led_alarm()
              motor.motor_maindoor()
              if full == 0:
                motor.pillbase_open()
                full=1
              elif full == 1:
                motor.pillbase_close()
                full = 2
              
            else:
              # print("Beam not broken")
              beam_time8 = datetime.datetime.now()
              break
        GPIO.output(led2, GPIO.LOW) # Turn off

        motor.turn()
        move = 0
        while move == 0:
          global average
          average = 0
          for num in range(4):
              StartTime = time.time()
              dist = motor.distance(StartTime)
              average = average + dist

          dist = average/4
          print ("Measured Distance = %.1f cm" % dist)

          if dist < 4 and dist > 0:
            motor.back()
            move = 1

        if A == 1: #if the beam is broken 
          diff = beam_time8-date8
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medhistory = "Medication was not taken on schedule"
          query_in = "INSERT INTO medhistory(initialdate, date, datedifference, mednottaken) VALUES(%s, %s, %s, %s)"
          values = (date8, beam_time8, datediff, medhistory)

          cursor.execute(query_in, values)

          mydb.commit()
          A = 0 #reset the value
        else:
          diff = beam_time8-date8
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medsettings = "Medication was taken on schedule"
          query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken) VALUES(%s, %s, %s, %s)"
          values = (date8, beam_time8, datediff, medsettings)

          cursor.execute(query_med, values)

          mydb.commit()
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))

# get_data8("8")

def get_data9(container):
    try:
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
          new = l.strip('(),') #Removes square brackets from incoming data
          # print(new)

      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container,new)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames, user) in cursor:
        global date9
        date9 = (scheduled_pilldate)
        current_person = (user)
        
      medPill = (f"Youll be taking medication for your: {mednames}")

    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")

    try:
      if x == (date9 + datetime.timedelta(minutes = -30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass

    if date9 == x:
      alert = database.child("Automatic_Pill_DispenserAlerts9").set(alert_data)
      GPIO.output( led1, GPIO.HIGH )
      main()
      medText = (f"{current_person} Its time to take your medication!")
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName9.mp3")
      os.system("mpg321 medName9.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time9, full

        # Open the door to let out the pill
        if full == 0:
          motor.pillbase_open()
          full=1
        elif full == 1:
          motor.pillbase_close()
          full = 2

        global mins, totalSecs
        global A, secs

        A, mins, totalSecs, secs = 0, 0, 0, 0
        startTime = time.time()
          
        while beam_broken:
          # Calculate the time passing
          totalSecs = time.time() - startTime
          mins = totalSecs//60
          secs = int(totalSecs%60)

          if beam_broken():
              # print("Beam Broken")
              # main()
              if mins >= 1 and A==0:
                error = database.child("Automatic_Pill_DispenserError9").set(warning_data)
                A = 1 #A is true if the besam is broken
                led_alarm()
              motor.motor_maindoor()
              if full == 0:
                motor.pillbase_open()
                full=1
              elif full == 1:
                motor.pillbase_close()
                full = 2

          else:
            # print("Beam not broken")
            beam_time9 = datetime.datetime.now()
            break
        GPIO.output(led2, GPIO.LOW) # Turn off

        motor.turn()
        move = 0
        while move == 0:
          global average
          average = 0
          for num in range(4):
              StartTime = time.time()
              dist = motor.distance(StartTime)
              average = average + dist

          dist = average/4
          print ("Measured Distance = %.1f cm" % dist)

          if dist < 4 and dist > 0:
            motor.back()
            move = 1

        if A == 1: #if the beam is broken      
          diff = beam_time9-date9
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medhistory = "Medication was not taken on schedule"
          query_in = "INSERT INTO medhistory(initialdate, date, datedifference, mednottaken) VALUES(%s, %s, %s, %s)"
          values = (date9, beam_time9, datediff, medhistory)

          cursor.execute(query_in, values)

          mydb.commit()
          A = 0 #reset the value
        else:
          diff = beam_time9-date9
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medsettings = "Medication was taken on schedule"
          query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken) VALUES(%s, %s, %s, %s)"
          values = (date9, beam_time9, datediff, medsettings)

          cursor.execute(query_med, values)

          mydb.commit()
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))

# get_data9("9")

def get_data10(container):
    try:
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
          new = l.strip('(),') #Removes square brackets from incoming data
          # print(new)

      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container,new)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames, user) in cursor:
        global date10
        date10 = (scheduled_pilldate)
        current_person = (user)
        
      medPill = (f"Youll be taking medication for your: {mednames}")

    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")
    
    try:
      if x == (date10 + datetime.timedelta(minutes = -30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass

    if date10 == x:
      alert = database.child("Automatic_Pill_DispenserAlerts10").set(alert_data)
      GPIO.output( led1, GPIO.HIGH )
      main()
      medText = (f"{current_person} Its time to take your medication!")
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName10.mp3")
      os.system("mpg321 medName10.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time10, full
        
        full=0

        # Open the door to let out the pill
        if full == 0:
          motor.pillbase_open()
          full=1
        elif full == 1:
          motor.pillbase_close()
          full = 2

        global mins, totalSecs
        global A, secs

        A, mins, totalSecs, secs = 0, 0, 0, 0
        startTime = time.time()
          
        while beam_broken():
          # Calculate the time passing
          totalSecs = time.time() - startTime
          mins = totalSecs//60
          secs = int(totalSecs%60)

          if beam_broken():
            # print("Beam Broken")
            # main()
            if mins >= 1 and A==0:
              error = database.child("Automatic_Pill_DispenserError10").set(warning_data)
              A = 1 #A is true if the beam is broken
              led_alarm()
            motor.motor_maindoor()
            if full == 0:
              motor.pillbase_open()
              full=1
            elif full == 1:
              motor.pillbase_close()
              full = 2
                
          else:
            beam_time10 = datetime.datetime.now()
            break
        GPIO.output(led2, GPIO.LOW) # Turn off

        motor.turn()
        move = 0
        while move == 0:
          global average
          average = 0
          for num in range(4):
            StartTime = time.time()
            dist = motor.distance(StartTime)
            average = average + dist

          dist = average/4
          print ("Measured Distance = %.1f cm" % dist)

          if dist < 4 and dist > 0:
            motor.back()
            move = 1

        if A == 1: #if the beam is broken

          diff = beam_time10-date10
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medhistory = "Medication was not taken on schedule"
          query_in = "INSERT INTO medhistory(initialdate, date, datedifference, mednottaken) VALUES(%s, %s, %s, %s)"
          values = (date10, beam_time10, datediff, medhistory)

          cursor.execute(query_in, values)

          mydb.commit()
          A = 0 #reset the value
        else:
          diff = beam_time10-date10
          seconds = diff.total_seconds() #returns the total number of seconds
          newtime = seconds
          day = newtime // (24 * 3600)
          newtime = newtime % (24 * 3600)
          hour = newtime // 3600
          newtime %= 3600
          minutes = newtime // 60
          newtime %= 60
          seconds = newtime
          datediff = ("%d:%d:%d:%d" % (day, hour, minutes, seconds))

          medsettings = "Medication was taken on schedule"
          query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken) VALUES(%s, %s, %s, %s)"
          values = (date10, beam_time10, datediff, medsettings)

          cursor.execute(query_med, values)

          mydb.commit()
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))
  
# get_data10("10")

while True:
    # The following code tests Pythons connection to mySQL
  mydb = mysql.connector.connect(
    host="localhost",
    user="USERS",
    password="engine451q",
    database="USERS"
  )

  cursor = mydb.cursor()

  name_cursor = mydb.cursor()
  name_values =  "select * FROM currentuser"
  name_cursor.execute(name_values)
  name_result = name_cursor.fetchone()

  sch_cursor = mydb.cursor()
  sch_values = "SELECT container, date_format(scheduled_pilldate, '%M %d %Y %r'), mednames FROM scheduledata"
  sch_cursor.execute(sch_values)
  schresult = sch_cursor.fetchall()

  his_cursor = mydb.cursor()
  his_values = "SELECT container, date_format(scheduled_pilldate, '%M %d %Y %r'), mednames, date_format(entry_date, '%M %d %Y %r') FROM schedulehistory"
  his_cursor.execute(his_values)
  hisresult = his_cursor.fetchall()

  med_rec1_cursor = mydb.cursor()
  med_rec1_values = "SELECT date_format(initialdate, '%M %d %Y %r'), date_format(date, '%M %d %Y %r'), datedifference, mednottaken FROM medhistory"
  med_rec1_cursor.execute(med_rec1_values)
  med_rec1result = med_rec1_cursor.fetchall()

  med_rec2_cursor = mydb.cursor()
  med_rec2_values = "SELECT date_format(initialdate, '%M %d %Y %r'), date_format(date, '%M %d %Y %r'), datedifference, medtaken FROM medhistory2"
  med_rec2_cursor.execute(med_rec2_values)
  med_rec2result = med_rec2_cursor.fetchall()

  data = ()
  now = datetime.datetime.now()
  x = now.replace(second=0, microsecond=0) #Replace second and millisecond

  medPass = 'Your medication time has passed'
  # medName1 = (f"Youre taking your: {mname1} pills" )

  medNo = 'Its not time to take your medication'
  medAlert = 'Your next medication will be ready in 30 minutes'
  medAlertError = 'You did not take your medication. Please take your medication'

  language = 'en'

  loop = 2
  delay = 1   # 1s
  led1 = 6
  led2 = 19

  beam = 16
  cont_beam = 26
  beam_sensor = False

  STATE = 0
  full = 0
  once = 0

  beam_time = datetime.datetime.now() #Captures the time, pills were removed from dispenser
  beam_time2 = datetime.datetime.now()
  beam_time3 = datetime.datetime.now()
  beam_time4 = datetime.datetime.now()
  beam_time5 = datetime.datetime.now()
  beam_time6 = datetime.datetime.now()
  beam_time7 = datetime.datetime.now()
  beam_time8 = datetime.datetime.now()
  beam_time9 = datetime.datetime.now()
  beam_time10 = datetime.datetime.now()


  looperror = 5
  buzzerPin = 5 
  delayerror = 0.5

  GPIO.setmode( GPIO.BCM )
  GPIO.setwarnings(False)

  GPIO.setup( led1, GPIO.OUT )
  GPIO.setup( led2, GPIO.OUT )
  GPIO.output( led1, GPIO.LOW )
  GPIO.output( led2, GPIO.LOW )
  
  GPIO.setup(buzzerPin, GPIO.OUT)
  GPIO.output(buzzerPin, GPIO.LOW)

  GPIO.setup(beam, GPIO.IN,pull_up_down=GPIO.PUD_UP)
  GPIO.setup(cont_beam, GPIO.IN,pull_up_down=GPIO.PUD_UP)

  get_data("1")
  now = datetime.datetime.now()
  seconds = now.second
  remaining = (60-seconds)
  current_time = now.replace(second=0, microsecond=0)

  if date1 == current_time:
    time.sleep(remaining)

  get_data2("2")
  now = datetime.datetime.now()
  seconds = now.second
  remaining = (60-seconds)
  current_time = now.replace(second=0, microsecond=0)

  if date2 == current_time:
    time.sleep(remaining)

  get_data3("3")
  now = datetime.datetime.now()
  seconds = now.second
  remaining = (60-seconds)
  current_time = now.replace(second=0, microsecond=0)

  if date3 == current_time:
    time.sleep(remaining)

  get_data4("4")
  now = datetime.datetime.now()
  seconds = now.second
  remaining = (60-seconds)
  current_time = now.replace(second=0, microsecond=0)

  if date4 == current_time:
    time.sleep(remaining)

  get_data5("5")
  now = datetime.datetime.now()
  seconds = now.second
  remaining = (60-seconds)
  current_time = now.replace(second=0, microsecond=0)

  if date5 == current_time:
    time.sleep(remaining)

  get_data6("6")
  now = datetime.datetime.now()
  seconds = now.second
  remaining = (60-seconds)
  current_time = now.replace(second=0, microsecond=0)

  if date6 == current_time:
    time.sleep(remaining)

  get_data7("7")
  now = datetime.datetime.now()
  seconds = now.second
  remaining = (60-seconds)
  current_time = now.replace(second=0, microsecond=0)

  if date7 == current_time:
    time.sleep(remaining)

  get_data8("8")
  now = datetime.datetime.now()
  seconds = now.second
  remaining = (60-seconds)
  current_time = now.replace(second=0, microsecond=0)

  if date8 == current_time:
    time.sleep(remaining)

  get_data9("9")
  now = datetime.datetime.now()
  seconds = now.second
  remaining = (60-seconds)
  current_time = now.replace(second=0, microsecond=0)

  if date9 == current_time:
    time.sleep(remaining)

  get_data10("10")
  now = datetime.datetime.now()
  seconds = now.second
  remaining = (60-seconds)
  current_time = now.replace(second=0, microsecond=0)

  if date10 == current_time:
    time.sleep(remaining)

  mydb.close() 

exit( 0 )



