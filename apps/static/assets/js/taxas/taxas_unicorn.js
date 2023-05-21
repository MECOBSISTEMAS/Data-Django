/* async function reinitializeDataTables() {
  console.log('in reinitializeDataTables')
  console.log('DataTable().destroy()')
  $('#table-taxas').DataTable().destroy();
  $('#table-taxas-aprovadas').DataTable().destroy();
  $('#table-taxas-nao-aprovadas').DataTable().destroy();
  await new Promise((resolve) => setTimeout(resolve, 800));
  console.log('Refazer o datatable apos o destroy e promise')
  $('#table-taxas').DataTable();
  $('#table-taxas-aprovadas').DataTable();
  $('#table-taxas-nao-aprovadas').DataTable();
} */

function reinitializeDataTables() {
  $('#table-taxas').DataTable();
  $('#table-taxas-aprovadas').DataTable();
  $('#table-taxas-nao-aprovadas').DataTable();
}
window.addEventListener("DOMContentLoaded", (event) => {
  Unicorn.addEventListener("updated", async (component) => {
      reinitializeDataTables();
  });
});
$(document).ready(function(){
  reinitializeDataTables();
});