import cherrypy
import re, json
from food_library import _food_database

class FoodController(object):

        def __init__(self, mdb=None):
                if mdb is None:
                        self.mdb = _food_database()
                else:
                        self.mdb = mdb

                self.mdb.load_food('food_data.dat')

        def GET_KEY(self, food_id):
		#'''when GET request for /movies/movie_id comes in, then we respond with json string'''
                output = {'result':'success'}
                food_id = int(food_id)


                try:
                        food = self.mdb.get_food(food_id)
                        if food is not None:
                                output['id'] = food_id
                                output['name'] = food[0]
                                output['group'] = food[1]
                                output['kcal'] = food[2]
                                output['prot'] = food[3]
                                output['fat'] = food[4]
                                output['carb'] = food[5]
                        else:
                                output['result'] = 'error'
                                output['message'] = 'food not found'
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)

        def PUT_KEY(self, food_id):
		#'''when PUT request for /movies/movie_id comes in, then we change that movie in the mdb'''
                output = {'result':'success'}
                food_id = int(food_id)

                data = json.loads(cherrypy.request.body.read().decode('utf-8'))

                food = list()
                food.append(data['name'])
                food.append(data['group'])
                food.append(data['kcal'])
                food.append(data['prot'])
                food.append(data['fat'])
                food.append(data['carb'])

                self.mdb.set_food(food_id, food)

                return json.dumps(output)

        def DELETE_KEY(self, food_id):
		#'''when GET request for /movies/movie_id comes in, then we respond with json string'''
                output = {'result':'success'}
                food_id = int(food_id)


                try:
                        food = self.mdb.get_food(food_id)
                        if food is not None:
                                self.mdb.delete_food(food_id)
                        else:
                                output['result'] = 'error'
                                output['message'] = 'food not found'
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)


        def GET_INDEX(self):
		#'''when GET request for /movies/ comes in, we respond with all the movie information in a json str'''
                output = {'result':'success'}
                output['food'] = []

                try:
                    for fid in self.mdb.get_food():
                        food = self.mdb.get_food(fid)
                        dfood = {'id':fid, 'name':food[0],'group':food[1],'kcal':food[2],'protein':food[3],'fat':food[4],'carb':food[5]}
                        output['food'].append(dfood)
                except Exception as ex:
                    output['result'] = 'error'
                    output['message'] = str(ex)

                return json.dumps(output)

        def POST_INDEX(self):
		#'''when POST for /movies/ comes in, we take title and genres from body of request, and respond with the new movie_id and more'''
                output = {'result':'success'}
                data = json.loads(cherrypy.request.body.read().decode('utf-8'))
                food = list()
                food.append(data['name'])
                food.append(data['group'])
                food.append(data['kcal'])
                food.append(data['protein'])
                food.append(data['carb'])
                food_id = 1
                for fid in self.mdb.get_food():
                    food_id = fid

                food_id = food_id + 1

                self.mdb.set_movie(food_id, food)
                if self.mdb.get_movie(food_id) is None:
                    output['result'] = 'error'
                    output['message'] = 'Food was not added'
                else:
                    output['id'] = food_id

                return json.dumps(output)

        def DELETE_INDEX(self):
            output = {'result':'success'}

            self.mdb.food_name.clear()
            if self.mdb.food_name:
                output['result'] = 'error'
                output['message'] = 'Unable to clear all names'
            self.mdb.food_group.clear()
            if self.mdb.food_group:
                output['result'] = 'error'
                output['message'] = 'Unable to clear all groups'
            self.mdb.food_kcal.clear()
            if self.mdb.food_kcal:
                output['result'] = 'error'
                output['message'] = 'Unable to clear all kcal'
            self.mdb.food_protein.clear()
            if self.mdb.food_protein:
                output['result'] = 'error'
                output['message'] = 'Unable to clear all proteins'
            self.mdb.food_fat.clear()
            if self.mdb.fat_group:
                output['result'] = 'error'
                output['message'] = 'Unable to clear all fat'
            self.mdb.food_carb.clear()
            if self.mdb.fat_carb:
                output['result'] = 'error'
                output['message'] = 'Unable to clear all carb'


            return json.dumps(output)
