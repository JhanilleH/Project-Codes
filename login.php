<?php include('register.php') ?>

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
            <a class="logo" href="login.php">Automatic<span>PillDispenser</span></a>
        </div>
    </div>
    <section class="login-section">
        <div class="frontpage">  
                <h2>Login to patient account</h2>
                <form action="login.php" method="post">
                    
                    <?php include('errors.php'); ?>

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
                    </div>    

                    <div class="login-left"></dev>
                        <label for="name"><b>Username</b></label>
                        <input type="text" name="username" placeholder="Enter Username"  autocomplete="off" required>
                        <br>
                        <label for="Password"><b>Password</b></label> 
                        <br>
                        <input type="password" name="password" placeholder="Enter Password"  autocomplete="off" required>
                        <br>
                        <input type="Submit" name="log_submit"> 
                    </div>
            
                    <style> p{font-size: 30px;}</style>
                    <p> Not a member?
                        <a class="sign" href="signup.php">Sign up</a>
                </p>
                </form>
        </div>
    </section>
   
</body>
</html>