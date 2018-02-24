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
  // category bar dropdown
  $(".dropdown-button").dropdown();
  // search
  $('#search').keypress(function(e) {
    if (e.which == 13) {
      console.log('enter pressed');
      e.preventDefault();
      $('#search-form').submit();
    }
  });
});
