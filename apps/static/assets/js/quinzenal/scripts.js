//*apps/static/assets/js/quinzenal/scripts.js

const tableBody = document.getElementById('table-body')
function addClickListeners() {
  window.document.querySelectorAll('#aprovar-repasse').forEach((element) => {
    element.addEventListener('click', (event) => {
      event.preventDefault()
      const xhr = new XMLHttpRequest()
      xhr.onload = function() {
        if (xhr.status === 200) {
          const response = JSON.parse(xhr.response)
          console.log(response.dados_dias);
          const newTbody = generateTbody(response.dados, response.dados_dias, response.data_inicio, response.data_fim)
          tableBody.innerHTML = newTbody
          addClickListeners()
        } else {
          console.log('ERRO NO AJAX', xhr.status, xhr.readyState);
          console.error(xhr.statusText);
        }
      }
      const url = event.target.href
      xhr.open('GET', url)
      xhr.send()
    })
  })
}

addClickListeners()

function generateTbody(dados, dados_dias, data_inicio, data_fim) {
  dados.sort((a, b) => a.id_vendedor - b.id_vendedor); // Ordena os dados pelo id_vendedor
  let tbody = ''
  dados.forEach(dado => {
    tbody += "<tr>"
    tbody += `<td><a name="aprovar-repasse" id="aprovar-repasse" class="btn btn-success btn-sm" href="/aprovar_repasse/${dado.id_vendedor}/${data_inicio}/${data_fim}/${dado.total_repasses_retidos}/${dado.total_credito}/${dado.total_taxa}/${dado.total_debito}/${dado.total_repasse}">Aprovar Repasse</a></td>`
    tbody += `<td>${dado.id_vendedor}</td>`
    tbody += `<td>${dado.vendedor}</td>`
    tbody += `<td>${dado.total_repasses_retidos}</td>`
    for (let dia in dados_dias) {
      tbody += `<td>${dado[dados_dias[dia]]}</td>`
    }
    tbody += `<td>${dado.total_credito}</td>`
    tbody += `<td>${dado.total_taxa}</td>`
    tbody += `<td>${dado.total_debito}</td>`
    tbody += `<td>${dado.total_repasse}</td>`
    tbody += "</tr>"
  })
  return tbody
}
