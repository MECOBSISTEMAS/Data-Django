function reinitializeDataTables() {
  $.extend( $.fn.dataTable.defaults, {
    "language": {
      "url": "/static/assets/js/Portuguese-Brasil.json"
    }
  });
  $('#table-cob').DataTable();
}
window.addEventListener("DOMContentLoaded", (event) => {
  Unicorn.addEventListener("updated", async (component) => {
      reinitializeDataTables();
  });
});
$(document).ready(function(){
  reinitializeDataTables();
});