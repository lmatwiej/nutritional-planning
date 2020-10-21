console.log('page load - entered main.js for js-other api');

var submitButton = document.getElementById('bsr-submit-button');
submitButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log('entered getFormInfo!');
    // call displayinfo
    var name = document.getElementById("name-text").value;
    console.log('Name you entered is ' + name);
    makeNetworkCallToApi(name);

} // end of get form info

function makeNetworkCallToAgeApi(name){
    console.log('entered make nw call' + name);
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = "https://api.nationalize.io?name=" + name;
    xhr.open("GET", url, true); // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateWithFirstResponse(name, xhr.responseText);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(null) // last step - this actually makes the request

} // end of make nw call

function updateAgeWithFirstResponse(name, response_text){
    var response_json = JSON.parse(response_text);
    // update a label
    var label1 = document.getElementById("response-line1");

    if(response_json['country'] == null){
        label1.innerHTML = 'Apologies, we could not predict your country.'
    } else{
        var code = response_json['country'][0]['country_id'];
        label1.innerHTML =  name + ', your assigned home country code is ' + code;
        makeNetworkCallToCountries(code);
    }
} // end of updateAgeWithResponse

function makeNetworkCallToCountries(code){
    console.log('entered make nw call ' + code);
    // set up url
    var xhr = new XMLHttpRequest(); // 1 - creating request object
    var url = "https://restcountries.eu/rest/v2/alpha/" + code;
    console.log(url);
    xhr.open("GET", url, true) // 2 - associates request attributes with xhr

    // set up onload
    xhr.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhr.responseText);
        // do something
        updateOutputWithResponse(code, xhr.responseText);
    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    // actually make the network call
    xhr.send(null) // last step - this actually makes the request

} // end of make nw call

function updateOutputWithResponse(code, response_text){
/*
    // dynamically adding label
    label_item = document.createElement("label"); // "label" is a classname
    label_item.setAttribute("id", "dynamic-label" ); // setAttribute(property_name, value) so here id is property name of button object

    var item_text = document.createTextNode(response_text); // creating new text
    label_item.appendChild(item_text); // adding something to button with appendChild()

    // option 1: directly add to document
    // adding label to document
    //document.body.appendChild(label_item);

    // option 2:
    // adding label as sibling to paragraphs
    var response_div = document.getElementById("response-div");
    response_div.appendChild(label_item);
*/
} // end of updateTriviaWithResponse
