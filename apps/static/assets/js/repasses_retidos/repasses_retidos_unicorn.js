function reinitializeDataTables() {
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