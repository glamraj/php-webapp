<h1>Hello Jawwy..</h1>
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

erroneous code example
<?php
if ($expr1) {// Noncompliant
  //...
} else if ($expr2) {
  //...
} else {
//    ...
}
function compute($a, $a, $c) { // Noncompliant
}
function compute($a, $a, $c) { // Noncompliant
}
if (is_bad_ip($requester)) {
  sleep(1);  // Noncompliant
}
?>

<h4>End of Portal</h4>
