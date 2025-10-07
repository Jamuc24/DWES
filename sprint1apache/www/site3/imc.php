<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de IMC</title>
</head>
    <body>
    <h1>Calculadora de IMC</h1>

<?php
  
    // Zona de declaracion de variables

    $peso = 0;
    $altura = 0; 
    $pesoOriginal = 0;
    $alturaOriginal = 0;
    $imc = 0;

 
    //Zona de la funcion que va a calcular el imc
 
    function calcular_imc($pesoOriginal, $alturaOriginal){
        $imc = $pesoOriginal / ($alturaOriginal * $alturaOriginal);
        return $imc;
    }

  
    //Zona de recogida de informacion con gets

    if (isset($_GET["peso"]) && isset($_GET["altura"])) {
        $pesoOriginal = $_GET["peso"];
        $alturaOriginal = $_GET["altura"];
        
        $imc = calcular_imc($pesoOriginal, $alturaOriginal);
    }


    //Zona de presentar por pantalla

    if (isset($_GET["peso"]) && isset($_GET["altura"])) {
        echo "Tu IMC es: " . number_format($imc, 2);

        if ($imc < 18.5) {
            echo "Tienes bajo peso, ojo a los vendavales";
        } elseif ($imc >= 18.5 && $imc <= 24.9) {
            echo "Tu peso es normal, todo en orden jefe";
        } else {
            echo "Tienes sobrepeso, a ver si comes menos donetes eh";
        }
    } 
?>

</html>