import unittest
from favorites_library import _favorites_log

class TestFavoritesAPI(unittest.TestCase):

    # Load the data & initialize any dictionaries necessary to test the API
    log = _food_log()
    log.load_favorites('favorites.dat')

    # Helper Function That Reloads fdb in case changes occurred
    def reload_log(self):
        self.log = _favorites_log() # Call constructor again to wipe clean all changes
        self.log.load_favorites('favorites.dat')

        # Initialize to have two favorites
        self.food_name["1"] = "Tea"
        self.food_rating["1"] = 10

        self.food_name["2"] = "Honey"
        self.food_rating["2"] = 8

    # Test if the get_foods utility successfully loads every food name
    def test_get_favorites(self):
        # Check if length of the returned list equals the length of fdb.food_name
        # Otherwise, checking each name in list and log.food_name would bloat the output
        self.assertEqual(len(self.log.get_favorites()), len(self.log.food_name))

    def test_get_favorite(self):
        self.reload_log()

        # Check if it correctly retrieves tea rated at 10
        food = self.log.get_favorite(1) 
        self.assertEqual(food[0], "Tea")
        self.assertEqual(food[1], 10)

    # Test to see if a food can be added successfully
    def test_set_favorite(self):
        # Call reload to clean changes for the test
        self.reload_log()

        # Create a new food and set it with the highest fid incremented
        new_food = list(("Milk", 7))
        new_fid = len(self.log.food_name) + 1
        self.log.set_food(new_fid, new_food)
        
        # Check if the newly added food can be retrieved
        food = self.log.get_favorite(new_fid)
        self.assertEqual(food[0], "Milk")
        self.assertEqual(food[1], 7)

    # Test to see if a food can be added successfully
    def test_delete_favorite(self):
        # Call reload to clean changes for the test
        self.reload_log()
        
        # Delete Honey
        self.log.delete_food(2)

        # Check if the entry is still there after being deleted
        self.assertFalse(2 in self.log.food_name)

if __name__ == "__main__":
    unittest.main()
