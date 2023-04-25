$(document).on('click', '.aprovar-parcela-taxa-btn', function(event) {
  event.preventDefault();
  
  var url = $(this).attr('href');
  
  $.ajax({
    url: url,
    type: 'GET',
    success: function(data) {
      var parcelasTaxas = data.parcelas_taxas;
      var dataInicio = data.data_inicio;
      var dataFim = data.data_fim;
      
      var $tbody = $('#parcelas-taxas-table tbody');
      $tbody.empty();
      
      $.each(parcelasTaxas, function(index, parcelaTaxa) {
        var $tr = $('<tr>');
        
        var $tdAcoes = $('<td>');
        var $aprovarBtn = $('<a>', {
          'href': '/aprovar_parcela_taxa/' + parcelaTaxa.id + '/' + dataInicio + '/' + dataFim,
          'class': 'btn btn-success aprovar-parcela-taxa-btn',
          'text': 'Aprovar'
        });
        $tdAcoes.append($aprovarBtn);
        
        var $tdIdContrato = $('<td>', {'text': parcelaTaxa.id_contrato});
        var $tdComprador = $('<td>', {'text': parcelaTaxa.comprador});
        var $tdIdComprador = $('<td>', {'text': parcelaTaxa.id_comprador});
        var $tdVendedor = $('<td>', {'text': parcelaTaxa.vendedor});
        var $tdIdVendedor = $('<td>', {'text': parcelaTaxa.id_vendedor});
        var $tdParcela = $('<td>', {'text': parcelaTaxa.parcela});
        var $tdDtVencimento = $('<td>', {'text': parcelaTaxa.dt_vencimento});
        var $tdValor = $('<td>', {'text': parcelaTaxa.valor});
        var $tdTcc = $('<td>', {'text': parcelaTaxa.tcc});
        var $tdDescontoTotal = $('<td>', {'text': parcelaTaxa.desconto_total});
        var $tdHonorarios = $('<td>', {'text': parcelaTaxa.honorarios});
        var $tdRepasse = $('<td>', {'text': parcelaTaxa.repasse});
        
        $tr.append($tdAcoes, $tdIdContrato, $tdComprador, $tdIdComprador, $tdVendedor, $tdIdVendedor, $tdParcela, $tdDtVencimento, $tdValor, $tdTcc, $tdDescontoTotal, $tdHonorarios, $tdRepasse);
        
        $tbody.append($tr);
      });
    },
    error: function() {
      alert('Erro ao carregar dados da tabela!');
    }
  });
});
