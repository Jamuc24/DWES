<?php
    
    //Zona de declaracion de variables

    $cantidad = 0;
    $resultado = "";
    $conversion = "";

    //Zona "fucnional del formulario" donde se hacen las conversiones de temperatura

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $cantidad = $_POST["cantidad"];
        $conversion = $_POST["conversion"];

        if ($conversion == "celsius_fahrenheit") {
            // Celsius → Fahrenheit
            $resultado = ($cantidad * 9 / 5) + 32;
            $mensaje = "$cantidad °C = " . number_format($resultado, 2) . " °fahrenhait";
        } elseif ($conversion == "fahrenheit_celsius") {
            // Fahrenheit → Celsius
            $resultado = ($cantidad - 32) * 5 / 9;
            $mensaje = "$cantidad °F = " . number_format($resultado, 2) . " °celsius";
        }
    }
?>

<!--Zona del formulario hecho en html-->

<form method="POST" action="">
    <label for="cantidad">Cantidad:</label>
    <input type="number" step="any" name="cantidad" id="cantidad" required>
    <br><br>

    <input type="radio" name="conversion" value="celsius_fahrenheit" required> Celsius → Fahrenheit<br>
    <input type="radio" name="conversion" value="fahrenheit_celsius" required> Fahrenheit → Celsius<br><br>

    <input type="submit" value="Convertir">
</form>

<!--Zona de presentar por pantalla el resultado de la conversion-->
<?php
    if (!empty($resultado)) {
        echo "<p><strong>Resultado:</strong> $mensaje</p>";
    }
?>
