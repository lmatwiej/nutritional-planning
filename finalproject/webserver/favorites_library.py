class _favorites_log:

        def __init__(self):
         self.food_rating = dict()
         self.food_name = dict()


        def load_favorites(self, food_file):
            f = open(food_file)
            for line in f:
                line = line.rstrip()
                components = line.split("::")
                fid = int(components[0])
                name = components[1]
                rating = components[2]
                self.food_rating[fid] = rating
                self.food_name[fid] = name
            f.close()

        def get_favorites(self):
         return self.food_name.keys()

        def get_favorite(self, fid):
         try:
                 rating = self.food_rating[fid]
                 name = self.food_name[fid]
                 food = list((name, rating))
         except Exception as ex:
                 food = None
         return food

        def set_favorite(self, fid, food):
         self.food_name[fid] = food[0]
         self.food_rating[fid] = food[1]

        def delete_favorite(self, fid):
         del(self.food_name[fid])
         del(self.food_rating[fid])

if __name__ == "__main__":
       fav = _favorites_log()
