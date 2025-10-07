<?php
 
    //Zona de declaracion de variables

    $num1 = 0;
    $num2 = 0;
    $operacion = "";
    $resultado = "";

    //Zona del formulario de php, OJO, no es el de html :p y hecho con post

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $num1 = $_POST["num1"];
        $num2 = $_POST["num2"];
        $operacion = $_POST["operacion"];

    //Zona del switch del formulario, lo que lo hace funcionar

        switch ($operacion) {
            case "sumar":
                $resultado = $num1 + $num2;
                break;

            case "restar":
                $resultado = $num1 - $num2;
                break;

            case "multiplicar":
                $resultado = $num1 * $num2;
                break;

            case "dividir":
                $resultado = $num1 / $num2;
                break;
        }
    }
?>

<!--Zona del formulario de HMTL, incorpora el post pero NO es php-->

<form method="POST" action="">
    <label for="num1">primer numero:</label>
    <input type="number" step="any" name="num1" id="num1" required>
    <br><br>

    <label for="num2">segundo numero:</label>
    <input type="number" step="any" name="num2" id="num2" required>
    <br><br>

    <label for="operacion">operacion a hacer:</label>
    <select name="operacion" id="operacion" required>
        <option value="sumar">sumar</option>
        <option value="restar">restar</option>
        <option value="multiplicar">multiplicar</option>
        <option value="dividir">dividir</option>
    </select>
    <br><br>

    <input type="submit" value="calcular">
</form>

<!--Zona de presentar por pantalla-->

<?php
    if ($resultado !== "") {
        echo "<p><strong>Resultado:</strong> $num1 ";

        switch ($operacion) {
            case "sumar": echo "+ $num2 = $resultado"; break;
            case "restar": echo "- $num2 = $resultado"; break;
            case "multiplicar": echo "* $num2 = $resultado"; break;
            case "dividir": echo "/ $num2 = $resultado"; break;
        }

        echo "</p>";
    }
?>
