$(document).ready(function() {
  // carousel
  $('.carousel').carousel();
  // side navbar
  $(".button-collapse").sideNav();
  // collapsible
  $('.collapsible').collapsible();
  // signin modal
  $('#signinmodal').modal();
  // signup modal
  $('#signupmodal').modal();
  // cart modal
  $('#cartmodal').modal();
  // change password
  $('.modal').modal();
  // category bar dropdown
  $(".dropdown-button").dropdown();
  // select
  $('select').material_select();
  // search
  $('#search').keypress(function(e) {
    if (e.which == 13) {
      console.log('enter pressed');
      e.preventDefault();
      $('#search-form').submit();
    }
  });
  // file input
  var fileInput = document.querySelector(".input-file"),
    button = document.querySelector(".input-file-trigger"),
    the_return = document.querySelector(".file-return");

  button.addEventListener("keydown", function(event) {
    if (event.keyCode == 13 || event.keyCode == 32) {
      fileInput.focus();
    }
  });
  button.addEventListener("click", function(event) {
    fileInput.focus();
    return false;
  });
  fileInput.addEventListener("change", function(event) {
    the_return.innerHTML = this.value;
  });
});
