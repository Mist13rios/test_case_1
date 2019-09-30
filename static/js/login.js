function validateEmail(email) {
  var re = /\S+@\S+\.\S+/;
  return re.test(email);
}

function validate() {
  var email = $("#login").val();
  if (validateEmail(email)) {
    $("#login").submit()
  } else {
    $("#login").val("");
    alert('Wrong login format!')
  }
  return false;
}
