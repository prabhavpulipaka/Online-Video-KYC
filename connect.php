<?php
    $FullName=$_POST['FullName'];
    $MobileNo=$_POST['MobileNo'];
    $DoB=$_POST['DoB'];
    $Gender=$_POST['Gender'];
    $Address=$_POST['Address'];

    $conn=new mysqli('localhost','root','','onlinevideokyc');
    if($conn->connect_error){
        die('connection failed:'.$conn->connect_error);
    }
    else{
        $stmt=$conn->prepare("insert into registration(FullName,MobileNo,DoB,Gender,Address) values(?,?,?,?,?)");
        $stmt->bind_param("sisss",$fullname,$mobile_no,$date_of_birth,$gender,$address);
        $stmt->execute();
        $stmt->close();
        $conn->close(); 
    }
?>