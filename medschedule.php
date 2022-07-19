<?php

$serverName = "";
    $userName = "";
    $password = "";
    $dbName = "";
$column_name = "mednames";
$table = "medication";

$conn = mysqli_connect($serverName, $userName, $password, $dbName);
$query1="SELECT * FROM $table";
$ans1=mysqli_query($conn, $query1);

$query2="SELECT * FROM $table";
$ans2=mysqli_query($conn, $query2);

$query3="SELECT * FROM $table";
$ans3=mysqli_query($conn, $query3);

$query4="SELECT * FROM $table";
$ans4=mysqli_query($conn, $query4);

$query5="SELECT * FROM $table";
$ans5=mysqli_query($conn, $query5);

$query6="SELECT * FROM $table";
$ans6=mysqli_query($conn, $query6);

$query7="SELECT * FROM $table";
$ans7=mysqli_query($conn, $query7);

$query8="SELECT * FROM $table";
$ans8=mysqli_query($conn, $query8);

$query9="SELECT * FROM $table";
$ans9=mysqli_query($conn, $query9);

$query10="SELECT * FROM $table";
$ans10=mysqli_query($conn, $query10);

?> 

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
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
                <li><a href="meed.html">Medication</a></li>
                <li><a href="medschedule.php">Schedule</a></li>
               
            </ul>

            <ul class="navigation2">
                <li class="gotomedication-history"><a href="medication history.html">Medication History</a></li>
            </ul>
        </nav>
    </div>
</div>




<section class="Scheduling">

    <h1>Schedule log</h1>
    <h4>Enter Patient Medication Schedule</h5>
    <div class="forms">   
    <form action="schedule.php" style="margin-bottom:-10;">
            <input type="Submit" value="View Schedule">
        </form>
