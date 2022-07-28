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
    <section class="signup-section"> 
                <h2>Sign up for APD3.0</h2>
                <form action="signup.php" method="post">

                        <?php include('errors.php'); ?>

                        <label for="name"><b>Username</b></label>
                        <input type="text" name="username" placeholder="Enter Username" value="<?php echo $username; ?>" autocomplete="off" required>
                        <br>
                        <label for="email"><b>Email</b></label>
                        <input type="text" name="email" placeholder="Enter Email Address" value="<?php echo $email; ?>" autocomplete="off" required>
                        <br>
                        <label for="Password"><b>Password</b></label>
                        <input type="password"name="password" placeholder="Enter Password" autocomplete="off" required>
                        <br>
                        <label for="Pin"><b>Device #<b></label>
                        <input type="text" name="devicenum" placeholder="Enter Device Number" value="<?php echo $devicenum; ?>" autocomplete="off" required>
                        <br>
                        <input type="Submit" name="submit"> <button class="backBtn"><a class="back" href="login.php">Go Back</button>
                </form>                   
    </section>
</body>
</html>