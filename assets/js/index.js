function checkPassword() {
  var password = document.getElementById("password").value;
  if (password === "battieboys") {
    document.getElementById("accesgranted").src = "assets/img/accesgranted.svg";
    document.getElementById("accesgranted").style.display = "block";
      setTimeout(function() {
      window.location.href = "enter.html";
    }, 1500);
  } else {
    document.getElementById("accesdenied").src = "assets/img/accesdenied.svg";
    document.getElementById("accesdenied").style.display = "block";
      setTimeout(function() {
      window.location.href = "index.html";
    }, 1500);
  }
}

function redirectLogin() {
  window.location.href = "login.html";

}

function redirectRegister() {
  window.location.href = "register.html";

}