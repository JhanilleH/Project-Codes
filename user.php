<?php
    $serverName = "";
    $userName = "";
    $password = "";
    $dbName = "";

    $conn = mysqli_connect($serverName, $userName, $password, $dbName);

    $query="SELECT * FROM medication";
    $result=mysqli_query($conn, $query);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Patient Medication List</title>
    <link rel="stylesheet" href="css/main.css">
    <style>
    table{
        margin:30px;
    }
    tr:hover {background-color: #ff99ff;}
    th {
        background-color: #ffccff;
        color: Black;
    }
</style>
</head>
<body>
<div class="toppane">
        <div class="container">
            <a class="logo" href="index.php">Automatic<span>PillDispenser</span></a>

            <img id="mobile-cta" class="mobile-menu" src="images/menu.svg" alt="For mobile website">

            <nav>
                <img id="mobile-exit" class="mobile-menu-exit" src="images/exit.svg" alt="Close navigation">
                <ul class="navigation1">
                    <li class="Home"><a href="index.php">Home</a></li>
                    <li><a href="user.html">Medication</a></li>
                    <li><a href="medschedule.php">Schedule</a></li>
                   
                </ul>

                <ul class="navigation2">
                    <li class="gotomedication-history"><a href="medication history.html">Medication History</a></li>
                </ul>

            </nav>

        </div>
    </div>
    <table align="center" border="2px" style="width:600px; line-height:40px;">
    <tr>
        <th colspan="4"><h2>Patient Medication List</h2></th>
    </tr>
    <t>
        <th>Medication ID</th>
        <th>Medication Purpose</th>
        
    </t>    
    <?php
        while($rows=mysqli_fetch_assoc($result))
        {
    ?>     
        <tr>
	    <td><?php echo $rows['medID']; ?></td>
        <td><?php echo $rows['mednames']; ?></td>
        </tr>
    <?php
        }

    ?>
    </table>

</body>
</html>
