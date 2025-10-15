
<?php

// Zona de conexion a la base de datos
$db = mysqli_connect('localhost', 'gino', '1234', 'mysitedb') or die('No se pudo conectar a la base de datos :c');
?>

<!--Zona de confirmacion de la conexion a la base de datos-->
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Conexión php y sql</title>
    </head>
    <body>
        <h1>Conexion establecida correctamente c:</h1>
    </body>
</html>


<?php

//Zona de desplegar la tabla

    $mostrar = mysqli_query($db, "SELECT * FROM tPrimarcas") or die("no funca la consulta");

    while ($linea = mysqli_fetch_array($mostrar)) {
        echo '<div>';
        echo '<img src="' . $linea['img'] . '" alt="' . $linea['nombre'] . '" width="100">';
        echo '<p>' . $linea['nombre'] . ' - ' . $linea['legion'] . '</p>';
        echo '<a href="detail.php?id=' . $linea['id'] . '">Ver detalle</a>';
        echo '</div><hr>';
    }

    mysqli_close($db);
?>

