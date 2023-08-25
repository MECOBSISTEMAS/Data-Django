function getCookie(cookieName="") {
  const cookie = window.document.cookie
  .split(';')
  .map(cookie => cookie.trim())
  .find(cookie => cookie.startsWith(cookieName + '='))

  if (cookie) {
    //! retornar o valor do cookie sem o nome do cookie
    return cookie.split('=')[1]
  }
  return ""
}

async function verifyContract() {
  const contractId = window.document.querySelector("input#contrato_id").value
  try{
    const response = await fetch('http://82.208.22.228:8000/execute_query_sql_class/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({
        "sql": `SELECT * FROM contratos where contratos.id = ${contractId};`
      })
    })
    
    if (response.ok) {
      const data = await response.json()
      console.log(`REQUISIÇÃO FEITA COM SUCESSO, \n DADOS: ${Object.entries(data)}`);

    } else {
      throw new Error(`Erro ao fazer a requisição, \n STATUS: ${response.status}`);
    }
  } catch(error) {
    throw new Error(`ERRO NA SOLICITAÇÃO \n ${error}`)
  }
}

function listnerButtonContractCheck() {
  const buttonCheck = window.document.querySelector("button#checar_contrato_id");
  buttonCheck.addEventListener('click', (event) => {
    event.preventDefault();
    /* enquanto a requsição estiver em andamento desabilitar o botão de checar */
    buttonCheck.disabled = true;
    verifyContract()
    .then(() => {
      buttonCheck.disabled = false;
    });
  });
}

function addPersonToList(pessoa) {
  const listaVendedores = window.document.querySelector("div#lista-vendedores");  
  listaVendedores.innerHTML += `<li class="list-group-item">${pessoa.fields.nome} <input type="number" name="peso" id="peso" placeholder="peso"> <input type="hidden" name="pessoa_id" value="${pessoa.fields.id}"> <button type="button" class="btn btn-danger btn-sm" id="del-vendedor">DEL</button> </li>`;
}

function removePersonAtList() {
  return "";
}

async function verifyPerson() {
  const personId = window.document.querySelector("input#pessoa_id").value
  const currentURL = new URL(window.location.href)
  const title = window.document.querySelector("h4#adicionar-vendedor-titulo");
  const buttonAddSeller =  window.document.querySelector("button#adicionar-vendedor");
  try {
    const response = await fetch(currentURL.href, {
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      method: 'POST',
      body: JSON.stringify({
        "pessoa_id": personId,
        "buscar-vendedor": true,
      })
    })
    
    const data = await response.json();
    if (response.ok) {
      const pessoa = JSON.parse(data.pessoa)[0];
      //addPersonToList(pessoa);
      //caso a pessoa exista, coloque esse titulo html em verde: <h4 id="adicionar-vendedor-titulo">Adicionar Vendedor</h4>
      //e habilite  o botão de adicionar vendedor
      title.style.color = "green";
      buttonAddSeller.disabled = false;

      console.log(`REQUISIÇÃO FEITA COM SUCESSO, \n DADOS: ${Object.entries(data)}`);
      return data;
    } else {
      title.style.color = "red";
      buttonAddSeller.disabled = true;
      throw new Error(`Erro ao fazer a requisição, \n STATUS: ${response.status}`);
    }
  } catch(error) {
    throw new Error(`ERRO NA SOLICITAÇÃO \n ${error}`)
  }
}

function listnerButtonPersonCheck() {
  const buttonCheck = window.document.querySelector("button#checar_pessoa_id");
  buttonCheck.addEventListener('click', async(event) => {
    event.preventDefault();
    /* enquanto a requsição estiver em andamento desabilitar o botão de checar */
    buttonCheck.disabled = true;
    try {
      await verifyPerson();
    } catch (error) {
      console.error(error);
    }
    buttonCheck.disabled = false;
    
  });
}

listnerButtonContractCheck();
listnerButtonPersonCheck();