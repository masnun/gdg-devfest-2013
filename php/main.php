<?php

$path = $_SERVER['REQUEST_URI'];

switch($path) {
    case '/phpinfo': phpinfo(); break;
    case '/dump/server': var_dump($_SERVER); break;

}