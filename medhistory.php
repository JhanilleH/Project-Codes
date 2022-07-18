<?php
    session_start();

    $serverName = "localhost";
    $userName = "USERS";
    $password = "engine451q";
    $dbName = "USERS";

    $conn = mysqli_connect($serverName, $userName, $password, $dbName);
    mysqli_select_db($conn, 'schedulehistory');

    $data="select * FROM medhistory2";
    $result=mysqli_query($conn, $data);

    

?>

<!DOCTYPE html>
<html>
<head>
    <title>Medication History</title>
    <link rel="stylesheet" href="css/main.css">
<style>
    table{
        margin:30px;
    }
    tr:hover {background-color: #ff99ff;}
    /* tr:nth-child(even) {background-color: #ffdaea;} */
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
                    <li><a href="med.html">Medication</a></li>
                    <li><a href="medschedule.php">Schedule</a></li>
                   
                </ul>

                <ul class="navigation2">
                    <li class="gotomedication-history"><a href="medication history.html">Medication History</a></li>
                </ul>

            </nav>

        </div>
    </div>

    <font size="5">
    
     
    <table align="center" border="2px" style="width:650px; line-height:40px;">
        <tr>
            <th colspan="5"><h2>Previous Patient Schedule</h2></th>
        </tr>
        <t>
            <th scope="col">Entries</th>
            <th scope="col"> Pill Containers</th>
            <th style="width: 25%" scope="col"> Date and Time</th>	
            <th scope="col"> Medication</th> 
            <th style="width: 20%" scope="col"> Date of Entry</th> 
        </t>    
        <?php
            $results_on_each = 10;
            $name = ($_SESSION['username']);
        
            $query="select * FROM schedulehistory WHERE user='".$name."' ";
            $ans=mysqli_query($conn, $query);

            $number_results = mysqli_num_rows($ans);
        
            // while ($row = mysqli_fetch_array($ans)){
            //     echo $row['scheduleid']. ' ' . $row['schedulehistory'] . '<br>';
            // }
        
            $number_of_pages = ceil($number_results/$results_on_each);
        
            if (!isset($_GET['pages'])){
                $pages = 1;
            }
            else{
                $pages = $_GET['pages'];
            }
        
            $first_page = ($pages-1)*$results_on_each;
        
            //  $starting_limit_number = ($page_number-1)*$results_on_each
            $query = "select * FROM schedulehistory WHERE user='".$name."' LIMIT " . $first_page . ',' . $results_on_each;
            $ans = mysqli_query($conn, $query);
        
            // while ($row = mysqli_fetch_array($ans)){
            //     echo $row['scheduleID'] . ' ' . $row['schedulehistory'] . '<br>';
            // }
        
            while($row=mysqli_fetch_array($ans))
                {
                    ?>    
                <tr>
                    <td><?php echo $row['scheduleID'] . ' ' . $row['schedulehistory']; ?></td>
                    <td><?php echo $row['container'] . ' ' . $row['schedulehistory']; ?></td>
                    <td><?php echo $row['scheduled_pilldate'] . ' ' . $row['schedulehistory']; ?></td>
                    <td><?php echo $row['mednames'] . ' ' . $row['schedulehistory']; ?></td>
                    <td><?php echo $row['entry_date'] . ' ' . $row['schedulehistory']; ?></td>
                </tr> 
            <?php
                }
            //Put a class for button and put comments in code
            for ($pages=1;$pages<=$number_of_pages;$pages++) {
                echo '<span> </span><button><a href="medhistory.php?pages=' . $pages . '">' . $pages . '</a></button>';
                // echo '<button class= "btn-primary"><a href=""?scheduleID=<?php echo $rows['scheduleID'];?</button>'
            }

            

        ?>
    </table>

    <table align="center" border="2px" style="width:1000px; line-height:40px;">
        <tr>
            <th colspan="4"><h2>Medication Taken on Schedule</h2></th>
        </tr>
        <t>
            <th scope="col" style="width:20%"> Scheduled Pill Date</th>
            <th scope="col" style="width:20%"> Date Pill Taken</th>
            <th scope="col" style="width:20%"> Time Passed Days:Hours:Minutes:Seconds</th>
            <th scope="col" style="width:40%"> Medication Status</th>
        </t>    
        <?php
            while($rows=mysqli_fetch_assoc($result))
            {
        ?>     
            <tr>
                <td><?php echo $rows['initialdate']; ?></td>
                <td><?php echo $rows['date']; ?></td>
                <td><?php echo $rows['datedifference']; ?></td>
                <td><?php echo $rows['medtaken']; ?></td>
            </tr>
        <?php
            }

        ?>
    </table>

    <table align="center" border="2px" style="width:1000px; line-height:40px;">
        <tr>
            <th colspan="4"><h2>Medication Not Taken on Schedule</h2></th>
        </tr>
        <t>
            <th scope="col" style="width:20%"> Scheduled Pill Date</th>
            <th scope="col" style="width:20%"> Date Pill Taken</th>
            <th scope="col" style="width:20%"> Time Passed Days:Hours:Minutes:Seconds</th>
            <th scope="col" style="width:40%"> Medication Status</th>
        </t>    
        <?php
            $results_on_page = 5;

            $history="select * FROM medhistory WHERE user='".$name."' ";
            $received=mysqli_query($conn, $info);
            $results_num = mysqli_num_rows($received);

            $page_count = ceil($results_num/$results_on_page);
        
            if (!isset($_GET['historypages'])){
                $historypages = 1;
            }
            else{
                $historypages = $_GET['historypages'];
            }
        
            $first_one = ($historypages-1)*$results_on_page;
        
            //  $starting_limit_number = ($page_number-1)*$results_on_each
            $query = "select * FROM medhistory WHERE user='".$name."' LIMIT " . $first_one . ',' . $results_on_page;
            $sec_ans = mysqli_query($conn, $query);

            while($rows=mysqli_fetch_assoc($sec_ans))
            {
        ?>     
            <tr>
                <td><?php echo $rows['initialdate']; ?></td>
                <td><?php echo $rows['date']; ?></td>
                <td><?php echo $rows['datedifference']; ?></td>
                <td><?php echo $rows['mednottaken']; ?></td>
            </tr>
        <?php
            }
            //Put a class for button and put comments in code
            for ($historypages=1;$historypages<=$page_count;$historypages++) {
                echo '<span> </span><button><a href="medhistory.php?pages=' . $pages . '">' . $pages . '</a></button>';
                // echo '<button class= "btn-primary"><a href=""?scheduleID=<?php echo $rows['scheduleID'];?</button>'
            }
        ?>
    </table>

</body>
</html>
