function comprar(nomeProduto, preco, imagem){
    document.getElementById('modalProdutoNome').textContent = nomeProduto;
    document.getElementById('modalProdutoPreco').textContent = preco;
    document.getElementById('modalProdutoImagem').src = imagem;

    const modal = bootstrap.Modal.getOrCreateInstance(document.getElementById('modalProduto'));
    modal.show();
}
function cadastrar(){
    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
    let telefone = document.getElementById("telefone").value;
    let idade = document.getElementById("idade").value;
    let numeracao = document.getElementById("numeracao").value;
    let cor = document.getElementById("cor").value;

    let mensagem = document.getElementById("mensagem").value;

    let estilo = document.querySelector('input[name="estilo"]:checked').value;

    let tipo = [] 
     document.querySelectorAll('input[name="tipo"]:checked').
     forEach(function (item) {
        tipo.push(item.value)
     });;

     console.log(tipo)

    let cliente ={
        nome: nome,
        email: email,
        telefone: telefone,
        idade: idade,
        numeracao: numeracao,
        cor: cor,
        mensagem: mensagem,
        estilo: estilo,

    }

    console.log(nome)
    console.log(email)
    console.log(telefone)
    console.log(cliente)



}

function calcularFrete(){

    let valor = document.getElementById("valorCompra").value;
    let regiao = document.getElementById("regiao").value;

    valor = parseFloat(valor);
    let frete;
    if(regiao =="sudeste"){
        frete = 19.90;
    }else if(regiao == "sul"){
        frete = 24.90;

    }
    else{
        frete = 29.90;
    }

    document.getElementById("resultadoFrete").textContent = "Frete: R$" + frete.toFixed(2);
    

}