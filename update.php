<?php
    // session_start();

    $serverName = "localhost"; $userName = "USERS"; $password = 
    "engine451q"; $dbName = "USERS";


    $conn = mysqli_connect($serverName, $userName, $password, $dbName);

    // $name = ($_SESSION['username']);

    if(isset($_POST['submit'])){
        $mednames_arr = json_decode($_POST['mednames']);
        $mednames_list=join(", ",$mednames_arr);
        

        $query= "UPDATE scheduledata SET scheduled_pilldate='".$_POST['scheduled_pilldate']."', mednames='".$mednames_list."'  WHERE scheduleID='".$_POST["scheduleID"]."'";
        $run = mysqli_query($conn,$query) or die(mysqli_error());
    }

    header("Content-Type: application/json; charset=UTF-8");
    if($run)
    {    
        $response["msg"] = "updated";
        $reply = json_encode($response);
        echo $reply;
    }
    else 
    {
        $response["msg"] = "not updated";
        $reply = json_encode($response);
        echo $reply;
    }

   
?>
