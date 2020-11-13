import unittest
import requests
import json

class TestReset(unittest.TestCase):

    # Define url endpoints needed for the unittests
    SITE_URL = 'http://student10.cse.nd.edu:51077' # replace with your port id
    print("Testing for server: " + SITE_URL)
    RESET_URL = SITE_URL + '/reset/'
    FOOD_URL = SITE_URL + '/food_name/'

    # Test PUT_KEY
    def test_put_reset_index(self):

        # Delete the database
        m = {}
        r = requests.delete(self.FOOD_URL, data = json.dumps(m))

        # Now call put and proceed to see if database still there
        # If database restored after deletion, put request succeeded
        r = requests.put(self.RESET_URL)
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # To check if database restored, issue get request
        r = requests.get(self.FOOD_URL)
        resp = json.loads(r.content.decode('utf-8'))

        # Populate a testfood dictionary with id = 200 information
        # Dictionary will not be empty if put was successful
        testfood = {}
        foods = resp['food']
        for food in foods:
            if food['id'] == 200:
                testfood = food

        # Test if the food is correct
        self.assertEqual(testfood['name'], 'TURKEY BACON')
        self.assertEqual(testfood['group'], 'Sausages and Luncheon Meats')
        self.assertEqual(testfood['kcal'], 368)
        self.assertEqual(testfood['protein'], 29.5)
        self.assertEqual(testfood['fat'], 25.87)
        self.assertEqual(testfood['carb'], 4.24)

    # Test for PUT_KEY
    def test_put_reset_key(self):

        # First delete entry under food id 200
        food_id = 200
        m = {}
        r = requests.delete(self.FOOD_URL + str(food_id), data = json.dumps(m))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')


        # After deleting, put the food_id back
        r = requests.put(self.RESET_URL + str(food_id))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # To check that it's back and put worked, issue a get request
        # Check to see if correct information is there
        r = requests.get(self.FOOD_URL + str(food_id))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'TURKEY BACON')
        self.assertEqual(resp['group'], 'Sausages and Luncheon Meats')
        self.assertEqual(resp['kcal'], 368)
        self.assertEqual(resp['prot'], 29.5)
        self.assertEqual(resp['fat'], 25.87)
        self.assertEqual(resp['carb'], 4.24)

if __name__ == "__main__":
    unittest.main()
