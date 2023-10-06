function reinitializeDataTables() {
  $.extend( $.fn.dataTable.defaults, {
    "language": {
      "url": "/static/assets/js/Portuguese-Brasil.json"
    }
  });
  $('#parcelas-taxas-table').DataTable();
}
window.addEventListener("DOMContentLoaded", (event) => {
  Unicorn.addEventListener("updated", async (component) => {
      reinitializeDataTables();
  });
});
$(document).ready(function(){
  reinitializeDataTables();
});