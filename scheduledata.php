<?php

    session_start();

    date_default_timezone_set('America/Jamaica');

    $serverName = "localhost";
    $userName = "USERS";
    $password = "engine451q";
    $dbName = "USERS";

    $conn = mysqli_connect($serverName, $userName, $password, $dbName);

    // if(isset($_POST['submit'])) {

    //     $meals = $_POST['meals1'];

    //     foreach($meals as $item)
    //     {
    //         // echo $item;
    //         $query_check = "Insert into meals_med(meals, container) values ('".$item."', '1')";
    //         $run = mysqli_query($conn,$query_check) or die(mysqli_error());
            
    //     }


    // }

    // if(isset($_POST['submit'])) {

    //     $meals = $_POST['meals2'];

    //     foreach($meals as $item)
    //     {
    //         // echo $item;
    //         $query_check = "Insert into meals_med(meals, container) values ('".$item."', '2')";
    //         $run = mysqli_query($conn,$query_check) or die(mysqli_error());
            
    //     }


    // }

    // if(isset($_POST['submit'])) {

    //     $meals = $_POST['meals3'];

    //     foreach($meals as $item)
    //     {
    //         // echo $item;
    //         $query_check = "Insert into meals_med(meals, container) values ('".$item."', '3')";
    //         $run = mysqli_query($conn,$query_check) or die(mysqli_error());
            
    //     }


    // }

    // if(isset($_POST['submit'])) {

    //     $meals = $_POST['meals4'];

    //     foreach($meals as $item)
    //     {
    //         // echo $item;
    //         $query_check = "Insert into meals_med(meals, container) values ('".$item."', '4')";
    //         $run = mysqli_query($conn,$query_check) or die(mysqli_error());
            
    //     }


    // }

    // if(isset($_POST['submit'])) {

    //     $meals = $_POST['meals5'];

    //     foreach($meals as $item)
    //     {
    //         // echo $item;
    //         $query_check = "Insert into meals_med(meals, container) values ('".$item."', '5')";
    //         $run = mysqli_query($conn,$query_check) or die(mysqli_error());
            
    //     }


    // }

    // if(isset($_POST['submit'])) {

    //     $meals = $_POST['meals6'];

    //     foreach($meals as $item)
    //     {
    //         // echo $item;
    //         $query_check = "Insert into meals_med(meals, container) values ('".$item."', '6')";
    //         $run = mysqli_query($conn,$query_check) or die(mysqli_error());
            
    //     }


    // }

    // if(isset($_POST['submit'])) {

    //     $meals = $_POST['meals7'];

    //     foreach($meals as $item)
    //     {
    //         // echo $item;
    //         $query_check = "Insert into meals_med(meals, container) values ('".$item."', '7')";
    //         $run = mysqli_query($conn,$query_check) or die(mysqli_error());
            
    //     }


    // }

    // if(isset($_POST['submit'])) {

    //     $meals = $_POST['meals8'];

    //     foreach($meals as $item)
    //     {
    //         // echo $item;
    //         $query_check = "Insert into meals_med(meals, container) values ('".$item."', '8')";
    //         $run = mysqli_query($conn,$query_check) or die(mysqli_error());
            
    //     }


    // }

    // if(isset($_POST['submit'])) {

    //     $meals = $_POST['meals9'];

    //     foreach($meals as $item)
    //     {
    //         // echo $item;
    //         $query_check = "Insert into meals_med(meals, container) values ('".$item."', '9')";
    //         $run = mysqli_query($conn,$query_check) or die(mysqli_error());
            
    //     }


    // }

    // if(isset($_POST['submit'])) {

    //     $meals = $_POST['meals10'];

    //     foreach($meals as $item)
    //     {
    //         // echo $item;
    //         $query_check = "Insert into meals_med(meals, container) values ('".$item."', '10')";
    //         $run = mysqli_query($conn,$query_check) or die(mysqli_error());
            
    //     }


    // }

    if(isset($_POST['submit'])) {

        $name = ($_SESSION['username']);
        // echo date_default_timezone_get();
        // exit();
        for ($i=1; $i<11; $i++){

            $mednames_list=join(", ",$_POST['mednames'.$i]);//turns array into a delimited list(delimiter-whatever is separting the values",")
            
            $query = "Insert into schedulehistory(container,scheduled_pilldate,mednames,entry_date,user) values (".$i.", '".$_POST['scheduled_pilldate'.$i]."', '".$mednames_list."', '".date("Y-m-d H:i:s")."', '".$name."')";//.= same as +=, appends it
            // $query = "Insert into scheduledata(container,scheduled_pilldate,mednames) values (".$i.", '".$_POST['scheduled_pilldate'.$i]."', '".$mednames_list."')";//.= same as +=, appends it
            // echo $query;
            $run = mysqli_query($conn,$query) or die(mysqli_error());
        }

        //select all from scheduledata, check if rows=0, save in variable
        //if variable is 0 then insert if not 0 update(inside)
        $query1="select * FROM scheduledata WHERE user='".$name."'";
        $ans1=mysqli_query($conn, $query1);
        $zero=0;
        if ($data=mysqli_query($conn, $query1))
            { 
                $rowcount=mysqli_num_rows($data);
            }      

        for ($j=1; $j<11; $j++){

            $mednames_list=join(", ",$_POST['mednames'.$j]);
            //$username = join(","[$name.$j]);

            if ($rowcount == $zero)
            {
                $query = "Insert into scheduledata(container,scheduled_pilldate,mednames,user) values (".$j.", '".$_POST['scheduled_pilldate'.$j]."', '".$mednames_list."', '".$name."')";//.= same as +=, appends it
                $run = mysqli_query($conn,$query) or die(mysqli_error());
            }
            else
            {
                $query = "UPDATE scheduledata SET scheduled_pilldate='".$_POST['scheduled_pilldate'.$j]."' , mednames='".$mednames_list."' , user='".$name."' WHERE container='".$j."' and user='".$name."' ";
                $run = mysqli_query($conn,$query) or die(mysqli_error());
            }

            
        }

        
        if ($run){
            
            echo "Form Submitted"; 

            header('location: /medschedule.php');  
        }
        else {
            echo "Form not submitted";
        }
    }
?>
