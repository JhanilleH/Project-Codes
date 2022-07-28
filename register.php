<?php
    session_start();//Allows for the use of session variables
    // include '/home/pi/Downloads/PHPMailer-master/src/phpmail.php'; 

    $serverName = "localhost"; //Connects file to the mysql database 
    $userName = "USERS";
    $password = "engine451q";
    $dbName = "USERS";
  
    $conn = mysqli_connect($serverName, $userName, $password, $dbName);
    
    $username_login = "";
    $email_login = "";
    $device = "";
    $errors = array();
    $_SESSION['success'] = "";
    
    // Users resgistration
    if(isset($_POST['submit'])) {
        // echo 'what';
     
        // if(!empty($_POST['SIGNusername']) && !empty($_POST['email']) && !empty($_POST['SIGNpassword']) && !empty($_POST['devicenum'])) {

        // Storing the inputted values in values. Also, Data sanitization is done to prevent SQL injections
        $username_login = mysqli_real_escape_string($conn, $_POST['username']);
        $email_login = mysqli_real_escape_string($conn, $_POST['email']);
        $passwords = mysqli_real_escape_string($conn, $_POST['password']);
        $device = mysqli_real_escape_string($conn, $_POST['devicenum']);

        // Check for empty input fields, if found, error messgaes will be shown
        if (empty($username_login)) { array_push($errors, "Username is required"); }
        if (empty($email_login)) { array_push($errors, "Email is required"); }
        if (empty($passwords)) { array_push($errors, "Password is required"); }
        if (empty($device)) { array_push($errors, "Device number is required"); }

        // echo $username_login;
        // echo $email_login;
        // echo $device;
        // echo $passwords;
        // If no errors are detected, user will be registered
        if (count($errors) == 0) {

            // Encrypts all password in database table
            $password_insert = password_hash($passwords, PASSWORD_DEFAULT);

            // // Select username from table
            // $query="SELECT * FROM userlogin where username = '$username_login'";
            // $result=mysqli_query($conn, $query);

            // $num = mysqli_num_rows($result);

            // if($num > 0) {
            //     { array_push($errors, "Username is already taken"); }
            // } 
            // else {
            //     // Insert user data into table
            //     $reg = "INSERT into userlogin (username, email, 'password', devicenum) values('$username_login','$email_login','$password_insert','$device')";
            //     mysqli_query($conn, $reg);
            // }
            $reg = "Insert into userlogin(username, email, password, devicenum) values('$username_login','$email_login','$password_insert','$device')";
            mysqli_query($conn, $reg);

            // // Logged in username stored in the session variable
            // $_SESSION['username'] = $username_login;

            // Display welcome message
            $_SESSION['success'] = "Signup successful";

            header('location: login.php');

        }
    }
    // Users Login 
    if (isset($_POST['log_submit'])) {
        $username_login = mysqli_real_escape_string($conn, $_POST['username']);
        $passwords = mysqli_real_escape_string($conn, $_POST['password']);
    
    // Error messages are sent if  input field is blank
    if (empty($username_login)){
        array_push($errors, "Username is required");
    }

    if (empty($passwords)) {
        array_push($errors, "Password is required");
    }

    if (count($errors) == 0) {

        //$password_insert = password_hash($passwords, PASSWORD_DEFAULT);
        
        $query="Select * FROM userlogin where username = '$username_login'";//search for unique username which gets the password for  the user
        $result=mysqli_query($conn, $query);

        $show_pass = mysqli_fetch_object($result);//this gets the password in the record
        $pass_result = $show_pass->password;
        //echo $password_insert;
        // echo $show_pass;
        // echo $pass_result;

        // $password_get = password_verify($passwords,$pass_result);

        if(password_verify($passwords,$pass_result)) {//this verifies the password being inputted
            // echo 'yes';

                // Username stored in session variable
            $_SESSION['username'] = $username_login;
            
            // Welcome message
            $_SESSION['success'] = "You have logged in!";

            header('location: index.php');
            
            $userquery="DELETE FROM currentuser";
            $output=mysqli_query($conn, $userquery);

            $userin = "Insert into currentuser(username) values ('".$username_login."')";//.= same as +=, appends it
            $run = mysqli_query($conn,$userin) or die(mysqli_error());

        } 
        else {
            
            // If the username and password doesn't match
            array_push($errors, "Username or password incorrect");
        }


    }

    }    
?>
</body>
</html>
