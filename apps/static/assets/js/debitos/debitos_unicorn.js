function reinitializeDataTables() {
  $.extend( $.fn.dataTable.defaults, {
    "language": {
      "url": "/static/assets/js/Portuguese-Brasil.json"
    }
  });
  $('#table-debito').DataTable();
  $('#table-debito-aprovadas').DataTable();
  $('#table-debito-nao-aprovadas').DataTable();
}
window.addEventListener("DOMContentLoaded", (event) => {
  Unicorn.addEventListener("updated", async (component) => {
      reinitializeDataTables();
  });
});
$(document).ready(function(){
  reinitializeDataTables();
});