 <?php
    $serverName = "localhost"; $userName = "USERS"; $password = 
    "engine451q"; $dbName = "USERS";

    $conn = mysqli_connect($serverName, $userName, $password, $dbName);
    
    $query="DELETE FROM scheduledata WHERE scheduleID='$_GET[scheduleID]'";
    $ans=mysqli_query($conn,$query);

    if($ans)
    {    
	   echo "Deleted";
	   header("location:schedule.php");
    }
    else 
    {
           echo "Not deleted";
    }
   
   
?>
