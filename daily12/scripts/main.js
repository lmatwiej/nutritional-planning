console.log("Page load happened!")

var submitButton = document.getElementById('bsr-submit-button')
submitButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log("Entered get Form Info!")
    // get text from title, author and story
    var task_name = document.getElementById('task-name').value;
    var task_description = document.getElementById('task-description').value;
    console.log('name:' + task_name + ' conent: ' + task_description);

    // get checkbox state
    if (document.getElementById('urgency').checked){
        markUrgent();
    }
	
	reminder_dict={};
	reminder_dict['name'] = task_name;
	reminder_dict['content'] = task_description;
    displayReminder(reminder_dict);

}

function markUrgent() {
}

function displayReminder(reminder_dict){
    console.log('entered displayReminder!');
    console.log(reminder_dict);
    // get fields from story and display in label.
    var reminder_title = document.getElementById('reminder_top');
    reminder_title.innerHTML = reminder_dict['name'];
	
	var reminder_body = document.getElementById('reminder-body');
	reminder_body.innerHTML = reminder_dict['content'];

}

