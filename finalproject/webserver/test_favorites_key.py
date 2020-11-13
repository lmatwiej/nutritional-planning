import unittest
import requests
import json

class TestFavoritesKey(unittest.TestCase):

    # Initialize endpoints to be used
    SITE_URL = 'http://student10.cse.nd.edu:51077' # replace with your port number and
    print("testing for server: " + SITE_URL)
    FAVORITES_URL = SITE_URL + '/favorites/'
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

        # Initialize food id and url endpoint: go for tea and 10 (id = 2)
        food_id = 2
        r = requests.get(self.FAVORITES_URL + str(food_id))

        # Test if response is valid JSON 
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))

        # Test if the correct food information returned (under id = 2)
        self.assertEqual(resp['name'], 'Tea')
        self.assertEqual(resp['rating'], 10)

    # Test PUT_KEY
    def test_food_put_key(self):
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

        # Attempt to modify id = 2, which contains rating for tea

        # Define info for a new food entry
        m = {}
        m['name'] = 'Tea'
        m['rating'] = 5

        # Issue put request to id = 2 endpoint with the new information

        r = requests.put(self.FAVORITES_URL + "2", data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # See if put request worked: if new data is now present at id = 2
        r = requests.get(self.FAVORITES_URL + "2")
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))

        # Unittests for each field of info under id = 24; should have rating 5
        self.assertEqual(resp['name'], 'Tea')
        self.assertEqual(resp['rating'], 2)

    # Test for DELETE_KEY
    def test_food_delete_key(self):
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
        
        # Specify a valid favorite to delete
        food_id = 2

        # Make a delete request and load response
        m = {}
        r = requests.delete(self.FAVORITES_URL + str(food_id), data = json.dumps(m)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # Attempt to get that food_id
        # Response should be error because food_id not present after deletion
        r = requests.get(self.FAVORITES_URL + str(food_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')

if __name__ == "__main__":
    unittest.main()
