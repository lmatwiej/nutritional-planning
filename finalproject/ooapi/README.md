Milestone 1 README: OO API

The OO API includes two API's: food_library.py and favorites_library.py.

The first one, food_library.py, includes function needed to interact with the data in food_data.dat containing a number of foods, their food groups, and their nutritional information. The food_library.py api loads the data from that file upon construction and holds it in a series of dictionaries that all use "fid" (food id) value to reference different pieces of info for the same food. The functions included provided different utilities for accessing or manipulating that data depending on requests from the server. For example, the get_food request would be used to obtain a specific food if a GET request was made to the correct endpoint.

The second one, favorites_library.py, originated from group discussions organized by Professor Kumar during class time. One other group suggested the idea of having a favorites component where a user can categorize a food from the food data retrieved in food_library.dat as a favorite and assign it a rating. The favorites_library.py api creates a dictionary where food names serve as keys with ratings for their values. The number of functions within the api provide ways to manipulate/access that dictionary: retrieve a rating, see all its keys and values, update a rating, get a filtered output, etc. As with the food_library.py, these functions provide utilities for the server to use in order to adequately handle client requests.

Both api's have their unique tests, which verify that the api functions work as expected:

1) To test food_library, run this command in your terminal: "python3 test_food_api.py"

2) To test favorites_library, run this command in your terminal: "python3 test_favorites_api.py"