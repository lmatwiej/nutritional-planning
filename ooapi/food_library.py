class _food_database:

       def __init__(self):
        self.food_group = dict()
        self.food_name = dict()
        self.food_kcal = dict()
        self.food_protein = dict()
        self.food_fat = dict()
        self.food_carb = dict()

       def load_food(self, food_file):
        f = open(food_file)
        for line in f:
                line = line.rstrip()
                components = line.split("::")
                fid = int(components[0])
                name = components[1]
                group = components[2]
                kcal = float(components[3])
                prot = float(components[4])
                fat = float(components[5])
                carb = float(components[6])
                self.food_group[fid] = group
                self.food_name[fid] = name
                self.food_kcal[fid] = kcal
                self.food_protein[fid] = prot
                self.food_fat[fid] = fat
                self.food_carb[fid] = carb
        f.close()

       def get_foods(self):
        return self.food_name.keys()

       def get_food(self, fid):
        try:
                group = self.food_group[fid]
                name = self.food_name[fid]
                kcal = self.food_kcal[fid]
                prot = self.food_protein[fid]
                fat = self.food_fat[fid]
                carb = self.food_carb[fid]
                food = list((name, group, kcal, prot, fat, carb))
        except Exception as ex:
                food = None
        return food

       def set_food(self, fid, food):
        self.food_name[fid] = food[0]
        self.food_group[fid] = food[1]
        self.food_kcal[fid] = food[2]
        self.food_protein[fid] = food[3]
        self.food_fat[fid] = food[4]
        self.food_carb[fid] = food[5]

       def delete_food(self, fid):
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
