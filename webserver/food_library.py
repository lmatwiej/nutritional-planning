class _food_database:

        # Constructor -- creates multiple dictionaries for specific information
        # info is tied together by food_id
        def __init__(self):
                self.food_group = dict()
                self.food_name = dict()
                self.food_kcal = dict()
                self.food_protein = dict()
                self.food_fat = dict()
                self.food_carb = dict()

        # Load the food file
        def load_food(self, food_file):
                # Open the file
                f = open(food_file)

                # Iterate through the lines
                for line in f:

                        # Split line by delimiters
                        line = line.rstrip()
                        components = line.split("::")

                        # Assign each field to a variable
                        fid = int(components[0])
                        name = components[1]
                        group = components[2]
                        kcal = float(components[3])
                        prot = float(components[4])
                        fat = float(components[5])
                        carb = float(components[6])

                        # Add each variable to its respective dictionary
                        self.food_group[fid] = group
                        self.food_name[fid] = name
                        self.food_kcal[fid] = kcal
                        self.food_protein[fid] = prot
                        self.food_fat[fid] = fat
                        self.food_carb[fid] = carb

                f.close()

        # Simply return every fid in the dictionaries
        def get_foods(self):
                return self.food_name.keys()

        # Return info for a specific food id
        def get_food(self, fid):
                try:
                        # Access each field of data from the respective dictionaries by fid
                        group = self.food_group[fid]
                        name = self.food_name[fid]
                        kcal = self.food_kcal[fid]
                        prot = self.food_protein[fid]
                        fat = self.food_fat[fid]
                        carb = self.food_carb[fid]

                        # Aggregate the fields into a single list
                        food = list((name, group, kcal, prot, fat, carb))
                except Exception as ex:
                        food = None

                # Return the list
                return food

        # Update info under fid with the new info from a food iterable
        def set_food(self, fid, food):

                # Assignment using fid as key and accessing new values from food
                self.food_name[fid] = food[0]
                self.food_group[fid] = food[1]
                self.food_kcal[fid] = food[2]
                self.food_protein[fid] = food[3]
                self.food_fat[fid] = food[4]
                self.food_carb[fid] = food[5]

        # Delete fid from dictionaries
        def delete_food(self, fid):

                # Simple python del function to delete entry from each dict
                del(self.food_name[fid])
                del(self.food_group[fid])
                del(self.food_kcal[fid])
                del(self.food_protein[fid])
                del(self.food_fat[fid])
                del(self.food_carb[fid])

if __name__ == "__main__":
       mdb = _food_database()

       #### MOVIES ########
       mdb.load_food('food_data.dat')

       food = mdb.get_food(4034)
       print(food[0])

       food[0] = 'ABC'
       mdb.set_food(1002, food)

       food = mdb.get_food(1002)
       print(food[0])
       ####################
