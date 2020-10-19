console.log("Page load happened!")

var submitButton = document.getElementById('bsr-submit-button')
submitButton.onmouseup = getFormInfo;

var clearButton = document.getElementById('bsr-clear-button')
clearButton.onmouseup = clearForm;

function clearForm() {
    console.log("Entered clear form");
    document.getElementById('task-name').value = "";
    document.getElementById('task-description').value = "";
    var reminder_title = document.getElementById('reminder-top');
    reminder_title.innerHTML = "";
    var reminder_body = document.getElementById('reminder-body');
    reminder_body.innerHTML = "";
}


function getFormInfo(){
    console.log("Entered get Form Info!")
    // get text from title, author and story
    var task_name = document.getElementById('task-name').value;
    var task_description = document.getElementById('task-description').value;
    console.log('name:' + task_name + ' content: ' + task_description);

    // get checkbox state
    if (document.getElementById('urgency-checkbox-value').checked){
        console.log("Checked urgency");
        task_name += " (URGENT)";
    } else {
        console.log("Urgency not checked");
    }
	
	reminder_dict={};
	reminder_dict['name'] = task_name;
	reminder_dict['content'] = task_description;
    displayReminder(reminder_dict);

}

function displayReminder(reminder_dict){
    console.log('entered displayReminder!');
    console.log(reminder_dict);
    var reminder_title = document.getElementById('reminder-top');
    reminder_title.innerHTML = reminder_dict['name'];
	
	var reminder_body = document.getElementById('reminder-body');
	reminder_body.innerHTML = reminder_dict['content'];

}

