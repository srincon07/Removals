var basicConditions = JSON.parse(document.getElementById('Basic').text);

document.getElementById("id_type_0").onclick = function () {
  document.getElementById('warning').innerHTML = "<p>" + basicConditions + "</p>";
}

var standardConditions = JSON.parse(document.getElementById('Standard').text);

document.getElementById("id_type_1").onclick = function () {
  document.getElementById('warning').innerHTML = "<p>" + standardConditions + "</p>";
}

var vipConditions = JSON.parse(document.getElementById('VIP').text);

document.getElementById("id_type_2").onclick = function () {
  document.getElementById('warning').innerHTML = "<p>" + vipConditions + "</p>";
}