
<!DOCTYPE html>
<html>
<head>
    <title>Sign up to Register</title>
    <link rel="stylesheet" href="css/main.css">
</head>
<body>
<div class="toppane">
        <div class="container">
            <a class="logo" href="login.html">Automatic<span>PillDispenser</span></a>
        </div>
    </div>
    
<?php

    $serverName = "localhost";
    $userName = "USERS";
    $password = "engine451q";
    $dbName = "USERS";
  
    $conn = mysqli_connect($serverName, $userName, $password, $dbName);

    if(isset($_POST['submit'])) {
        if(!empty($_POST['SIGNusername']) && !empty($_POST['SIGNpassword'])) {

        $name = $_POST['SIGNusername'];
        $password = $_POST['SIGNpassword'];

        $query="SELECT * FROM SIGNUPDATA where SIGNusername = '$name'";

        $result=mysqli_query($conn, $query);
        
        $show_pass = mysqli_fetch_object($result);
        $pass_result = $show_pass->SIGNpassword;

        $password_get = password_verify($password,$pass_result);
        // $num = mysqli_num_rows($result);

        if(password_verify($password,$pass_result)) {
            header('location: /index.html');
        } 

        else {
         //   echo "Incorrect Username or Password";
            header('location: /login.html');
        }
    }
 }
?>
</body>
</html>
