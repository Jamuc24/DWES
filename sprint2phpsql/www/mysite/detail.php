
<?php

// Zona de conexion a la base de datos
$db = mysqli_connect('localhost', 'gino', '1234', 'mysitedb') or die('no se pudo conectar');

// Zona de comprobar que se pasa el parámetro id
if (!isset($_GET['id'])) {
    die('no elegiste un primarca');
}

$id = $_GET['id'];

// Zona donde se gestionan los datos de la consulta
$query = "SELECT * FROM tPrimarcas WHERE id = $id";
$result = mysqli_query($db, $query) or die('hmmmmmm algo no va bien');
$primarca = mysqli_fetch_array($result);

// Zona de salida por pantalla, primero los datos del primarca y deapues los comentarios asociados
echo '<h1>' . $primarca['nombre'] . '</h1>';
echo '<h2>Legión: ' . $primarca['legion'] . '</h2>';
echo '<img src="' . $primarca['img'] . '" alt="' . $primarca['nombre'] . '" width="200"><br><br>';

echo '<h3>Comentarios imperiales:</h3>';
echo '<ul>';

$query2 = "SELECT * FROM tComentarios WHERE primarca_id = $id";
$result2 = mysqli_query($db, $query2) or die('hmmmmmm algo no va bien');

while ($comentario = mysqli_fetch_array($result2)) {
    echo '<li>' . $comentario['comentario'] . '</li>';
}

echo '</ul>';

mysqli_close($db);
?>
