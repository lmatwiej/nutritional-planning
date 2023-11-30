Names and Netids:

    Lukasz Matwiejczyk - lmatwiej
    Pablo Martinez-Abrego Gonzalez - pmarti22

OO API

    The OO API includes two API's: food_library.py and favorites_library.py. The first one, food_library.py, includes functions needed to interact with the data in food_data.dat containing a number of foods, their food groups, and their nutritional information. The food_library.py api loads the data from that file upon construction and holds it in a series of dictionaries that all use "fid" (food id) value to reference different pieces of info for the same food. The functions included provided different utilities for accessing or manipulating that data depending on requests from the server. For example, the get_food request would be used to obtain a specific food if a GET request was made to the correct endpoint.

    The second one, favorites_library.py, originated from group discussions organized by Professor Kumar during class time. One other group suggested the idea of having a favorites component where a user can categorize a food from the food data retrieved in food_library.dat as a favorite and assign it a rating. The favorites_library.py api parallels the structure of the food_library.py api except that it has two dictionaries storing names and ratings related by a food id. The number of functions within the api provide ways to manipulate/access that dictionary: retrieve a rating, see all its keys and values, update a rating, etc. As with the food_library.py, these functions provide utilities for the server to use in order to adequately handle client requests.

    Both api's have their unique tests, which verify that the api functions work as expected. Each api test contains a unittest for every function that involves comparing the result of a function a correct/expected result. If the correct result comes through, the unittests pass. Here is how you run them:

    - To test food_library, run this command in your terminal: "python3 test_food_api.py"

    - To test favorites_library, run this command in your terminal: "python3 test_favorites_api.py"

    If all the tests pass, the api's are good to go.

Web Service information

    The web service uses port 51077, and the files have http://student10.cse.nd.edu currently hardcoded for the host. The web service customer can use the different resources specified by the JSON Specification (link below) to manipulate database data or access database data. Data includes nutritional facts about food as well as favorites. Please see JSON Spec for more information on what return to expect from eaach resource.

JSON Specification for REST API

    The JSON Specification can be found at the following link available to all grad TA's and the professor:

    https://docs.google.com/document/d/1N2qYPYhGMLyEl74ss6YjGge0J-xd0t7OUW2op6pvroA/edit#

User Interaction

    The user interacts with the app in two ways: the search feature and the favorites log feature.

    The search feature affords the user an opportunity to type in the name of any potential food item. Upon clicking the search button, the application renders a table with search results. Search results contain any food names that included the query string plus the nutritional information for each food. For example, if the user wants to know more about apples, the user can search 'apples' and observe the kcal, protein, fat, and carb values mostly in grams for the standard apple.

    The search feature also includes a second search feature (selected from the dropdown). The user has the option to search for foods with specific nutritional values. The second dropdown menu choice generates a form that the user fills out and submits. The inputs provided serve as filters and return a filtered set of data.

    Each food entry in the table also includes a food id. This id is crucial for the next aspect of the interaction: the favorites log feature. After the user does some searching (and maybe tasting), he/she can add the food item a log of favorites on the right. The user inputs the id listed in the table, inputs a rating, and then clicks one of three buttons. The submit button adds the food id's name and the rating to the log. This change is immediately visible in the table below. The delete button will delete the food id, if present, from the table. The update button will reassign the new rating input to the food id.

Starting the Server:

    The server.py is within the webserver directory under finalproject. To run the server, please run "python3 server.py" on student10.cse.nd.edu. Then visit the link to the front end client listed as final project on the public page of the Gitlab: 
    http://pmarti22.gitlab.io/programming-paradigms-final-project/

Tests for the Web Client:

    - To test search functionality, the client can enter these values and expect these results:
        a) Under 'food' search in dropdown, search 'chocolate syrup' and expect to see id's 518 and 841
        b) Under 'food' search in dropdown, search 'blueberries' and expect to see id 251

    - To test favorites functionality, the client can enter these values and expect these results
        a) Enter 782 for food id and any rating; expect to see popcorn in the table with the rating
        b) Enter 782 again for food id with a new rating and click update; expect to see popcorn with the new rating
        c) Enter 782 and click delete; expect table to be empty

Complexity:

    The project's complexity manifests in the various functionalities it supports and how those functionalities relate to each other. The project essentially takes on a twofold structure as described throughout this documentation. The first aspect allows the user to search for nutritional information as conveniently and flexibly as possible. The app goes beyond the low complexity of a simple 'search and provide model' with two subsets of the search. The two search options -- 1) food and 2) nutritional facts -- significantly expand the scale of the search itself. Essentially, it no longer serves as a phone book for foods but also as a filter extremely relevant to user's underlying motivation in visiting the web service. 

    The search functionality already demonstrates an expanded scale and added complexity, yet it is only one level of the whole project's complexity. The higher level connects this search (already expansive in scale on its own) with a favorites log via the food id. The user can extend the interaction beyond the search itself and allow the app to be a one-stop shop for tracking favorites from the list. This favorites log on the right side of the screen itself branches out in complexity to include delete and update options as well. This extra level of complexity encourages user interaction and even prompts the user to revisit the app to search new foods and discover new favorites to replace the old.

    The complexity is reflected in the code through the breakdown of two controllers: one for the search and one for the favorites. The controllers interact with similar API's in very similar ways to accomplish complementary tasks. Thus, not only does the structure amplify scale and add some complexity; it also integrates these moving parts into one fluid workflow for the user.

Link to Presentation Slides

    https://docs.google.com/presentation/d/15hnIlHB_ARVpCtwsgEDsreQkdV81LqdhAi9N5x4CteY/edit?usp=sharing
