<?php
 
 // Starting the session, to use and
 // store data in session variable
 session_start();
   
 // If the session variable is empty, this
 // means the user is yet to login
 // User will be sent to 'login.php' page
 // to allow the user to login
 if (!isset($_SESSION['username'])) {
     $_SESSION['msg'] = "You have to log in first";
     header('location: login.php');
 }
   
 // Logout button will destroy the session, and
 // will unset the session variables
 // User will be headed to 'login.php'
 // after logging out
 if (isset($_GET['logout'])) {
     session_destroy();
     unset($_SESSION['username']);
     header("location: login.php");
 }
 ?>


<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8"> 
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Automatic Pill Dispenser</title>
        <link rel="stylesheet" href="css/main.css">

    </head>

    <body>
        <div class="toppane">
            <div class="container">
                <a class="logo" href="index.php">Automatic<span>PillDispenser</span></a>

                <img id="mobile-cta" class="mobile-menu" src="images/menu.svg" alt="For mobile website">

                <nav>
                    <img id="mobile-exit" class="mobile-menu-exit" src="images/exit.svg" alt="Close navigation">
                    <ul class="navigation1">
                        <li class="Home"><a href="index.php">Home</a></li>
                        <li><a href="med.html">Medication</a></li>
                        <li><a href="medschedule.php">Schedule</a></li>
                       
                    </ul>

                    <ul class="navigation2">
                        <li class="gotomedication-history"><a href="medication history.html">Medication History</a></li>
                    </ul>
                    <a href="index.php?logout='1'">LOGOUT</a>
                </nav>

            </div>
            
        </div>
        <div class="content">
         <!-- Notification given when users log in-->
            <?php if (isset($_SESSION['success'])) : ?>
                <div class="error success" >
                    <h3>
                        <?php
                            echo $_SESSION['success'];
                            unset($_SESSION['success']);
                        ?>
                    </h3>
                </div>
            <?php endif ?>
  
            <!-- welcome message for users-->
            <?php  if (isset($_SESSION['username'])) : ?>     
            <p>
                    <strong>
                    Welcome
                        <?php echo $_SESSION['username']; ?>
                    </strong>
            </p>
        </div>
       
        <section class="hero">
            <div class="container">
                <div class="left-col">
                    <p class="subhead">ADP3.0</p>
                    
                    <div class="hero-cta">
                        <a href="med.html" class="navigation-cta">Set Medication List</a>
                        <a href="medschedule.php" class="Set-schedule-cta">
                            <img src="images/iconmonstr-calendar-7.svg" class="hero-img" alt="Set Scedule">Set Patient Schedule
                        </a>
                    </div>
                 </div>
            </div>
        </section>
       

        <div id="DigitalCLOCK" class="clock" onload="showTime()"></div>
        <div id="CurrentDate" class="date" ></div>

        <script>

            const mobileBtn = document.getElementById('mobile-cta')
                nav = document.querySelector('nav')
                mobileBtnExit = document.getElementById('mobile-exit');

            mobileBtn.addEventListener('click', () => {
                nav.classList.add('menu-btn');
            })

            mobileBtnExit.addEventListener('click', () => {
                nav.classList.remove('menu-btn');
            })

            //This function retrieves the current time on your computer and displays it in the browser.
            function showTime(){
            
                const days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
                const months = ["January","February","March","April","May","June","July","August","September","October","November","December"]; 
            var date = new Date();
            var h = date.getHours(); 
            var m = date.getMinutes(); 
            var s = date.getSeconds(); 
            var dd = days[date.getUTCDay()];
            var day = date.getUTCDate();
            var month = months[date.getUTCMonth()];
            var year = date.getUTCFullYear();
            var session = "AM";
            
            if(h == 0){
                h = 12;
            }
            
            if(h > 12){
                h = h - 12;
                session = "PM";
            }
            
            h = (h < 10) ? "0" + h : h;
            m = (m < 10) ? "0" + m : m;
            s = (s < 10) ? "0" + s : s;
            
            var time = h + ":" + m + ":" + s + " " + session;
            var cal =  dd + ", " + month + " " + day+", " + year;

            document.getElementById("DigitalCLOCK").innerText = time;
            document.getElementById("CurrentDate").innerText = cal;
            
            setTimeout(showTime, 1000);
        
            }
    
            showTime();

           

        </script>

    <?php endif ?>
  </body>
</html>