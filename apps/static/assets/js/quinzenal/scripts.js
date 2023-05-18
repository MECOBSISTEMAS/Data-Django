// Adiciona um evento de clique para todos os botões de aprovação de repasse
const buttons = document.getElementsByName('aprovar-repasse');
buttons.forEach(button => {
  button.addEventListener('click', async event => {
    event.preventDefault();
    const url = event.target.href;
    const csrftoken = getCookie('csrftoken'); // obtém o valor do token CSRF do cookie
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrftoken // inclui o token CSRF no cabeçalho da requisição
        }
      });
      if (response.status === 200) {
        const row = event.target.closest('tr');
        row.remove();
      } else {
        throw new Error('Erro ao aprovar repasse');
      }
    } catch (error) {
      console.error(error);
      alert('Erro ao aprovar repasse');
    }
  });
});

// Função para obter um cookie pelo nome
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
