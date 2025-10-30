<?php

$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('No se pudo conectar');
?>
<html>
    <body>
    <?php
    // Zona para obtener los datos de los primarcas
    $primarca_id = $_POST['primarca_id'];
    $comentario = $_POST['comentario'];

    //Zona para insertar los datos
    $query = "INSERT INTO tComentarios (primarca_id, comentario, fecha) VALUES ('".$primarca_id."', '".$comentario."', NOW())";

    mysqli_query($db, $query) or die('hmmmmm algo va mal');

    // Zona para confirmar que se guardo el comentario
    echo "<p>Nuevo comentario ";
    echo mysqli_insert_id($db);
    echo " añadido</p>";

    //Zona para volver a la pagina anterior (los comentarios)
    echo "<a href='detail.php?id=".$primarca_id."'>Volver</a>";

    mysqli_close($db);
    ?>
    </body>
</html>