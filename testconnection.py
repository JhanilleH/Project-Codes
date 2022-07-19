import os
import time
import datetime 
import motor

from gtts import gTTS
import mysql.connector
import RPi.GPIO as GPIO
from mysql.connector import Error

# The following code tests Pythons connection to mySQL



cursor = mydb.cursor()

data = ()
now = datetime.datetime.now()
x = now.replace(second=0, microsecond=0) #Replace second and millisecond

medText = 'Its time to take your medication!'
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
    

def get_data(container):
    try:
      cursor.execute("select * FROM currentuser")
      result=cursor.fetchone()
      for l in result:
          new = l.strip('(),') #Removes square brackets from incoming data
          # print(new)

      statement = "SELECT container, scheduled_pilldate, mednames, user FROM scheduledata WHERE container=%s and user=%s"
      data = (container,new)
      cursor.execute(statement,data)
      for (container, scheduled_pilldate, mednames, user) in cursor:
        global date1
        date1 = (scheduled_pilldate)
        current = (user)
        # print(current)
        
      medPill = (f"Youll be taking medication for your: {mednames}")
       
    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")
    
    if x == (date1 - datetime.timedelta(minutes = 30)):
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medAlert, lang=language, slow=False)
      myobj.save("medAlert.mp3")
      os.system("mpg321 medAlert.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

    if date1 == x:
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medNames.mp3")
      os.system("mpg321 medNames.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time

        motor.motor_pillbase()

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
              A = 1 #A is true if the beam is broken
              led_alarm()
            print("Alpha")
            motor.motor_maindoor()
            print("ABCD")
            motor.motor_pillbase()
            print("EFG")
          else:
            # print("Beam not broken")
            # motor.motor_maindoor()
            beam_time = datetime.datetime.now()
            print(beam_time)
            break   
          GPIO.output(led2, GPIO.LOW) # Turn off 
      
        while beam_brokenop():
          print("HIJ")
          # print("help")
          # if beam_brokenop():
          if beam_brokenop():
            print("KLMN")
            # motor.motor_maindoorclose()
            motor.motor_maindoor()
            motor.motor_center()

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
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))

get_data("1")

