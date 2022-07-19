<?php
      $serverName = "";
    $userName = "";
    $password = "";
    $dbName = "";

      $conn = mysqli_connect($serverName, $userName, $password, $dbName);

      $em = $_POST['email'];
      $dev = $_POST['dev_num'];
      $user = $_POST['username'];
      $pass = $_POST['password'];

      $query = "Insert into AppSignup(email,dev_num,username,password) values('$em', '$dev', '$user', '$pass')";

      $run = mysqli_query($conn,$query) or die(mysqli_error());


?>   
