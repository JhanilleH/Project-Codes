<?php
    session_start();

    $serverName = "localhost";
    $userName = "USERS";
    $password = "engine451q";
    $dbName = "USERS";

    $conn = mysqli_connect($serverName, $userName, $password, $dbName);
    mysqli_select_db($conn, 'schedulehistory');

    

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

    button{
        background-color: #ffccff;
        color: White;
        font-size: 0.6em;
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
            $results_pages  = 10;
            $name = ($_SESSION['username']);

            $data="select * FROM medhistory2 WHERE user='".$name."'";
            $result=mysqli_query($conn, $data);

            $no_results = mysqli_num_rows($result);

            $page_no = ceil($no_results/$results_pages);

            if (!isset($_GET['pages'])){
                $pages = 1;
            }
            else{
                $pages = $_GET['pages'];
            }

            $page_one = ($pages-1)*$results_pages;

            $data = "select * FROM medhistory2 WHERE user='".$name."' LIMIT " . $page_one . ',' . $results_pages;
            $result = mysqli_query($conn, $data);

            while($rows=mysqli_fetch_assoc($result))
            {
                ?>     
            <tr>
                <td><?php echo $rows['initialdate'] . ' ' . $row['medhistory2']; ?></td>
                <td><?php echo $rows['date'] . ' ' . $row['medhistory2']; ?></td>
                <td><?php echo $rows['datedifference'] . ' ' . $row['medhistory2']; ?></td>
                <td><?php echo $rows['medtaken'] . ' ' . $row['medhistory2']; ?></td>
            </tr>
        <?php
            }

            for ($pages=1;$pages<=$page_no;$pages++) {
                echo '<span> </span><button><a href="medhistory.php?pages=' . $pages . '">' . $pages . '</a></button>';
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
            $results_on_page = 10;
            $name = ($_SESSION['username']);

            $history="select * FROM medhistory WHERE user='".$name."' ";
            $received=mysqli_query($conn, $history);

            $results_num = mysqli_num_rows($received);

            $page_count = ceil($results_num/$results_on_page);
        
            if (!isset($_GET['pages'])){
                $pages = 1;
            }
            else{
                $pages = $_GET['pages'];
            }
        
            $first_one = ($pages-1)*$results_on_page;
        
            //  $starting_limit_number = ($page_number-1)*$results_on_each
            $history = "select * FROM medhistory WHERE user='".$name."' LIMIT " . $first_one . ',' . $results_on_page;
            $received = mysqli_query($conn, $history);

            while($rows=mysqli_fetch_assoc($received))
            {
                ?>     
            <tr>
                <td><?php echo $rows['initialdate'] . ' ' . $row['medhistory']; ?></td>
                <td><?php echo $rows['date'] . ' ' . $row['medhistory']; ?></td>
                <td><?php echo $rows['datedifference'] . ' ' . $row['medhistory']; ?></td>
                <td><?php echo $rows['mednottaken'] . ' ' . $row['medhistory']; ?></td>
            </tr>
        <?php
            }
            //Put a class for button and put comments in code
            for ($pages=1;$pages<=$page_count;$pages++) {
                echo '<span> </span><button><a href="medhistory.php?pages=' . $pages . '">' . $pages . '</a></button>';
                // echo '<button class= "btn-primary"><a href=""?scheduleID=<?php echo $rows['scheduleID'];?</button>'
            }
        ?>
    </table>

</body>
</html>
