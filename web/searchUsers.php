<?php
  $servername = "mysql_db";
  $username = "testuser";
  $password = "testpassword";
  $dbname = "testdb";
  $conn = new mysqli($servername, $username, $password, $dbname);

  $id = mysqli_real_escape_string($conn, $_GET['id']);
  $data = mysqli_query($conn, "select username from users where id = $id");
  $response = mysqli_fetch_array($data);
  if(!isset($response['username'])){
    http_response_code(404);
  }
?>
