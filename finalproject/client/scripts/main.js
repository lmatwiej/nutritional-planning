console.log('page load');

<<<<<<< HEAD
var sendButton = document.getElementById('send-button');
sendButton.onmouseup = getFormInfo;
console.log('After send button');
var send2Button = document.getElementById('send2-button');
send2Button.onmouseup = getForm2Info;
console.log('After send2 button');
var clearButton = document.getElementById('clear-button');
clearButton.onmouseup = clearForm;
console.log('After clear button');
var clear2Button = document.getElementById('clear2-button');
clear2Button.onmouseup = clear2Form;
console.log('After clear2 button');
=======
var submitButton = document.getElementById('submit-button');
submitButton.onmouseup = getFormInfo;
console.log('After send button');
>>>>>>> 06be47695240812aab8cca6afbe39c33811d5972

function getFormInfo(){
    console.log('entered getFormInfo!');
    // call displayinfo
<<<<<<< HEAD
    var url_base = "http://student10.cse.nd.edu"
    var port_num = 51077
    var action = "GET"; // default
    var message_body = null;
    var key = document.getElementById("food-input").value;

    makeRequest(url_base, port_num, action, key, message_body);

} // end of get form info

function makeRequest(url_base, port_num, action, key, message_body){

    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = url_base + ":" + port_num + "/food_name/";
    xhr.open(action, url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        var jsonData = JSON.parse(xhr.responseText);
        var foodObj = jsonData["food"]; //bar
        // var name = foodObj[1].name;
        var output = [];
        var i;
        var str;
        var food_name = key.toLowerCase();
        for (i = 0; i < foodObj.length; i++) {
          str = foodObj[i].name;
          if (str.indexOf(key) >= 0) {
            output.push(foodObj[i]);
          }
        }

        var html = "<table border='1|1'>";
        html+="<tr>";
        html+="<td>"+"Name"+"</td>";
        html+="<td>"+"Group"+"</td>";
        html+="<td>"+"KCal"+"</td>";
        html+="<td>"+"Protein"+"</td>";
        html+="<td>"+"Fat"+"</td>";
        html+="<td>"+"Carbs"+"</td>";
        html+="<td>"+"Favorite?"+"</td>";

        html+="</tr>";
for (var i = 0; i < output.length; i++) {
    html+="<tr>";
    html+="<td>"+output[i].name+"</td>";
    html+="<td>"+output[i].group+"</td>";
    html+="<td>"+output[i].kcal+"</td>";
    html+="<td>"+output[i].protein+"</td>";
    html+="<td>"+output[i].fat+"</td>";
    html+="<td>"+output[i].carb+"</td>";
    html+="<td><button>★</button></td>";

    html+="</tr>";

}
html+="</table>";
document.getElementById("answer-label").innerHTML = html;

        // do something
        // document.getElementById("answer-label").innerHTML = JSON.stringify(output, null, 4);
        // updateWithResponse(output);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(message_body); // last step - this actually makes the request

} // end of make nw call

function clearForm() {
  document.getElementById("answer-label").innerHTML = "-";
}

function getForm2Info() {
  console.log('entered getFormInfo!');
  // call displayinfo
  var url_base = "http://student10.cse.nd.edu"
  var port_num = 51077
  var action = "GET"; // default
  var message_body = null;
  var key = document.getElementById("calstext").value;

  makeRequest2(url_base, port_num, action, key, message_body);
}

function makeRequest2(url_base, port_num, action, key, message_body){

    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = url_base + ":" + port_num + "/food_name/";
    xhr.open(action, url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        var jsonData = JSON.parse(xhr.responseText);
        var foodObj = jsonData["food"]; //bar
        // var name = foodObj[1].name;
        var output = [];
        var i;
        var tcals;
        var tprot;
        var tfats;
        var tcarbs;

        var cals = parseFloat(key);
        var calLen = document.getElementById('calstext');
        var prot = parseFloat(document.getElementById("protstext").value);
        var protLen = document.getElementById('protstext');
        var fat = parseFloat(document.getElementById("fatstext").value);
        var fatLen = document.getElementById('fatstext');
        var carbs = parseFloat(document.getElementById("carbstext").value);
        var carbLen = document.getElementById('carbstext');

        for (i = 0; i < foodObj.length; i++) {
          tcals = foodObj[i].kcal;
          tprot = foodObj[i].protein;
          tfat = foodObj[i].fat;
          tcarbs = foodObj[i].carb;
          if (!(tcals > cals-5 && tcals < cals+5) && (calLen.value.length != 0)) {
            continue;
          }
          if (!(tprot > prot-1 && tprot < prot+1) && (protLen.value.length != 0)) {
            continue;
          }
          if (!(tfat > fat-3 && tfat < fat+3) && (fatLen.value.length != 0)) {
            continue;
          }
          if (!(tcarbs > carbs-3 && tcarbs < carbs+3) && (carbLen.value.length != 0)) {
            continue;
          }
          output.push(foodObj[i]);
        }

        var html = "<table border='1|1'>";
        html+="<tr>";
        html+="<td>"+"Name"+"</td>";
        html+="<td>"+"Group"+"</td>";
        html+="<td>"+"KCal"+"</td>";
        html+="<td>"+"Protein"+"</td>";
        html+="<td>"+"Fat"+"</td>";
        html+="<td>"+"Carbs"+"</td>";
        html+="<td>"+"Favorite?"+"</td>";

        html+="</tr>";
for (var i = 0; i < output.length; i++) {
    html+="<tr>";
    html+="<td>"+output[i].name+"</td>";
    html+="<td>"+output[i].group+"</td>";
    html+="<td>"+output[i].kcal+"</td>";
    html+="<td>"+output[i].protein+"</td>";
    html+="<td>"+output[i].fat+"</td>";
    html+="<td>"+output[i].carb+"</td>";
    var id = "\"" + output[i].id + "\""
    html+="<td><button id="+id+">★</button></td>";

    html+="</tr>";

}
html+="</table>";
document.getElementById("answer2-label").innerHTML = html;

        // do something
        // document.getElementById("answer-label").innerHTML = JSON.stringify(output, null, 4);
        // updateWithResponse(output);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(message_body); // last step - this actually makes the request

} // end of make nw call

function clear2Form() {
  document.getElementById("answer2-label").innerHTML = "-";
}
=======
    var food_input = document.getElementById("food-input").foodInput;

    /* var action = "GET"; // default

    if (document.getElementById("radio-get").checked) {
        action = "GET";
    } else if (document.getElementById("radio-put").checked) {
        action = "PUT";
    } else if (document.getElementById("radio-post").checked) {
        action = "POST";
    } else if (document.getElementById("radio-delete").checked) {
        action = "DELETE";
    }

    var key = "";
    if (document.getElementById("checkbox-use-key").checked) {
        key = document.getElementById("input-key").value;
    }

    var message_body = null;
    if (document.getElementById("checkbox-use-message").checked) {
        message_body = document.getElementById("text-message-body").value;
    } */

    makeRequest(food_input);

} // end of get form info

function makeRequest(food_input){


    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = "student10.cse.nd.edu:51077/food_name/" + food_input
    var action = "GET"

    xhr.open(action, url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateWithResponse(xhr.responseText);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(null) // last step - this actually makes the request

} // end of make nw call
>>>>>>> 06be47695240812aab8cca6afbe39c33811d5972

function updateWithResponse(response_text){

    // update a label
    var answer = document.getElementById("answer-label");
    answer.innerHTML = response_text;
}
