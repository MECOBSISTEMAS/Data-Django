const ctx = window.document.querySelector('#firstChart').getContext('2d');

const firstChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio'],
    datasets: [{
    label: 'Vendas',
    data: [12, 19, 3, 5, 2],
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderColor: 'rgba(255, 99, 132, 1)',
    borderWidth: 1
  }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

const ctx2 = window.document.querySelector('#secondChart').getContext('2d');

new Chart(ctx2, {
  type: 'bar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: 'Numero de vendas',
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: [
        'rgba(255, 0, 0, 0.7)',       // vermelho com 50% de transparência
        'rgba(0, 0, 255, 0.7)',       // azul com 50% de transparência
        'rgba(255, 255, 0, 0.7)',     // amarelo com 50% de transparência
        'rgba(0, 128, 0, 0.7)',       // verde com 50% de transparência
        'rgba(128, 0, 128, 0.7)',     // roxo com 50% de transparência
        'rgba(255, 165, 0, 0.7)'      // laranja com 50% de transparência
      ],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

const ctx3 = window.document.querySelector('#thirdChart').getContext('2d');

new Chart(ctx3, {
  type: 'doughnut',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: 'Numero de vendas',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

const ctx4 = window.document.querySelector('#fourthChart').getContext('2d');

new Chart(ctx4, {
  type: 'pie',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: 'Numero de vendas',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

const ctx5 = window.document.querySelector('#fifthChart').getContext('2d');

new Chart(ctx5, {
  type: 'polarArea',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: 'Numero de vendas',
      data: [12, 10, 3, 5, 2, 3],
      borderWidth: 2
    }]
  },
  options: {
    responsive: false, // Desativa a responsividade para diminuir o tamanho do gráfico
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

const tabelas_valores = window.document.querySelector('#tabelas-valores');

function listnerFilterTables() {
  const tabel = window.document.querySelector('#tabelas-valores');
}