console.log('page load');

var submitButton = document.getElementById('submit-button');
submitButton.onmouseup = getFormInfo;
console.log('After send button');

function getFormInfo(){
    console.log('entered getFormInfo!');
    // call displayinfo
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

function updateWithResponse(response_text){

    // update a label
    var answer = document.getElementById("answer-label");
    answer.innerHTML = response_text;
}
