import time
import pyrebase
import datetime
import sys
import os
import mysql.connector

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

# alert = ("It's time to take your medication")

# alert_data= {
#     "Warnings": alert,
# }

# alert2 = ("Medication has not been taken")

# warning_data= {
#     "Warnings": alert2,
# }

# alert = database.child("Automatic_Pill_DispenserAlerts").set(alert_data)
# error = database.child("Automatic_Pill_DispenserError").set(warning_data)

# The following code tests Pythons connection to mySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="USERS",
  password="engine451q",
  database="USERS"
)

while True:
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

  name = database.child("Automatic_Pill_DispenserUser").set(name_result)
  schedule = database.child("Automatic_Pill_DispenserSchedule").set(schresult)
  history = database.child("Automatic_Pill_DispenserHistory").set(hisresult)
  medrecord1 = database.child("Automatic_Pill_DispenserRecord1").set(med_rec1result)
  medrecord2 = database.child("Automatic_Pill_DispenserRecord2").set(med_rec2result)

  time.sleep(15)