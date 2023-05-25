function reinitializeDataTables() {
  //coloque a linguagem do DataTable portugues brasil
  $.extend( $.fn.dataTable.defaults, {
    "language": {
      "url": "//cdn.datatables.net/plug-ins/1.10.21/i18n/Portuguese-Brasil.json"
    }
  });
  $('#table-repasse-retido').DataTable();
  $('#table-repasses-retidos-nao-aprovadas').DataTable();
  $('#table-repasses-retidos-aprovadas').DataTable();
}
window.addEventListener("DOMContentLoaded", (event) => {
  Unicorn.addEventListener("updated", async (component) => {
      reinitializeDataTables();
  });
});
$(document).ready(function(){
  reinitializeDataTables();
});