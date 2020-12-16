console.log("ABBA");

$(document).ready(function() {
  $.ajax({
    url: "http://localhost:8080/get?v=1",
    dataType: "json"
  }).done(function (msg) {
    console.log(msg);
  });
});
