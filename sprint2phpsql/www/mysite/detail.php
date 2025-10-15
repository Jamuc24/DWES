<?php
// Zona de conexión a la base de datos
$db = mysqli_connect('localhost', 'gino', '1234', 'mysitedb') or die('no se pudo conectar');

// Comprobamos que se haya pasado el id del primarca
if (!isset($_GET['id'])) {
    die('no elegiste un primarca');
}

$id = $_GET['id'];

// Zona para incorporarlo directamente a la tabla de la base de datos

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $comentario = trim($_POST['comentario']);

    if (!empty($comentario)) {
        $query_insert = "INSERT INTO tComentarios (primarca_id, comentario) VALUES ($id, '$comentario')";
        mysqli_query($db, $query_insert) or die('hmmmmm algo va mal');
        header("Location: detail.php?id=$id");
        exit;
    }
}

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

if (mysqli_num_rows($result2) > 0) {
    while ($comentario = mysqli_fetch_array($result2)) {
        echo '<li>' . htmlspecialchars($comentario['comentario']) . '</li>';
    }
} else {
    echo '<li>Aun no hay comentarios? vaya...</li>';
}
echo '</ul>';

// Zona para desplegar el formulario
echo '
    <hr>
    <h3>Añadir comentario</h3>
    <form action="detail.php?id=' . $id . '" method="POST">
        <textarea name="comentario" rows="4" cols="50" placeholder="Escribe tu comentario..." required></textarea><br><br>
        <input type="submit" value="Enviar comentario">
    </form>
';

mysqli_close($db);
?>
