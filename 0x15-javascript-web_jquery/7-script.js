$('document').ready(function () {
  $.getJSON('https://swapi.co/api/people/5/?format=json', function (value) {
    $('DIV#character').text(value.name);
  });
});
