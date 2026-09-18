<?php
    // criar conexao
    include_once("_conexao.php");
    $conexao= conectaBD();

    $cod = filter_input(INPUT_GET, "var_codigo");
    $dados= "DELETE FROM vendedor WHERE codigo = {$codigo}";

    mysqli_query($conexao, $dados) or die(mysqli_error());

    echo "Excluído com Sucesso!";

    mysqli_close($conexao);
?>
