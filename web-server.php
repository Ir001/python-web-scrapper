<?php
if($_SERVER['REQUEST_METHOD'] == 'POST'){
    print_r($_POST);
    
    // $fp = fopen('results.json', 'w');
    // fwrite($fp, json_encode($_POST));
    // fclose($fp);
}
