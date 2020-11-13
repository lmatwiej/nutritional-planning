class _favorites_log:

        # Constructor -- creates rating and name dictionaries
        def __init__(self):
                self.food_rating = dict()
                self.food_name = dict()

        # Load in 'favorites.dat' that has predefined favorites
        def load_favorites(self, food_file):
                f = open(food_file)
                for line in f:
                        
                        # Split line by delimiters
                        line = line.rstrip()
                        components = line.split("::")

                        # Assign each field to a variable
                        fid = int(components[0])
                        name = components[1]
                        rating = components[2]
                        
                        # Add each variable to its respective dictionary
                        self.food_rating[fid] = rating
                        self.food_name[fid] = name

                f.close()

        # Return every fid in favorites
        def get_favorites(self):
                return self.food_name.keys()

        # Get the rating for a specific favorite using fid
        def get_favorite(self, fid):
                try:
                        # Retrieve rating under fid
                        rating = self.food_rating[fid]
                        name = self.food_name[fid]

                        # List of the name and rating pair
                        food = list((name, rating))
                except Exception as ex:
                        food = None

                # Return name, rating pair
                return food

        # Update a favorite name, rating pair under the fid
        def set_favorite(self, fid, food):

                # Update the name
                self.food_name[fid] = food[0]

                # Update the rating
                self.food_rating[fid] = food[1]

        # Delete a favorite
        def delete_favorite(self, fid):

                # Delete from the names
                del(self.food_name[fid])

                # Delete from the ratings
                del(self.food_rating[fid])

if __name__ == "__main__":
       fav = _favorites_log()
