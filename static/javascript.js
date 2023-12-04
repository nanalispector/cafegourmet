// Chamar a função para obter produtos quando a página carregar
window.onload = function () {    
    getProducts();
};

function redirectToDetails(url) {
    window.location.href = url;
}

// Função para limpar a pesquisa
function clearSearch() {
    var input = document.getElementById('searchInput');
    input.value = '';

    // Redireciona para a rota principal para exibir todos os produtos
    window.location.href = '/';
}