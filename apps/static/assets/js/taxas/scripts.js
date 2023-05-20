// Adiciona um evento de clique para todos os botões de aprovação de taxa
const approveButtons = document.getElementsByName('aprovar-taxa');
approveButtons.forEach(button => {
  button.addEventListener('click', async event => {
    event.preventDefault();
    const url = event.target.href;
    try {
      const response = await fetch(url, {
        method: 'GET'
      });
      if (response.status === 200) {
        const jsonResponse = await response.json();
        const creditosNaoAprovados = jsonResponse.taxas_nao_aprovadas;
        const creditosAprovados = jsonResponse.taxas_aprovadas;
        
        // Atualizar a tabela de taxas não aprovadas com os novos dados
        const tabelaNaoAprovadas = document.getElementById('table-taxas-nao-aprovadas');
        tabelaNaoAprovadas.innerHTML = ''; // Limpar a tabela
        
        creditosNaoAprovados.forEach(credito => {
          const row = createTableRow(credito);
          tabelaNaoAprovadas.appendChild(row);
        });
        
        // Atualizar a tabela de taxas aprovadas com os novos dados
        const tabelaAprovadas = document.getElementById('table-taxas-aprovadas');
        tabelaAprovadas.innerHTML = ''; // Limpar a tabela
        
        creditosAprovados.forEach(credito => {
          const row = createTableRow(credito);
          tabelaAprovadas.appendChild(row);
        });
      } else {
        throw new Error('Erro ao aprovar taxa');
      }
    } catch (error) {
      console.error(error);
      alert('Erro ao aprovar taxa');
    }
  });
});

// Função auxiliar para criar uma nova linha na tabela com base nos dados do crédito
function createTableRow(credito) {
  const row = document.createElement('tr');
  
  const clienteIdCell = document.createElement('td');
  clienteIdCell.textContent = credito.cliente_id;
  row.appendChild(clienteIdCell);
  
  const clienteNomeCell = document.createElement('td');
  clienteNomeCell.textContent = credito.cliente.nome;
  row.appendChild(clienteNomeCell);
  
  const dtTaxaCell = document.createElement('td');
  dtTaxaCell.textContent = credito.dt_taxa;
  row.appendChild(dtTaxaCell);
  
  const taxasCell = document.createElement('td');
  taxasCell.textContent = credito.taxas;
  row.appendChild(taxasCell);
  
  return row;
}