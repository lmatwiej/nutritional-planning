console.log('page load');

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

function getFormInfo() {
    console.log('entered getFormInfo!');
    // call displayinfo
    var url_base = "http://student10.cse.nd.edu"
    var port_num = 51077
    var action = "GET"; // default
    var message_body = null;
    var key = document.getElementById("food-input").value;

    makeRequest(url_base, port_num, action, key, message_body);

} // end of get form info

function makeRequest(url_base, port_num, action, key, message_body) {

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
            str = foodObj[i].name.toLowerCase();
            if (str.indexOf(key) >= 0) {
                output.push(foodObj[i]);
            }
        }

        var html = "<table border='1|1'>";
        html += "<tr>";
        html += "<td>" + "Name" + "</td>";
        html += "<td>" + "Group" + "</td>";
        html += "<td>" + "KCal" + "</td>";
        html += "<td>" + "Protein" + "</td>";
        html += "<td>" + "Fat" + "</td>";
        html += "<td>" + "Carbs" + "</td>";
        html += "<td>" + "Food ID" + "</td>";

        html += "</tr>";
        for (var i = 0; i < output.length; i++) {
            html += "<tr>";
            html += "<td>" + output[i].name + "</td>";
            html += "<td>" + output[i].group + "</td>";
            html += "<td>" + output[i].kcal + "</td>";
            html += "<td>" + output[i].protein + "</td>";
            html += "<td>" + output[i].fat + "</td>";
            html += "<td>" + output[i].carb + "</td>";
            html += "<td>" + output[i].id + "</td>";

            html += "</tr>";

        }
        html += "</table>";
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
  document.getElementById("answer-label").innerHTML = "";
}

function getForm2Info() {
    console.log('entered getForm2Info!');
    // call displayinfo
    var url_base = "http://student10.cse.nd.edu"
    var port_num = 51077
    var action = "GET"; // default
    var message_body = null;
    var key = document.getElementById("calstext").value;

    makeRequest2(url_base, port_num, action, key, message_body);

}

function makeRequest2(url_base, port_num, action, key, message_body) {

    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = url_base + ":" + port_num + "/food_name/";
    xhr.open(action, url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
            // must be written before send
            console.log(xhr.responseText);
            updateWithResponse2("hello");
        var jsonData = JSON.parse(xhr.responseText);
        var foodObj = jsonData["food"]; //bar
        var output = [];
        var i;
        var str;

        var cals = parseFloat(document.getElementById("calstext").value);
        var prots = parseFloat(document.getElementById("protstext").value);
        var carbs = parseFloat(document.getElementById("carbstext").value);
        var fats = parseFloat(document.getElementById("fatstext").value);
        var calLen = document.getElementById('calstext');
        var protLen = document.getElementById('protstext');
        var carbLen = document.getElementById('carbstext');
        var fatLen = document.getElementById('fatstext');


        for (i = 0; i < foodObj.length; i++) {
          var tcals = foodObj[i].kcal;
          var tprots = foodObj[i].protein;
          var tcarbs = foodObj[i].carb;
          var tfats = foodObj[i].fat;

          if (!(tcals >= cals-5 && tcals <= cals+5)) {
            if(!(calLen.value.length == 0)) {
              continue;
            }
          }
          if (!(tprots >= prots-3 && prots <= tprots+3)) {
            if(!(protLen.value.length == 0)) {
              continue;
            }
          }
          if (!(tcarbs >= carbs-1 && tcarbs <= carbs+1)) {
            if(!(carbLen.value.length == 0)) {
              continue;
            }
          }
          if (!(tfats >= fats-3 && tfats <= fats+3)) {
            if(!(fatLen.value.length == 0)) {
              continue;
            }
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
        html+="<td>"+"Food ID"+"</td>";

        html+="</tr>";
        for (var i = 0; i < output.length; i++) {
          html+="<tr>";
          html+="<td>"+output[i].name+"</td>";
          html+="<td>"+output[i].group+"</td>";
          html+="<td>"+output[i].kcal+"</td>";
          html+="<td>"+output[i].protein+"</td>";
          html+="<td>"+output[i].fat+"</td>";
          html+="<td>"+output[i].carb+"</td>";
          html += "<td>" + output[i].id + "</td>";

          html+="</tr>";

        }
        html+="</table>";
        document.getElementById("answer2-label").innerHTML = html;

        // do something
        // document.getElementById("answer-label").innerHTML = JSON.stringify(output, null, 4);
        // updateWithResponse(foodObj);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(message_body); // last step - this actually makes the request

} // end of make nw call

function clear2Form() {
  document.getElementById("answer2-label").innerHTML = "";
}

function updateWithResponse(response_text){

    // update a label
    var answer = document.getElementById("answer-label");
    answer.innerHTML = response_text;
}

function updateWithResponse2(response_text){

    // update a label
    var answer = document.getElementById("answer2-label");
    answer.innerHTML = response_text;
}
