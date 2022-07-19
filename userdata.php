<?php
      $serverName = "";
      $userName = "";
      $password = "";
      $dbName = "";

      $conn = mysqli_connect($serverName, $userName, $password, $dbName);

    if(isset($_POST['submit'])) {
        if(!empty($_POST['mednames'])) {
            $mname = $_POST['mednames'];
	        
            $query = "Insert into medication(mednames) values('$mname')";

            $run = mysqli_query($conn,$query) or die(mysqli_error());

            if ($run){
                echo "Form Submitted";

                header('location: med.html');  
            }
            else {
                echo ("<script> window.alert('Form not submitted'); window.loation.href='med.html';</script>");
            }
        }    
            else {
                echo ("<script> window.alert('First field required'); window.location.href='med.html';</script>");
            }
	}
        

?>
