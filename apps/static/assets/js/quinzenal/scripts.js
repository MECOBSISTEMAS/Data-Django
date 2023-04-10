//*apps/static/assets/js/quinzenal/scripts.js

const tableBody = document.getElementById('table-body')

window.document.querySelectorAll('#aprovar-repasse').forEach((element) => {
  element.addEventListener('click', (event) => {
    event.preventDefault()
    const xhr = new XMLHttpRequest()
    xhr.onload = function() {
      if (xhr.status === 200) {
        const response = JSON.parse(xhr.response)
        const newTbody = generateTbody(response.dados)
        tableBody.innerHTML = newTbody
      } else {
        console.log('ENTREI AQUI', xhr.status, xhr.readyState);
        console.error(xhr.statusText);
      }
    }
    const url = event.target.href
    xhr.open('GET', url)
    xhr.send()
  })
})


function generateTbody(dados) {
  let tbody = ''
  dados.forEach(dado => {
    tbody += "<tr>"
    tbody += `<td><a name="aprovar-repasse" id="aprovar-repasse" class="btn btn-success btn-sm" href="/aprovar_repasse/${dado.id}/${dado.data_inicio}/${dado.data_fim}">Aprovar Repasse</a></td>`
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
