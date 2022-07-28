import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import mysql.connector
from mysql.connector import Error

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/home/pi/Documents/automaticpilldispenser-bc076-firebase-adminsdk-vy3bs-b2aa601c69.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://automaticpilldispenser-bc076-default-rtdb.firebaseio.com/"})


while True:
    
    schedule = db.reference("/Automatic_Pill_Dispenser")
    users = db.reference("/Automatic_Pill_DispenserUser")
    app_users = db.reference("/Automatic_Pill_DispenserLog")
    medication = db.reference("/Automatic_Pill_DispenserMeds")

    user_values = users.get()
    schedule_values = schedule.get()
    login_values = app_users.get()
    med_values = medication.get()


    # login = login_values[Automatic_Pill_DispenserMeds]
    schedule_data = schedule_values["MedSchedule"]["true"]
    meds = med_values["Automatic_Pill_DispenserMeds"]["Meds"]
    var = schedule_data.split(',')

    for l in var:
        new = l.strip('[/]]"]["') #Removes square brackets from incoming data
        # print(new)
        container = new.split('\/') #Strip separates the string into elements of an array, it splits everywhere there is an \/
        # print (container)
        container_number, datetime_set, medication, user = container[0], container[3] + "-" + container[1] + "-" + container[2] + " " + container[4], container[5], container[6]#Container is an array, this is calling the already separated elements of the array. its how you referenece an element in a list/array. +"-" adds text between values
        user = user.strip('["\\')
        # print(user)

        # while True: pass

        mydb = mysql.connector.connect(
        host="localhost",
        user="USERS",
        password="engine451q",
        database="USERS"
        )

        mycursor = mydb.cursor()

        # if checkUsername = mycursor.execute('SELECT username FROM AppSignup WHERE username=?', (users))
        #     print('No entry to add')
            
        # for r in user:
        #     username = r.strip('\["/]')
        #     print(username)

        mycursor.execute('SELECT * FROM scheduledata WHERE container=%s', [container_number])
        result = mycursor.fetchall()

        # print(result)
        
        if result == []:
            # print(result)
            continue

        print(result[0][2],datetime_set)
        print(result[0][3],medication)
        # while True:  pass
        if result[0][2] == datetime_set and result[0][3] == medication:
            continue 
        # print(result)
        # print(container_number, datetime_set, medication, user)

        query_sch = "UPDATE scheduledata SET container=%s, scheduled_pilldate=%s, mednames=%s, user=%s WHERE container=%s"
        # collected_time = datetime.strptime(datetime_set, "%I:%M %p")
        # app_date = datetime.strftime(collected_time, "%H:%M:S")
        
        # app_date = date_format(datetime_set, '%m %d %Y %r')
        # print(app_date)
        # while True:  pass
        values = [container_number,datetime_set,medication,user,container_number]
        print(values)

        # while True: pass
        mycursor.execute(query_sch,values)

        # if result

        mydb.commit()

        # print(mycursor.rowcount, "Schedule inserted.")

    for n in meds:
        medlist = n.strip('{:')
        # print(medlist)
        
        mycursor.execute('SELECT mednames FROM medication')
        show_meds = mycursor.fetchall()

        
        query = "INSERT IGNORE INTO medication(mednames, user) VALUES (%s, %s)"
        values = [medlist,user]

        mycursor.execute(query,values)
        
        mydb.commit()

        # print(mycursor.rowcount, "Medication inserted.")

    # mycursor.execute("SELECT username FROM currentuser")
    # users = mycursor.fetchall()



    # lead3 = (list(med_values.keys()))
    # # ['Meds']
    # medicine_names = list(med_values["Meds"].keys())
    # # print(medicine_names)
    # for m in medicine_names:
    #     print(m)
        
        
    # for data in lead:
    #     print(data)
    # print(login_values)
    lead2 = (list(login_values.keys()))
    # print(lead2)
    # print(login_values)

    for logindata in lead2:
    # print(lead)
        emails = login_values[logindata]['email']
        device_num = login_values[logindata]['device_num']
        users = login_values[logindata]['username']
        passcode = login_values[logindata]['password']

        new_emails = emails.strip('"')
        new_devnum = device_num.strip('"')
        new_users = users.strip('"')
        new_passcode = passcode.strip('"')
        # print(new_emails, new_devnum, new_users, new_passcode)

        mydb = mysql.connector.connect(
        host="localhost",
        user="USERS",
        password="engine451q",
        database="USERS"
        )

        mycursor = mydb.cursor()

        # if checkUsername = mycursor.execute('SELECT username FROM AppSignup WHERE username=?', (users))
        #     print('No entry to add')
            
        # else:

        sql = "INSERT IGNORE INTO AppSignup (email,dev_num,username,password) VALUES (%s, %s, %s, %s)"
        record = (new_emails,new_devnum,new_users,new_passcode)

        try:
            mycursor.execute(sql,record)
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

        mydb.commit()

        # print(mycursor.rowcount, "record inserted.")
        # time.sleep(10)