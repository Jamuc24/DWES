<?php
// Zona de conexión a la base de datos
$db = mysqli_connect('localhost', 'gino', '1234', 'mysitedb') or die('no se pudo conectar');

// Comprobamos que se haya pasado el id del primarca
if (!isset($_GET['id'])) {
    die('no elegiste un primarca');
}

$id = $_GET['id'];

//Anteriormente aqui se encontraba una seccion de codigo que cumplia la funcion de comment.php, pero se removio por escabilidad

// Zona de obtencion de los datos de los primarcas
$query = "SELECT * FROM tPrimarcas WHERE id = $id";
$result = mysqli_query($db, $query) or die('hmmmmm algo va mal');
$primarca = mysqli_fetch_array($result);

// Zona de para desplegar los primarcas
echo '<h1>' . $primarca['nombre'] . '</h1>';
echo '<h2>Legión: ' . $primarca['legion'] . '</h2>';
echo '<img src="' . $primarca['img'] . '" alt="' . $primarca['nombre'] . '" width="200"><br><br>';

// Zona para desplegar los comentarios que ya hay
echo '<h3>Comentarios imperiales:</h3>';
echo '<ul>';

$query2 = "SELECT * FROM tComentarios WHERE primarca_id = $id";
$result2 = mysqli_query($db, $query2) or die('hmmmmm algo va mal');

//Zona con cambios para integrar el control de la fecha
if (mysqli_num_rows($result2) > 0) {
    while ($comentario = mysqli_fetch_array($result2)) {
        echo '<li>';
        echo htmlspecialchars($comentario['comentario']);
        if (!empty($comentario['fecha'])) {
            echo ' <small style="color:#666;">(' . $comentario['fecha'] . ')</small>';
        }
        echo '</li>';
    }
} else {
    echo '<li>Aun no hay comentarios? vaya...</li>';
}

// Zona para desplegar el formulario (Ahora incorpora el comment.php)
echo '
    <hr>
    <h3>Añadir comentario</h3>
    <form action="comment.php" method="POST">
        <textarea name="comentario" rows="4" cols="50" placeholder="Escribe tu comentario..." required></textarea><br><br>
        <input type="hidden" name="primarca_id" value="' . $id . '">
        <input type="submit" value="Enviar comentario">
    </form>
';

mysqli_close($db);
?>
