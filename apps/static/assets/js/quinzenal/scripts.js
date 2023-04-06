//*apps/static/assets/js/quinzenal/scripts.js

window.document.querySelectorAll('#aprovar-repasse').forEach((element) => {
  element.addEventListener('click', (event) => {
    event.preventDefault()
    console.log(event.target);
    //xml = XMLHttpRequest()
  })
})