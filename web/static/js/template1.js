const navToggle = document.querySelector(".nav-toggle1");
const navMenu = document.querySelector(".nav-menu1");

navToggle.addEventListener("click", () => {
  navMenu.classList.toggle("nav-menu_visible1");

  if (navMenu.classList.contains("nav-menu_visible1")) {
    navToggle.setAttribute("aria-label", "Cerrar menú");
  } else {
    navToggle.setAttribute("aria-label", "Abrir menú");
  }
});

document.getElementById("aceptar_terminos").addEventListener('change', checkAccepted);

function checkAccepted(event) {
  var btnEnviar = document.getElementById("btnEnviar1");
  console.log(this.checked);
  btnEnviar.disabled = !this.checked;

}


