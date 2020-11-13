import unittest
import requests
import json

class TestFood(unittest.TestCase):

    # Initialize endpoints to be used
    SITE_URL = 'http://student10.cse.nd.edu:51077' # replace with your port number and
    print("testing for server: " + SITE_URL)
    FOOD_URL = SITE_URL + '/food_name/'
    RESET_URL = SITE_URL + '/reset/'

    # Helper function that resets data at start of individual tests
    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, data = json.dumps(m))

    # Returns true if valid JSON
    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    # Test GET_KEY
    def test_food_get_key(self):
        self.reset_data()

        # Initialize food id and url endpoint
        food_id = 424
        r = requests.get(self.FOOD_URL + str(food_id))

        # Test if response is valid JSON 
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))

        # Test if the correct food information returned (under id = 424)
        self.assertEqual(resp['name'], 'ACORNS')
        self.assertEqual(resp['group'], 'Nut and Seed Products')
        self.assertEqual(resp['kcal'], 387)
        self.assertEqual(resp['prot'], 6.15)
        self.assertEqual(resp['fat'], 23.86)
        self.assertEqual(resp['carb'], 40.75)

    # Test PUT_KEY
    def test_food_put_key(self):
        self.reset_data()

        # Attempt to modify id = 424, which contains information on acorns

        # Define info for a new food entry
        m = {}
        m['name'] = 'Gerber'
        m['group'] = 'Baby Foods'
        m['kcal'] = '66'
        m['prot'] = '2'
        m['fat'] = '3'
        m['carb'] = '8'

        food_id = 90
        # Issue put request to food_id endpoint with the new information
        r = requests.put(self.FOOD_URL + str(food_id), data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # See if put request worked: if new data is now present at id = 424
        r = requests.get(self.FOOD_URL + str(food_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))

        # Unittests for each field of info under id = 424; should match the above
        self.assertEqual(resp['name'], 'Gerber')
        self.assertEqual(resp['group'], 'Baby Foods')
        self.assertEqual(resp['kcal'], '66')
        self.assertEqual(resp['prot'], '2')
        self.assertEqual(resp['fat'], '3')
        self.assertEqual(resp['carb'], '8')

    # Test for DELETE_KEY
    def test_food_delete_key(self):
        self.reset_data()
        
        # Specify a valid food to delete
        food_id = 600

        # Make a delete request and load response
        m = {}
        r = requests.delete(self.FOOD_URL + str(food_id), data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # Attempt to get that food_id
        # Response should be error because food_id not present after deletion
        r = requests.get(self.FOOD_URL + str(food_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')

if __name__ == "__main__":
    unittest.main()
