import unittest
import requests
import json

class TestFood(unittest.TestCase):

    SITE_URL = 'http://student10.cse.nd.edu:51077' # replace with your port number and
    print("testing for server: " + SITE_URL)
    FOOD_URL = SITE_URL + '/food_name/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, data = json.dumps(m))


    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_food_get_key(self):
        self.reset_data()
        food_id = 1003
        r = requests.get(self.FOOD_URL + str(food_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'Butter oil, anhydrous')
        self.assertEqual(resp['group'], 'Dairy and Egg Products')
        self.assertEqual(resp['kcal'], 876.0)
        self.assertEqual(resp['prot'], 0.28)
        self.assertEqual(resp['fat'], 99.48)
        self.assertEqual(resp['carb'], 0)

    def test_food_put_key(self):
        self.reset_data()
        food_id = 1004

        r = requests.get(self.FOOD_URL + str(food_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'Cheese, blue')
        self.assertEqual(resp['group'], 'Dairy and Egg Products')
        self.assertEqual(resp['kcal'], 353.0)
        self.assertEqual(resp['prot'], 21.4)
        self.assertEqual(resp['fat'], 28.74)
        self.assertEqual(resp['carb'], 2.34)

        m = {}
        m['name'] = 'Gerber'
        m['group'] = 'Baby Foods'
        m['kcal'] = '66'
        m['prot'] = '2'
        m['fat'] = '3'
        m['carb'] = '8'
        r = requests.put(self.FOOD_URL + str(food_id), data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.FOOD_URL + str(food_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'Gerber')
        self.assertEqual(resp['group'], 'Baby Foods')
        self.assertEqual(resp['kcal'], '66')
        self.assertEqual(resp['prot'], '2')
        self.assertEqual(resp['fat'], '3')
        self.assertEqual(resp['carb'], '8')

    def test_food_delete_key(self):
        self.reset_data()
        food_id = 1008

        m = {}
        r = requests.delete(self.FOOD_URL + str(food_id), data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.FOOD_URL + str(food_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')

if __name__ == "__main__":
    unittest.main()
