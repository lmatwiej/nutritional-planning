import unittest
import requests
import json

class TestFoodIndex(unittest.TestCase):

    # Define endpoints to which requests are made
    SITE_URL = 'http://student10.cse.nd.edu:51077'
    print("Testing for server: " + SITE_URL)
    FAVORITES_URL = SITE_URL + '/favorites/'
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

        # Add two favorites to an empty favorites log
        m = {}
        m['name'] = 'Honey'
        m['rating'] = 7

        # First post
        r = requests.post(self.FAVORITES_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))

        m['name'] = 'Tea'
        m['rating'] = 10

        # Second post
        r = requests.post(self.FAVORITES_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))

        # Send get request to /favorites/ -- this should return id's 1 and 2
        r = requests.get(self.FAVORITES_URL)

        # Check if JSON
        self.assertTrue(self.is_json(r.content.decode()))

        # Load all the dictionary into a string
        resp = json.loads(r.content.decode())

        # Iterate through all the foods and pick out id = 1
        testfood = {}
        foods = resp['food']
        for food in foods:
            if food['id'] == 2:
                testfood = food #hould be tea, 10

        # Test if correct food retrieved under id = 200
        self.assertEqual(testfood['name'], 'Tea')
        self.assertEqual(testfood['rating'], 10)

    # Test for POST Index
    def test_food_index_post(self):
        self.reset_data()

        # Create a dictionary with name, rating to be added
        m = {}
        m['name'] = 'Honey'
        m['rating'] = 7

        # Make the request with new info as the body
        r = requests.post(self.FAVORITES_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        # Test if the posted id was 1; this should be the first favorite
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['id'], 1)

        # Test to see if a get request to the FOOD_URL with id 1 will return newly added entry
        r = requests.get(self.FAVORITES_URL + str(resp['id']))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        # Test if the name and rating are honey and 7
        self.assertEqual(resp['name'], m['name'])
        self.assertEqual(resp['group'], m['rating'])

    # Test for DELETE_INDEX
    def test_food_index_delete(self):
        self.reset_data()

        # Empty dictionary is message body per specification
        m = {}
        r = requests.delete(self.FAVORITES_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        # Try to get all the foods
        r = requests.get(self.FAVORITES_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        # Test is successful if the favorites dictionary returned is empty
        food = resp['food']
        self.assertFalse(food)

if __name__ == "__main__":
    unittest.main()
