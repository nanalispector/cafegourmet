// Chamar a função para obter produtos quando a página carregar
window.onload = function () {    
    getProducts();
};

function redirectToDetails(url) {
    window.location.href = url;
}
