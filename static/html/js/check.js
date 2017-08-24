$(function() {

  var redirectIfClientIsAvailable = function(eidClient) {
    $('#result').html('Detected eID-Client. Forwarding...');
    setTimeout(function() {
      window.location = "../api/eIdService/getTcTokenUrl?protocol=" + eidClient.protocol + "&host=" + eidClient.host + "&" + window.location.search.substr(1);
    }, 3000);
  };

  var checker = new ClientChecker(redirectIfClientIsAvailable, 5000);

  $('#continueButton').click(function() {
      window.location = "../api/eIdService/getTcTokenUrl?" + window.location.search.substr(1);
  });
});