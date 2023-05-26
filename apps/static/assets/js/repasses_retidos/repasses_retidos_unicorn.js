function reinitializeDataTables() {
  //coloque a linguagem do DataTable portugues brasil
  $.extend( $.fn.dataTable.defaults, {
    "language": {
      "url": "/static/assets/js/Portuguese-Brasil.json"
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