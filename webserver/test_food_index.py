import unittest
import requests
import json

class TestFoodIndex(unittest.TestCase):

    # Define endpoints to which requests are made
    SITE_URL = 'http://student10.cse.nd.edu:51077'
    print("Testing for server: " + SITE_URL)
    FOOD_URL = SITE_URL + '/food_name/'
    RESET_URL = SITE_URL + '/reset/'

    # Helper function that resets the data so individual tests do not affect each other
    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, json.dumps(m))

    # Helper function to check if valid JSON
    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    # Test for GET_INDEX
    def test_food_index_get(self):
        self.reset_data()

        # Send get request to /food_name
        r = requests.get(self.FOOD_URL)

        # Check if JSON
        self.assertTrue(self.is_json(r.content.decode()))

        # Load all the dictionary into a string
        resp = json.loads(r.content.decode())

        # Iterate through all the foods and pick out id = 200
        testfood = {}
        foods = resp['food']
        for food in foods:
            if food['id'] == 200:
                testfood = food

        # Test if correct food retrieved under id = 200
        self.assertEqual(testfood['name'], 'TURKEY BACON')
        self.assertEqual(testfood['group'], 'Sausages and Luncheon Meats')
        self.assertEqual(testfood['kcal'], 368)
        self.assertEqual(testfood['protein'], 29.5)
        self.assertEqual(testfood['fat'], 25.87)
        self.assertEqual(testfood['carb'], 4.24)

    # Test for POST Index
    def test_food_index_post(self):
        self.reset_data()

        # Create a dictionary with food information to be added
        m = {}
        m['name'] = 'Gerber'
        m['group'] = 'Baby Foods'
        m['kcal'] = '66'
        m['prot'] = '2'
        m['fat'] = '3'
        m['carb'] = '8'

        # Make the request with new info as the body
        r = requests.post(self.FOOD_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        # Test if the posted id was 988 and response was success
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['id'], 988)

        # Test to see if a get request to the FOOD_URL with id 988 will return newly added entry
        r = requests.get(self.FOOD_URL + str(resp['id']))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        # Test each entry element
        self.assertEqual(resp['name'], m['name'])
        self.assertEqual(resp['group'], m['group'])
        self.assertEqual(resp['kcal'], m['kcal'])
        self.assertEqual(resp['prot'], m['prot'])
        self.assertEqual(resp['fat'], m['fat'])
        self.assertEqual(resp['carb'], m['carb'])

    # Test for DELETE_INDEX
    def test_food_index_delete(self):
        self.reset_data()

        # Empty dictionary is message body per specification
        m = {}
        r = requests.delete(self.FOOD_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        # Try to get all the foods
        r = requests.get(self.FOOD_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        # Test is successful if the food dictionary returned is empty
        food = resp['food']
        self.assertFalse(food)

if __name__ == "__main__":
    unittest.main()
