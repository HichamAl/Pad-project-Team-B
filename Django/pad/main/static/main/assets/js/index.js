

function checkPassword() {
  var password = document.getElementById("password").value;
  if (password === "battieboys") {
    document.getElementById("accesgranted").src = "/static/main/assets/img/accesgranted.svg";
    document.getElementById("accesgranted").style.display = "block";
      setTimeout(function() {
      window.location.href = "../enter";
    }, 1500);
  } else {
    document.getElementById("accesdenied").src = "/static/main/assets/img/accesdenied.svg";
    document.getElementById("accesdenied").style.display = "block";
      setTimeout(function() {
      window.location.href = "../index";
    }, 1500);
  }
}

function redirectLogin() {
  window.location.href = "../login";

}

function redirectRegister() {
  window.location.href = "../register";

}