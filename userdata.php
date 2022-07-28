<?php
    session_start();    

    $serverName = "localhost";
    $userName = "USERS";
    $password = "engine451q";
    $dbName = "USERS";

    $conn = mysqli_connect($serverName, $userName, $password, $dbName);

    if(isset($_POST['submit'])) {
        $name = ($_SESSION['username']);

        $mname = $_POST['mednames'];
        
        $query = "Insert into medication(mednames, user) values('".$mname."', '".$name."')";
        $run = mysqli_query($conn,$query) ;

        if ($run){
            echo "Form Submitted";

            header('location: /med.html');  
        }
        else{
            echo "Form Not Submitted";
        }

            // else {
            //     echo ("<script> window.alert('Form not submitted'); window.loation.href='med.html';</script>");
            // }
            
	}
        

?>
