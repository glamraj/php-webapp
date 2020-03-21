<h1>Hello Good Jawwy</h1>
<h4>Attempting MySQL connection from php...</h4>
<h4>Start of Portal</h4>

<?php
$host = 'localhost';
$user = 'web1';
$pass = 'Web1l234567?-';
$conn = new mysqli($host, $user, $pass);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
    echo "Connected to MySQL successfully!";
}

?>

//erroneous code example
<?
if ($expr1) {
  //...
} else if ($expr2) {
  //...
} else {
//    ...
}
?>

<h4>End of Portal</h4>
