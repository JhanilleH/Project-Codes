<?php 
    session_start();
    $name = ($_SESSION['username']);

    $serverName = "localhost"; 
    $userName = "USERS"; 
    $password = "engine451q"; 
    $dbName = "USERS";

    $conn = mysqli_connect($serverName, $userName, $password, $dbName);

    $query="SELECT * FROM scheduledata WHERE user='".$name."' ";
    $ans=mysqli_query($conn, $query);

    $query="Select username FROM userlogin";//search for unique username which gets the password for  the user
    $result=mysqli_query($conn, $query);


?>

<!DOCTYPE html>
<html>
<head>
    <title>Patient Schedule</title>
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/modal.css">
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
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script>
    $(document).ready(function() {
        $(".hide_material button").click(function() {
            $(this).closest('tr').hide();
            //Use Alternative
        });
    });
</script>    
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
    <table align="center" border="2px" style="width:660px; line-height:40px;">
        <tr>
            <th colspan="5"><h2>Patient Schedule</h2></th>
        </tr>
        <t>
            <th scope="col">Entries</th>
            <th scope="col"> Pill Containers</th>
            <th scope="col"> Date and Time</th>	
            <th scope="col"> Medication</th>
	        <th style="width: 25%" scope="col"> Options</th>
        </t>    
	<?php
            while($rows=mysqli_fetch_array($ans))
            {     
	?> 
	    <tr class="hide_material"><td></td>         
                <td><?php echo $rows['container']; ?></td>
                <td><?php echo $rows['scheduled_pilldate']; ?></td>
                <td><?php echo $rows['mednames']; ?></td>
		<td><button type="button" class= "btn-primary" id="btn" >Delete</a></button>
            <button class= "update-btn btn-primary" id="<?php echo $rows['scheduleID'];?>">Update</button>
        </td>         
            </tr>

        <?php
            }

        ?>
    </table>

    <!-- The Modal -->
    <div id="myModal" class="modal">
        <!-- Modal content -->
        <div class="modal-content">
        <span class="close-modal">&times;</span>
        <p>Update Record</p>
        <div >
            <label for="modal-contname"></label><br>
            <input type="datetime-local" name="scheduled_pilldate" id="modal-scheduled_pilldate" style="width: 300px; height: 70px;" >
            <br>
            <label for="mednames">Choose medication(s)</label><br>
            <select name="mednames[]" multiple="multiple" id="modal-current_select">
                <option style="width: 280px; height: 10px;"></option>
                <?php
                    $query="SELECT * FROM medication ORDER BY mednames";
                    $res=mysqli_query($conn, $query);
                    if($res) {
                        while($row=mysqli_fetch_array($res)) {
                            $mednames=$row["mednames"];
                            echo"<option>$mednames<br></option>";
                        }
                    }
                ?>
            </select>
            <input type="submit" value="Submit" id="modal-submit">
        </div>
        </div>
    </div>

    <script>
        var modal = document.getElementById("myModal");
        var recordID = "";
        var close = document.getElementsByClassName("close-modal")[0];
        close.addEventListener("click", () => {
            modal.style.display = "none";
        })
        document.querySelectorAll(".update-btn").forEach( ub => {
            ub.addEventListener("click", event => {
                modal.style.display = "block";
                recordID = event.target.id
            })
        })

        document.getElementById("modal-submit").addEventListener("click", ()=> {
            
            var dateEntered = document.getElementById("modal-scheduled_pilldate").value
            const selected = document.querySelectorAll('#modal-current_select option:checked');
            const medications = Array.from(selected).map(el => el.value);

            details = {
                scheduleID: recordID,
                scheduled_pilldate: dateEntered, //Left is databasename and right is variable storing value, left is  key=right is value
                mednames: JSON.stringify(medications),
                submit: "submit"
            }
            var formBody = [];
            for (var property in details) {
                var encodedKey = encodeURIComponent(property);
                var encodedValue = encodeURIComponent(details[property]);
                formBody.push(encodedKey + "=" + encodedValue);
            }
            formBody = formBody.join("&");

            fetch('update.php', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
                },
                body: formBody
            })
            .then(res => res.json())
            .then(reply => {
                if (reply["msg"] == "updated") {
                    window.location.replace("/schedule.php");
                }
            })

            
        })
        
    </script> 
</body>
</html>
