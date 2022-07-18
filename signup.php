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
                <h2>Sign up for ADP3.0</h2>
                <form action="signup.php" method="post">

                        <?php include('errors.php'); ?>

                        <label for="name">Username</label>
                        <input type="text" name="username" placeholder="Enter Username" value="<?php echo $username; ?>" required>
                        <br>
                        <label for="email">Email</label>
                        <input type="text" name="email" placeholder="Enter Email Address" value="<?php echo $email; ?>" required>
                        <br>
                        <label for="Password">Password</label>
                        <input type="text"name="password" placeholder="Enter Password" required>
                        <br>
                        <label for="Pin">Device #</label>
                        <input type="text" name="devicenum" placeholder="Enter Device Number" value="<?php echo $devicenum; ?>" required>
                        <br>
                        <input type="Submit" name="submit"> 
                </form>                   
    </section>
</body>
</html>