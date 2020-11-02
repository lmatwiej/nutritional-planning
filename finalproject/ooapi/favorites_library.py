class _favorites_log:

        # Constructor
        def __init__(self):
            self.favorites = dict()

        # Reset the list of favorites
        def reset_favs(self):
            self.favorites.clear()

        # Return all the favorites
        def get_all_favs(self):
            return self.favorites

        # Return a specific favorite
        def get_fav(self, name):
            if name in self.favorites:
                return self.favorites[name]
            else:
                return None

        # Return all favorites with at least a certain rating
        def get_filtered_ratings(self, rating):
            filtered_favs = dict()
            for key, value in self.favorites.items():
                if (value >= rating):
                    filtered_favs[key] = value
            return filtered_favs

        def add_favorite(self, name, rating):
            self.favorites[name] = rating


        def delete_favorite(self, name):
            del(self.favorites[name])

if __name__ == "__main__":
       fav = _favorites_log()

