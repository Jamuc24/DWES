<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Tabla del 7</title>
</head>
<body>
    <h1 background-color="red">tabla de multiplicar del 7</h1>
    <table border="1">
        <?php
            for ($numero = 1; $numero <= 10; $numero++) {
                $resultado = 7 * $numero;
                echo "<tr><td>7 x $numero</td><td>$resultado</td></tr>";
            }
        ?>
    </table>
</body>
</html>
