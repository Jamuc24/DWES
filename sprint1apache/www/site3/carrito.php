<?php
  
    // Zona de declaracion del array

    $carrito = array(
        "Monster Mango" => 3.50,
        "Bocata de chorizo" => 1.20,
        "Danoninos pack de 4" => 1.10,
        "Donetes de fresa" => 2.30
    );

   
    //Zona de hacer el calculo del total del carrito
 
    $compratotal = 0;
    foreach($carrito as $precio){
        $compratotal += $precio;
    }

    //Zona de presentar por pantalla la tabla 

    echo "<table border='1' cellspacing='0' cellpadding='5'>";
    echo "<tr><th>articulo</th><th>precio (€)</th></tr>";

    foreach($carrito as $articulo => $precio){
        echo "<tr>";
        echo "<td>$articulo</td>";
        echo "<td>" . number_format($precio, 2) . "€</td>";
        echo "</tr>";
    }

    echo "<tr><td><strong>TOTAL:</strong></td><td><strong>" . number_format($compratotal, 2) . "€</strong></td></tr>";
    echo "</table>";
?>
