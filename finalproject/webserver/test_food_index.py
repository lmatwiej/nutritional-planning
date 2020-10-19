import unittest
import requests
import json

class TestFoodIndex(unittest.TestCase):

    SITE_URL = 'http://student10.cse.nd.edu:51077' # replace with your assigned port id
    print("Testing for server: " + SITE_URL)
    FOOD_URL = SITE_URL + '/food_name/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_food_index_get(self):
        self.reset_data()
        r = requests.get(self.FOOD_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        testfood = {}
        foods = resp['food']
        for food in foods:
            if food['id'] == 1020:
                testfood = food

        self.assertEqual(testfood['name'], 'Cheese, fontina')
        self.assertEqual(testfood['group'], 'Dairy and Egg Products')
        self.assertEqual(testfood['kcal'], 389.0)
        self.assertEqual(testfood['protein'], 25.6)
        self.assertEqual(testfood['fat'], 31.14)
        self.assertEqual(testfood['carb'], 1.55)

    def test_food_index_post(self):
        self.reset_data()

        m = {}
        m['name'] = 'Gerber'
        m['group'] = 'Baby Foods'
        m['kcal'] = '66'
        m['prot'] = '2'
        m['fat'] = '3'
        m['carb'] = '8'
        r = requests.post(self.FOOD_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['id'], 93601)

        r = requests.get(self.FOOD_URL + str(resp['id']))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['name'], m['name'])
        self.assertEqual(resp['group'], m['group'])
        self.assertEqual(resp['kcal'], m['kcal'])
        self.assertEqual(resp['prot'], m['prot'])
        self.assertEqual(resp['fat'], m['fat'])
        self.assertEqual(resp['carb'], m['carb'])

    def test_food_index_delete(self):
        self.reset_data()

        m = {}
        r = requests.delete(self.FOOD_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.FOOD_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        food = resp['food']
        self.assertFalse(food)

if __name__ == "__main__":
    unittest.main()
