<?php

    $db = mysqli_connect('localhost', 'gino', '1234', 'mysitedb') or die('No se pudo conectar');

    //Zona para recoger los datos introducios por el usuario en el formulario
    $nombre = $_POST['nombre'];
    $apellidos = $_POST['apellidos'];
    $correo = $_POST['correo'];
    $nombre_usuario = $_POST['nombre_usuario'];
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];

    //Zona para validar los campos introcidos (que se rellene el formulario entero)
    if (empty($nombre) || empty($apellidos) || empty($correo) || empty($nombre_usuario) || empty($password) || empty($confirm_password)) {
    die('No llenaste todos los campos, cuenta no creada');
    }

    //Zona para controlar si las contraseñas son iguales
    if ($password !== $confirm_password) {
    die('Las constrasennas no coinciden, cuenta no creada');
    }

    //Zona para verificar si el correo ya esta registrado
    $query_check_email = "SELECT id FROM tUsuarios WHERE correo = '$correo'";
    $result_email = mysqli_query($db, $query_check_email);

    if (mysqli_num_rows($result_email) > 0) {
    die('El correo que quieres registrar ya esta registrado, cuenta no creada');
    }

    //Zona para verificar si el nombre de usuario ya esta registrado
    $query_check_user = "SELECT id FROM tUsuarios WHERE nombre_usuario = '$nombre_usuario'";
    $result_user = mysqli_query($db, $query_check_user);

    if (mysqli_num_rows($result_user) > 0) {
    die('Este nombre de usuario ya esta tomado , cuenta no creada');
    }

    //Zona para codificar la contraseña
    $password_hashed = password_hash($password, PASSWORD_DEFAULT);

    //Zona para insertar en la base de datos el usuario
    $query_insert = "INSERT INTO tUsuarios (nombre, apellidos, correo, nombre_usuario, password) 
    VALUES ('$nombre', '$apellidos', '$correo', '$nombre_usuario', '$password_hashed')";
    echo'Registro exisotoso Soldado, bienvenido al imperio';
    if (mysqli_query($db, $query_insert)) {
    
    //Zona para regresar al main.php
    header('Location: main.php');
    } else {
    die('hmmmmmmm algo anda mal' . mysqli_error($db));
    }

    mysqli_close($db);
?>