def get_data2(container):
    try:
      statement = "SELECT container, scheduled_pilldate, mednames FROM scheduledata WHERE container=%s"
      data = (container,)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames) in cursor:
        global date2
        date2 = (scheduled_pilldate)
        
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
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medNames2.mp3")
      os.system("mpg321 medNames2.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off
    
      full = 0
      if beam_broken2():
        global beam_time2

        motor.motor_pillbase()

        GPIO.output( led2, GPIO.HIGH )
        global mins, totalSecs
        global A

        A, mins, totalSecs = 0, 0, 0
        startTime = time.time()
          
        while beam_broken:
          # Calculate the time passing
          totalSecs = time.time() - startTime
          mins = totalSecs//60
          secs = int(totalSecs%60)

          if beam_broken():
            motor.motor_pillbase()
            motor.motor_maindoor()
            # print("Beam Broken")
              # main()
            if mins >= 1:
              A = 1 #A is true if the beam is broken
              led_alarm()
          else:
              # print("Beam not broken")
              motor.motor_maindoor()
              beam_time2 = datetime.datetime.now()
              print(beam_time2)
              break
        GPIO.output(led2, GPIO.LOW) # Turn off

        while beam_brokenop():
          if beam_broken():
            motor.motor_maindoorclose()
            motor.motor_maindoor()
            motor.motor_center()
                 
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
          query_med = "INSERT INTO medhistory2(initialdate, date, datedifference, medtaken, user) VALUES(%s, %s, %s, %s)"
          values = (date2, beam_time2, datediff, medsettings)

          cursor.execute(query_med, values)

          mydb.commit()
        print("The beam was broken for {} minutes {} seconds".format(mins, secs))


get_data2("2")

def get_data3(container):
    try:
      statement = "SELECT container, scheduled_pilldate, mednames FROM scheduledata WHERE container=%s"
      data = (container,)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames) in cursor:
        date3 = (scheduled_pilldate)
        
        medPill = (f"Youll be taking medication for your: {mednames}")

    except database.Error as e:
      print (f"Error retrieving entry from database: {e}")

    try:
      if x == (date3 + datetime.timedelta(minutes = -30)):
        GPIO.output( led1, GPIO.HIGH )
        main()
        myobj = gTTS(text=medAlert, lang=language, slow=False)
        myobj.save("medAlert.mp3")
        os.system("mpg321 medAlert.mp3")
        GPIO.output(led1, GPIO.LOW) # Turn off
    except Exception:
      pass
    if date3 == x:
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName3.mp3")
      os.system("mpg321 medName3.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time3

        motor.motor_pillbase()

        global mins, totalSecs
        global A

        A, mins, totalSecs = 0, 0, 0
        startTime = time.time()
        
        while beam_broken():
          # Calculate the time passing
          totalSecs = time.time() - startTime
          mins = totalSecs//60
          secs = int(totalSecs%60)

          if beam_broken():
            motor.motor_pillbase()
            motor.motor_maindoor()
            if mins >= 1:
              A = 1 #A is true if the beam is broken
              led_alarm()
          else:
              # print("Beam not broken")
              motor.motor_maindoor()
              beam_time3 = datetime.datetime.now()
              print(beam_time3)
              break
        GPIO.output(led2, GPIO.LOW) # Turn off
        
        while beam_brokenop():
          if beam_broken():
            motor.motor_maindoorclose()
            motor.motor_maindoor()
            motor.motor_center()

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

    

get_data3("3")

def get_data4(container):
    try:
      statement = "SELECT container, scheduled_pilldate, mednames FROM scheduledata WHERE container=%s"
      data = (container,)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames) in cursor:
        date4 = (scheduled_pilldate)

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
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName4.mp3")
      os.system("mpg321 medName4.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off
      print(x)

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time4

        motor.motor_pillbase()

        global mins, totalSecs
        global A

        A, mins, totalSecs = 0, 0, 0
        startTime = time.time()
          
        while beam_broken():
            # Calculate the time passing
            totalSecs = time.time() - startTime
            mins = totalSecs//60
            secs = int(totalSecs%60)

            if beam_broken():
                motor.motor_pillbase()
                motor.motor_maindoor()
                # main()
                if mins >= 1:
                  A = 1 #A is true if the beam is broken
                  led_alarm()
            else:
                # print("Beam not broken")
                motor.motor_maindoor()
                beam_time4 = datetime.datetime.now()
                print(beam_time4)
                break
            GPIO.output(led2, GPIO.LOW) # Turn off

        while beam_brokenop():
          if beam_broken():
            motor.motor_maindoorclose()
            motor.motor_maindoor()
            motor.motor_center()

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

get_data4("4")

def get_data5(container):
    try:
      statement = "SELECT container, scheduled_pilldate, mednames FROM scheduledata WHERE container=%s"
      data = (container,)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames) in cursor:
        date5 = (scheduled_pilldate)
        
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
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName5.mp3")
      os.system("mpg321 medName5.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )
      
      if beam_broken2():
        global beam_time5

        motor.motor_pillbase()
        
        global mins, totalSecs
        global A

        A, mins, totalSecs = 0, 0, 0
        startTime = time.time()
          
        while beam_broken:
          # Calculate the time passing
          totalSecs = time.time() - startTime
          mins = totalSecs//60
          secs = int(totalSecs%60)

          if beam_broken():
              motor.motor_pillbase()
              motor.motor_maindoor()
              # main()
              if mins >= 1:
                A = 1 #A is true if the beam is broken
                led_alarm()
          else:
              # print("Beam not broken")
              motor.motor_maindoor()
              beam_time5 = datetime.datetime.now()
              print(beam_time5)
              break
          GPIO.output(led2, GPIO.LOW) # Turn off

        while beam_brokenop():
          if beam_broken():
            motor.motor_maindoorclose()
            motor.motor_maindoor()
            motor.motor_center()
        
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
        
get_data5("5")

def get_data6(container):
    try:
      statement = "SELECT container, scheduled_pilldate, mednames FROM scheduledata WHERE container=%s"
      data = (container,)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames) in cursor:
        date6 = (scheduled_pilldate)

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
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName6.mp3")
      os.system("mpg321 medName6.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time6

        motor.motor_pillbase()
   
        global mins, totalSecs
        global A

        A, mins, totalSecs = 0, 0, 0
        startTime = time.time()
          
        while beam_broken:
            # Calculate the time passing
            totalSecs = time.time() - startTime
            mins = totalSecs//60
            secs = int(totalSecs%60)

            if beam_broken():
                motor.motor_pillbase()
                motor.motor_maindoor()
                # main()
                if mins >= 1:
                  A = 1 #A is true if the beam is broken
                  led_alarm()
            else:
                motor.motor_maindoor()
                print("Beam not broken")
                beam_time6 = datetime.datetime.now()
                print(beam_time6)
                break
        GPIO.output(led2, GPIO.LOW) # Turn off

        while beam_brokenop():
          if beam_broken():
            motor.motor_maindoorclose()
            motor.motor_maindoor()
            motor.motor_center()

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


get_data6("6")

def get_data7(container):
    try:
      statement = "SELECT container, scheduled_pilldate, mednames FROM scheduledata WHERE container=%s"
      data = (container,)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames) in cursor:
        date7 = (scheduled_pilldate)
        
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
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName7.mp3")
      os.system("mpg321 medName7.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time7

        motor.motor_pillbase()

        global mins, totalSecs
        global A

        A, mins, totalSecs = 0, 0, 0
        startTime = time.time()
          
        while beam_broken:
            # Calculate the time passing
            totalSecs = time.time() - startTime
            mins = totalSecs//60
            secs = int(totalSecs%60)

            if beam_broken():
                motor.motor_pillbase()
                motor.motor_maindoor()
                # main()
                if mins >= 1:
                  A = 1 #A is true if the beam is broken
                  led_alarm()
                  event.wait(20)
            else:
                motor.motor_maindoor()
                # print("Beam not broken")
                beam_time7 = datetime.datetime.now()
                print(beam_time7)
                break

            GPIO.output(led2, GPIO.LOW) # Turn off

        while beam_brokenop():
          if beam_broken():
            motor.motor_maindoorclose()
            motor.motor_maindoor()
            motor.motor_center()

        motor.motor_center()
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


get_data7("7")

def get_data8(container):
    try:
      statement = "SELECT container, scheduled_pilldate, mednames FROM scheduledata WHERE container=%s"
      data = (container,)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames) in cursor:
        date8 = (scheduled_pilldate)
         
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
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName8.mp3")
      os.system("mpg321 medName8.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time8
        
        motor.motor_pillbase()
        
        global mins, totalSecs
        global A

        A, mins, totalSecs = 0, 0, 0
        startTime = time.time()
          
        while beam_broken():
            # Calculate the time passing
            totalSecs = time.time() - startTime
            mins = totalSecs//60
            secs = int(totalSecs%60)

            if beam_broken():
                # print("Beam Broken")
                # main()
                if mins >= 1:
                  A = 1 #A is true if the beam is broken
                  led_alarm()
            else:
                # print("Beam not broken")
                beam_time8 = datetime.datetime.now()
                print(beam_time8)
                break
            GPIO.output(led2, GPIO.LOW) # Turn off

        while beam_brokenop():
          if beam_broken():
            motor.motor_maindoorclose()
            motor.motor_maindoor()
            motor.motor_center()

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

get_data8("8")

def get_data9(container):
    try:
      statement = "SELECT container, scheduled_pilldate, mednames FROM scheduledata WHERE container=%s"
      data = (container,)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames) in cursor:
        date9 = (scheduled_pilldate)
        
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
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName9.mp3")
      os.system("mpg321 medName9.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time9

        global mins, totalSecs
        global A

        A, mins, totalSecs = 0, 0, 0
        startTime = time.time()
          
        while beam_broken:
            # Calculate the time passing
            totalSecs = time.time() - startTime
            mins = totalSecs//60
            secs = int(totalSecs%60)

            if beam_broken():
                # print("Beam Broken")
                # main()
                if mins >= 1:
                  led_alarm()
                  A = 1 #A is true if the beam is broken
            else:
                # print("Beam not broken")
                beam_time9 = datetime.datetime.now()
                print(beam_time9)
                break
            GPIO.output(led2, GPIO.LOW) # Turn off

        while beam_brokenop():
          if beam_broken():
            motor.motor_maindoorclose()
            motor.motor_maindoor()
            motor.motor_center()

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

get_data9("9")

def get_data10(container):
    try:
      statement = "SELECT container, scheduled_pilldate, mednames FROM scheduledata WHERE container=%s"
      data = (container,)
      cursor.execute(statement, data)
      for (container, scheduled_pilldate, mednames) in cursor:
        date10 = (scheduled_pilldate)
        
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
      GPIO.output( led1, GPIO.HIGH )
      main()
      myobj = gTTS(text=medText, lang=language, slow=False)
      myobj.save("medtime.mp3")
      os.system("mpg321 medtime.mp3")

      myobj = gTTS(text=medPill, lang=language, slow=False)
      myobj.save("medName10.mp3")
      os.system("mpg321 medName10.mp3")
      GPIO.output(led1, GPIO.LOW) # Turn off

      GPIO.output( led2, GPIO.HIGH )

      if beam_broken2():
        global beam_time9
        
        motor.motor_pillbase()

        global mins, totalSecs
        global A

        A, mins, totalSecs = 0, 0, 0
        startTime = time.time()
          
        while beam_broken():
            # Calculate the time passing
            totalSecs = time.time() - startTime
            mins = totalSecs//60
            secs = int(totalSecs%60)

            if beam_broken():
                # print("Beam Broken")
                # main()
                if mins >= 1:
                  A = 1 #A is true if the beam is broken
                  led_alarm()
                  
            else:
                # print("Beam not broken")
                beam_time10 = datetime.datetime.now()
                print(beam_time10)
                break
            GPIO.output(led2, GPIO.LOW) # Turn off

        while beam_brokenop():
          if beam_broken():
            motor.motor_maindoorclose()
            motor.motor_maindoor()
            motor.motor_center()

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
   

get_data10("10")


exit( 0 )

mydb.close() 


