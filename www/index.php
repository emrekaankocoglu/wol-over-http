<!DOCTYPE html>
<html>
<body>

<h1>WOL over HTTP</h1>



<form action="" method="post">
  <select name="select1">
  </select>
  <label for="key">Key:</label><br>
  <input type="text" id="key" name="key"><br>
  <br><br>
  <input type="submit" name="submit" value="Submit">
</form>

<?php
    if(isset($_POST['submit'])){
    if(!empty($_POST['select1'])) {
        $selected = $_POST['select1'];
        $keyauth = $_POST['key'];
        passthru("python3 send.py $selected $keyauth");
    } else {
        echo 'Please select the value.';
    }
    }
?>


</body>
</html>