</div>
    <form action="backend/scheduledata.php" method="post" style="margin-top:-5;">
        <label for="contname"><b>Pill Container</b></label>
        <label for="contname1"><b>1</b></label><br>
        <input type="datetime-local" name="scheduled_pilldate1" style="width: 300px; height: 70px;" >
        <br>
        <label for="mednames">Choose medication(s)</label><br>
        <select name="mednames1[]" multiple="multiple" id="current_select">
            <option style="width: 280px; height: 10px;"></option>

                <?php

                    if($ans1) {
                        while($row=mysqli_fetch_array($ans1)) {
                            $mednames=$row["$column_name"];
                            echo"<option>$mednames<br></option>";
                        }
                    }
	

                ?>
        </select><br>______________________________________________________________________________</br><p>

        <label for="contname"><b>Pill Container<b></label>
        <label for="contname2"><b>2</b></label><br>
        <input type="datetime-local" name="scheduled_pilldate2" style="width: 300px; height: 70px;">   
        <br>
        <label for="mednames">Choose medication(s)</label><br>
        <select name="mednames2[]" multiple="multiple" id="current_select">
            <option style="width: 280px; height: 10px;"></option>

                <?php

                    if($ans2) {
                        while($row=mysqli_fetch_array($ans2)) {
                            $mednames=$row["$column_name"];
                            echo"<option>$mednames<br></option>";
                        }
                    }

                ?>
        </select><br>______________________________________________________________________________</br><p> 

        <label for="contname"><b>Pill Container<b></label>
        <label for="contname3"><b>3</b></label><br>
        <input type="datetime-local" name="scheduled_pilldate3" style="width: 300px; height: 70px;">   
        <br>
        <label for="mednames">Choose medication(s)</label><br>
        <select name="mednames3[]" multiple="multiple" id="current_select">
            <option style="width: 280px; height: 10px;"></option>

                <?php

                    if($ans3) {
                        while($row=mysqli_fetch_array($ans3)) {
                            $mednames=$row["$column_name"];
                            echo"<option>$mednames<br></option>";
                        }
                    }

                ?>
        </select><br>______________________________________________________________________________</br><p>   

        <label for="contname"><b>Pill Container<b></label>
        <label for="contname4"><b>4</b></label><br>
        <input type="datetime-local" name="scheduled_pilldate4" style="width: 300px; height: 70px;">   
        <br>
        <label for="mednames">Choose medication(s)</label><br>
        <select name="mednames4[]" multiple="multiple" id="current_select">
            <option style="width: 280px; height: 10px;"></option>

                <?php

                    if($ans4) {
                        while($row=mysqli_fetch_array($ans4)) {
                            $mednames=$row["$column_name"];
                            echo"<option>$mednames<br></option>";
                        }
                    }

                ?>
        </select><br>______________________________________________________________________________</br><p>  
        
        <label for="contname"><b>Pill Container<b></label>
        <label for="contname5"><b>5</b></label><br>
        <input type="datetime-local" name="scheduled_pilldate5" style="width: 300px; height: 70px;">   
        <br>
        <label for="mednames">Choose medication(s)</label><br>
        <select name="mednames5[]" multiple="multiple" id="current_select">
            <option style="width: 280px; height: 10px;"></option>

                <?php

                    if($ans5) {
                        while($row=mysqli_fetch_array($ans5)) {
                            $mednames=$row["$column_name"];
                            echo"<option>$mednames<br></option>";
                        }
                    }

                ?>
        </select><br>______________________________________________________________________________</br><p>  
       
        <label for="contname"><b>Pill Container<b></label>
        <label for="contname6"><b>6</b></label><br>
        <input type="datetime-local" name="scheduled_pilldate6" style="width: 300px; height: 70px;">   
        <br>
        <label for="mednames">Choose medication(s)</label><br>
        <select name="mednames6[]" multiple="multiple" id="current_select">
            <option style="width: 280px; height: 10px;"></option>

                <?php

                    if($ans6) {
                        while($row=mysqli_fetch_array($ans6)) {
                            $mednames=$row["$column_name"];
                            echo"<option>$mednames<br></option>";
                        }
                    }

                ?>
        </select><br>______________________________________________________________________________</br><p>  
       
        <label for="contname"><b>Pill Container<b></label>
        <label for="contname7"><b>7</b></label><br>
        <input type="datetime-local" name="scheduled_pilldate7" style="width: 300px; height: 70px;">   
        <br>
        <label for="mednames">Choose medication(s)</label><br>
        <select name="mednames7[]" multiple="multiple" id="current_select">
            <option style="width: 280px; height: 10px;"></option>

                <?php

                    if($ans7) {
                        while($row=mysqli_fetch_array($ans7)) {
                            $mednames=$row["$column_name"];
                            echo"<option>$mednames<br></option>";
                        }
                    }

                ?>
        </select><br>______________________________________________________________________________</br><p>  
       
        <label for="contname"><b>Pill Container<b></label>
        <label for="contname8"><b>8</b></label><br>
        <input type="datetime-local" name="scheduled_pilldate8" style="width: 300px; height: 70px;">   
        <br>
        <label for="mednames">Choose medication(s)</label><br>
        <select name="mednames8[]" multiple="multiple" id="current_select">
            <option style="width: 280px; height: 10px;"></option>

                <?php

                    if($ans8) {
                        while($row=mysqli_fetch_array($ans8)) {
                            $mednames=$row["$column_name"];
                            echo"<option>$mednames<br></option>";
                        }
                    }

                ?>
        </select><br>______________________________________________________________________________</br><p>  

        <label for="contname"><b>Pill Container<b></label>
        <label for="contname9"><b>9</b></label><br>
        <input type="datetime-local" name="scheduled_pilldate9" style="width: 300px; height: 70px;">  
        <br>
        <label for="mednames">Choose medication(s)</label><br> 
        <select name="mednames9[]" multiple="multiple" id="current_select">
            <option style="width: 280px; height: 10px;"></option>

                <?php

                    if($ans9) {
                        while($row=mysqli_fetch_array($ans9)) {
                            $mednames=$row["$column_name"];
                            echo"<option>$mednames<br></option>";
                        }
                    }

                ?>
        </select><br>______________________________________________________________________________</br><p>  
        
        <label for="contname"><b>Pill Container<b></label>
        <label for="contname10"><b>10</b></label><br>
        <input type="datetime-local" name="scheduled_pilldate10" style="width: 300px; height: 70px;">   
        <br>
        <label for="mednames">Choose medication(s)</label><br>
        <select name="mednames10[]" multiple="multiple" id="current_select">
            <option style="width: 280px; height: 10px;"></option>

                <?php

                    if($ans10) {
                        while($row=mysqli_fetch_array($ans10)) {
                            $mednames=$row["$column_name"];
                            echo"<option>$mednames<br></option>";
                        }
                    }

                ?>
        </select><p>  

            <input type="Submit" name="submit">  
        </form>

  
  </section>
</body>
</html>
