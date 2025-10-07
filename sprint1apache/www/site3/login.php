<?php
  
    //Zona de declaracion de variables

    $usuario = "";
    $contrasena = "";
    $mensaje = "";

    //Zona del procesamiento del formulario

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $usuario = $_POST["usuario"];
        $contrasena = $_POST["contrasena"];

        if ($usuario == "admin" && $contrasena == "1234") {
            $mensaje = "contrasena correcta, bienvenido";
        } else {
            $mensaje = "tu NO eres el usuario, listillo";
        }
    }
?>

<!--ZOna del formulario html-->

<form method="POST" action="">
    <label for="usuario">usuario:</label>
    <input type="text" name="usuario" id="usuario" required>
    <br><br>

    <label for="contrasena">contrasena:</label>
    <input type="password" name="contrasena" id="contrasena" required>
    <br><br>

    <input type="submit" value="iniciar sesion">
</form>

<!--Zona de salida por pantalla-->

<?php
    if ($mensaje != "") {
        echo "<p><strong>$mensaje</strong></p>";
    }
?>
