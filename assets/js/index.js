function checkPassword() {
  var password = document.getElementById("password").value;
  if (password === "battieboys") {
    document.getElementById("accesgranted").src = "assets/accesgranted.svg";
    document.getElementById("accesgranted").style.display = "block";
      setTimeout(function() {
      window.location.href = "homepage.html";
    }, 1500);
  } else {
    document.getElementById("accesdenied").src = "assets/accesdenied.svg";
    document.getElementById("accesdenied").style.display = "block";
      setTimeout(function() {
      window.location.href = "index.html";
    }, 1500);
  }
}