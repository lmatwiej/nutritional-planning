console.log("Page load happened!")

var clearButton = document.getElementById('bsr-clear-button')
clearButton.onmouseup = clearForm;
console.log("get clear button");

var submitButton = document.getElementById('bsr-submit-button')
submitButton.onmouseup = getFormInfo;

function clearForm() {
    document.getElementById('task-name').value = "";
    document.getElementById('task-description').value = "";
    var reminder_title = document.getElementById('reminder-top');
    reminder_title.innerHTML = "Reminder";
    var reminder_body = document.getElementById('reminder-body');
    reminder_body.innerHTML = "Reminder Message";
    var urgent_label = document.getElementById('urgent-label');
    if (urgent_label) {
        urgent_label.remove();
    }
}

function getFormInfo(){
    console.log("Entered get Form Info!")
    // get text from title, author and story
    var task_name = document.getElementById('task-name').value;
    var task_description = document.getElementById('task-description').value;
    console.log('name:' + task_name + ' conent: ' + task_description);

    // get checkbox state
    if (document.getElementById('urgency').checked){
        console.log("Checked urgency");
        markUrgent();
    } else {
        console.log("Urgency not checked");
    }
	
	reminder_dict={};
	reminder_dict['name'] = task_name;
	reminder_dict['content'] = task_description;
    displayReminder(reminder_dict);

}

function markUrgent() {
	console.log("Entered markUrgent");
	var newLabel = document.createElement("span");
	newLabel.setAttribute("id","urgent-label");
	newLabel.setAttrbiute("class", "label label-danger");
	newLabel.innerHTML("Urgent Reminder");
	var div = document.getElementById('reminder-top'); 
	div.append(newLabel);
}

function displayReminder(reminder_dict){
    console.log('entered displayReminder!');
    console.log(reminder_dict);
    // get fields from story and display in label.
    var reminder_title = document.getElementById('reminder-top');
    reminder_title.innerHTML = reminder_dict['name'];
	
	var reminder_body = document.getElementById('reminder-body');
	reminder_body.innerHTML = reminder_dict['content'];

}

