const handleClick = () => {
    const button = document.getElementById("meu_botão");
//    const classbutton = new HTMLCollectionOf<element>();
    const valor = parseInt(button.innerText) += 1;
    button.innerText = paserString(valor);

    console.log(button.innerText)
}
