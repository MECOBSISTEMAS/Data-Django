/* const ctx = window.document.querySelector('#firstChart').getContext('2d'); */

/* const firstChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto','Setembro',  'Outubro', 'Novembro', 'Dezembro'],
    datasets: [{
    label: 'Vendas',
    data: [12, 19, 3, 5, 2, 7, 8, 9, 10, 11, 12, 13],
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
}); */

const repasses_aprovados_chart = window.document.querySelector("#repasses_aprovados_chart").getContext("2d");

/* new Chart(repasses_aprovados_chart, {
  type: "bar",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "Numero de vendas",
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
          "rgba(255, 0, 0, 0.7)", // vermelho com 50% de transparência
          "rgba(0, 0, 255, 0.7)", // azul com 50% de transparência
          "rgba(255, 255, 0, 0.7)", // amarelo com 50% de transparência
          "rgba(0, 128, 0, 0.7)", // verde com 50% de transparência
          "rgba(128, 0, 128, 0.7)", // roxo com 50% de transparência
          "rgba(255, 165, 0, 0.7)", // laranja com 50% de transparência
        ],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
}); */

const ctx3 = window.document.querySelector("#thirdChart").getContext("2d");

new Chart(ctx3, {
  type: "doughnut",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "Numero de vendas",
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

const ctx4 = window.document.querySelector("#fourthChart").getContext("2d");

new Chart(ctx4, {
  type: "pie",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "Numero de vendas",
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

const ctx5 = window.document.querySelector("#fifthChart").getContext("2d");

new Chart(ctx5, {
  type: "polarArea",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "Numero de vendas",
        data: [12, 10, 3, 5, 2, 3],
        borderWidth: 2,
      },
    ],
  },
  options: {
    responsive: false, // Desativa a responsividade para diminuir o tamanho do gráfico
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

const tabelas_valores = window.document.querySelector("#tabelas-valores");

function listnerFilterTables() {
  const tabel = window.document.querySelector("#tabelas-valores");
}

async function getTableValues() {
  const currentURL = new URL(window.location.href);
  currentURL.searchParams.set("construir-dashs-ajax", "");

  try {
    const response = await fetch(currentURL.href, {
      method: "GET",
      headers: {
        "X-CSRFTOKEN": getCookie("csrftoken"),
        "Content-Type": "application/json",
      },
    });

    const data = response.json();
    if (response.ok) {
      return data;
    }
  } catch (error) {
    throw new Error(error);
  }
}

function getCookie(cookieName) {
  const cookieValue = window.document.cookie
    .split(";")
    .map((cookie) => cookie.trim())
    .find((cookie) => cookie.startsWith(cookieName + "="));

  if (cookieValue) {
    return cookieValue.split("=")[1];
  }
  return "NOT_FOUND";
}

function buildDashe(element, label, labels, data, responsive = true) {
  return new Chart(element, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: label,
          data: data,
          backgroundColor: [
            "rgba(255, 0, 0, 0.7)", // vermelho com 50% de transparência
            "rgba(0, 0, 255, 0.7)", // azul com 50% de transparência
            "rgba(255, 255, 0, 0.7)", // amarelo com 50% de transparência
            "rgba(0, 128, 0, 0.7)", // verde com 50% de transparência
            "rgba(128, 0, 128, 0.7)", // roxo com 50% de transparência
            "rgba(255, 165, 0, 0.7)", // laranja com 50% de transparência
          ],
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: responsive, // Desativa a responsividade para diminuir o tamanho do gráfico
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}
  


//quando a pagina estiver devidamente carregada, chame o getTableValues
window.addEventListener("DOMContentLoaded", async () => {
  const data = await getTableValues();
  const mesesDoAno = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto','Setembro',  'Outubro', 'Novembro', 'Dezembro']
  const creditos_chart = window.document.querySelector("#creditos_chart").getContext("2d");
  const debitos_chart = window.document.querySelector("#debitos_chart").getContext("2d");
  const repasses_retidos_chart = window.document.querySelector("#repasses_retidos_chart").getContext("2d");
  const taxas_totais_chart = window.document.querySelector("#taxas_totais_chart").getContext("2d");
  const taxas_tbb_chart = window.document.querySelector("#taxas_tbb_chart").getContext("2d");
  const taxas_tec_chart = window.document.querySelector("#taxas_tec_chart").getContext("2d");
  const taxas_tac_chart = window.document.querySelector("#taxas_tac_chart").getContext("2d");
  const taxas_tcc_chart = window.document.querySelector("#taxas_tcc_chart").getContext("2d");
  const taxas_spc_chart = window.document.querySelector("#taxas_spc_chart").getContext("2d");
  const taxas_confeccao_judicial_chart = window.document.querySelector("#taxas_confeccao_judicial_chart").getContext("2d");
  const taxas_honorarios_direto_chart = window.document.querySelector("#taxas_honorarios_direto_chart").getContext("2d");
  const taxas_honorarios_judiciais_chart = window.document.querySelector("#taxas_honorarios_judiciais_chart").getContext("2d");
  
  buildDashe(
    repasses_aprovados_chart, 
    'Repasses Aprovados', 
    mesesDoAno, 
    Object.values(JSON.parse(data.table_values)['Repasses Aprovados']),
  )

  buildDashe(
  creditos_chart,
  'Créditos',
  mesesDoAno,
  Object.values(JSON.parse(data.table_values)['Creditos']),
  )

  buildDashe(
    debitos_chart,
    'Débitos',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Debitos']),
  )

  buildDashe(
    repasses_retidos_chart,
    'Repasses Retidos',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Repasse Retido']),
  )

  buildDashe(
    taxas_totais_chart,
    'Taxas Totais',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Taxas Totais']),
  )

  buildDashe(
    taxas_tbb_chart,
    'Taxas TBB',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Taxas TBB']),
  )

  buildDashe(
    taxas_tec_chart,
    'Taxas TEC',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Taxas TEC']),
  )

  buildDashe(
    taxas_tac_chart,
    'Taxas TAC',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Taxas TAC']),
  )

  buildDashe(
    taxas_tcc_chart,
    'Taxas TCC',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Taxas TCC']),
  )
  
  buildDashe(
    taxas_spc_chart,
    'Taxas SPC',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Taxas SPC']),
  )
  
  buildDashe(
    taxas_confeccao_judicial_chart,
    'Taxas Confeccao Judicial',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Taxas Confeccao Judicial']),
  )

  buildDashe(
    taxas_honorarios_direto_chart,
    'Taxas Honorarios Direto',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Taxas Honorarios Direto']),
  )

  buildDashe(
    taxas_honorarios_judiciais_chart,
    'Taxas Honorarios Judiciais',
    mesesDoAno,
    Object.values(JSON.parse(data.table_values)['Taxas Honorarios Judiciais']),
  )


});
