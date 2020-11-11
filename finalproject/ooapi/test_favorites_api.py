import unittest
from favorites_library import _favorites_log

class TestFavoritesAPI(unittest.TestCase):

    # Initialize a favorites log
    fav = _favorites_log()

    # Helper function that resets the log in case undesired changes occurred
    def reset_log(self):
        self.fav.reset_favs()

    # Test if utility returns entire dictionary
    def test_get_all_favs(self):
        # Check if what's returned is equal to self.fav
        self.assertEqual(self.fav.favorites, self.fav.get_all_favs())

	# Test if utility will return the correct rating
    def test_get_fav(self):

		# First add a favorite to the log
        self.fav.favorites["Pierogi"] = 10

        # Try to get that favorite back
        return_rating = self.fav.get_fav("Pierogi")

		# Check if it worked
        self.assertEqual(return_rating, 10)

    # Test to see if all favs with minimum rating can be returned
    def test_get_filtered_ratings(self):
		# Add some names and ratings to fav after initializing it again
        self.reset_log()
        self.fav.favorites["Blueberry"] = 2
        self.fav.favorites["Raspberry"] = 3
        self.fav.favorites["Strawberry"] = 4
        self.fav.favorites["Blackberry"] = 5
        self.fav.favorites["Watermelon"] = 6
        self.fav.favorites["Orange"] = 7
        self.fav.favorites["Pineapple"] = 8
        self.fav.favorites["Lemon"] = 1
        self.fav.favorites["Canteloupe"] = 5
        self.fav.favorites["Coconut"] = 4

        # Create a 'cheat sheet'
        filtered = ["Watermelon", "Orange", "Pineapple"]

        # Retrieve ratings over 5
        returned = self.fav.get_filtered_ratings(6)

        # Check results
        for name in filtered:
            self.assertTrue(name in returned)
        self.assertTrue(len(filtered) == len(returned))
        
    # Test to see if a favorite can be added successfully
    def test_add_favorite(self):
        # Add a favorite to an empty fav
        self.reset_log()
        self.fav.add_favorite("pierogi", 10)

		# Check if the favorite is in the fav
        self.assertTrue("pierogi" in self.fav.get_all_favs())

    # Test to see if a rating can be successfully updated
    def test_add_favorite(self):

        # Add pierogi with rating 1
        self.reset_log()
        self.fav.add_favorite("pierogi", 1)

        # Update the rating to 10
        self.fav.update_rating("pierogi", 10)
        
        # Get the rating and check if it's set to 10
        rating = self.fav.get_fav("pierogi")
        self.assertEquals(rating, 10)

if __name__ == "__main__":
    unittest.main()
