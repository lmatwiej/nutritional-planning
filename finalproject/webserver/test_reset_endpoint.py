import unittest
import requests
import json

class TestReset(unittest.TestCase):

    SITE_URL = 'http://student10.cse.nd.edu:51077' # replace with your port id
    print("Testing for server: " + SITE_URL)
    RESET_URL = SITE_URL + '/reset/'
    FOOD_URL = SITE_URL + '/food_name/'

    def test_put_reset_index(self):
        m = {}
        r = requests.delete(self.FOOD_URL, data = json.dumps(m))
        r = requests.put(self.RESET_URL)

        resp = json.loads(r.content.decode('utf-8'))

        self.assertEqual(resp['result'], 'success')
        r = requests.get(self.FOOD_URL)
        resp = json.loads(r.content.decode('utf-8'))

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

    def test_put_reset_key(self):

        food_id = 1020
        m = {}
        r = requests.delete(self.FOOD_URL + str(food_id), data = json.dumps(m))
        r = requests.put(self.RESET_URL + str(food_id))

        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.FOOD_URL + str(food_id))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'Cheese, fontina')
        self.assertEqual(resp['group'], 'Dairy and Egg Products')
        self.assertEqual(resp['kcal'], 389.0)
        self.assertEqual(resp['prot'], 25.6)
        self.assertEqual(resp['fat'], 31.14)
        self.assertEqual(resp['carb'], 1.55)

if __name__ == "__main__":
    unittest.main()
