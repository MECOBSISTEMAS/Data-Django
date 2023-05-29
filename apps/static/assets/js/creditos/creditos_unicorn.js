function reinitializeDataTables() {
  $.extend( $.fn.dataTable.defaults, {
    "language": {
      "url": "/static/assets/js/Portuguese-Brasil.json"
    }
  });
  $('#table-credito').DataTable();
  $('#table-credito-aprovadas').DataTable();
  $('#table-credito-nao-aprovadas').DataTable();
}
window.addEventListener("DOMContentLoaded", (event) => {
  Unicorn.addEventListener("updated", async (component) => {
      reinitializeDataTables();
  });
});
$(document).ready(function(){
  reinitializeDataTables();
});