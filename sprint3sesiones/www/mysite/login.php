
<?php
    session_start();
    $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('No se pudo conectar');

    // Zona para obtener los datos del formulario de login.html
    $correo = $_POST['correo'];
    $password = $_POST['password'];

    // Zona para comprobar si los datos pasados no estan vacios
    if (empty($correo) || empty($password)) {
        die('Completa todos los datos del formulario');
    }

    // Zona para comprobar si el usuario se encuentra entre los correos que ya estan registrados
    $query = "SELECT id, password, nombre FROM tUsuarios WHERE correo = ?";
    $stmt = $db->prepare($query);
    $stmt->bind_param("s", $correo);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows == 0) {
        die('No hay un usuario con ese mail');
    }

    // Zona para obtener el usuario
    $usuario = $result->fetch_assoc();

    // Verificar la contraseña con password_verify
    if (password_verify($password, $usuario['password'])) {
        // Contraseña correcta - iniciar sesión
        $_SESSION['user_id'] = $usuario['id'];
        $_SESSION['user_name'] = $usuario['nombre'];
        $_SESSION['user_email'] = $correo; // ← AÑADIDO: guardar email también
        

        header("Refresh: 2; URL=main.php");
    } else {
        // Contraseña incorrecta
        die('error en la contrasenna');
    }

    $stmt->close();
    $db->close();
?>