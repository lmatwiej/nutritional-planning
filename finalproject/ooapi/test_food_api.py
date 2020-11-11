import unittest

class TestFoodAPI(unittest.TestCase):

    # Load the data & initialize any dictionaries necessary to test the API
    def __init__(self):
        self.fdb = _food_database()
        self.fdb.load_food('food_data.dat')

    # Helper Function That Reloads fdb in case changes occurred
    def reload_fdb(self):
        self.fdb = _food_database() # Call constructor again to wipe clean all changes
        self.fdb.load_food('food_data.dat')

    # Test if the get_foods utility successfully loads every food name
    def test_get_foods(self):
        # Check if length of the returned list equals the length of fdb.food_name
        # Otherwise, checking each name in list and fdb.food_name would bloat the output
        self.assertEqual(self.fdb.get_foods().len(), len(fdb.food_name))

    def test_get_food(self):

        # Randomly select foods to get after manually checking the data
        food = self.fdb.get_food(120) # Sunflower Oil
        self.assertEqual(food[0].lower(), "sunflower oil")
        self.assertEqual(food[1].lower(), "fats and oils")
        self.assertEqual(food[2], 884)
        self.assertEqual(food[3], 0)
        self.assertEqual(food[4], 100)
        self.assertEqual(food[5], 0)

        # Previous unittests checked every element of the food list
        # This next test only checks the name because it only intends to ensure consistent results
        food = self.fdb.get_food(362) # Garlic
        self.assertEqual(food[0].lower(), "garlic")

    # Test to see if a food can be added successfully
    def test_set_food(self):
        # Call reload to clean changes for the test
        self.reload_fdb()

        # Create a new food and set it with the highest fid incremented
        new_food = list(("Pierogi", "Polish Delicacy", 300,10,10,20))
        new_fid = self.fdb.food_name.len() + 1
        self.fdb.set_food(new_fid, new_food)
        
        # Check if the newly added food can be retrieved
        food = self.fdb.get_food(new_fid)
        self.assertEqual(food[0].lower(), "pierogi")
        self.assertEqual(food[1].lower(), "polish delicacy")
        self.assertEqual(food[2], 300)
        self.assertEqual(food[3], 10)
        self.assertEqual(food[4], 10)
        self.assertEqual(food[5], 20)

    # Test to see if a food can be added successfully
    def test_delete_food(self):
        # Call reload to clean changes for the test
        self.reload_fdb()

        # Create a new food and set it with the highest fid incremented
        new_food = list(("Pierogi", "Polish Delicacy", 300,10,10,20))
        new_fid = fdb.food_name.len() + 1
        self.fdb.set_food(new_fid, new_food)
        
        # Delete the newly added entry
        self.fdb.delete_food(new_fid)

        # Check if the entry is still there after being deleted
        self.assertFalse(new_fid in self.fdb.food_name)

if __name__ == "__main__":
    unittest.main()
