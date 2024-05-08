const handleClick = () => {
    const button = document.getElementById("meu_botão");
    let valor = parseInt(button.innerText);
    valor ++;
    button.innerText = valor.toString();
    console.log(button.innerText);
}