import cherrypy
import re, json
from favorites_library import _favorites_log


class FavoritesController(object):

        # Constructor - initialize a favorites log with API
        def __init__(self, mdb=None):
                if mdb is None:
                        self.mdb = _favorites_log()
                else:
                        self.mdb = mdb

                # Load predefined favorites with API function
                self.mdb.load_favorites('favorites.dat')


        def GET_KEY(self, food_id):
		#'''when GET request for /favorites/food_id comes in, then we respond with json string'''
                output = {'result':'success'}
                food_id = int(food_id)

                try:
                        # Utilize API function to get food under the endpoint food_id
                        food = self.mdb.get_favorite(food_id)

                        # If food_id is not in database, food will be None
                        if food is not None:

                                # Populate the output with name rating data
                                output['id'] = food_id
                                output['name'] = food[0]
                                output['rating'] = food[1]
                        else:
                                output['result'] = 'error'
                                output['message'] = 'food not found'
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)

        def PUT_KEY(self, food_id):
		#'''when PUT request for /favorites/food_id comes in, then we change that movie in the mdb'''
                output = {'result':'success'}
                food_id = int(food_id)

                # Load message body with new data
                data = json.loads(cherrypy.request.body.read().decode('utf-8'))

                # Populate a list with the name and rating from data
                food = list()
                food.append(data['name'])
                food.append(data['rating'])

                # Utilize API Function to update that the food id with new data
                self.mdb.set_favorite(food_id, food)
                return json.dumps(output)

        def DELETE_KEY(self, food_id):
		#'''when DELETE request for /favorites/food_id comes in, then we delete that favorite'''
                output = {'result':'success'}
                food_id = int(food_id)

                try:
                        # First try to get the food_id
                        food = self.mdb.get_favorite(food_id)

                        # If food not None, food_id is present can be deleted
                        if food is not None:

                                # Proceed to delete
                                self.mdb.delete_favorite(food_id)
                        else:
                                output['result'] = 'error'
                                output['message'] = 'food not found'
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)


        def GET_INDEX(self):
		#'''when GET request for /favorites/ comes in, we respond with all the favorites information in a json str'''
                output = {'result':'success'}
                output['food'] = []

                try:
                         # Use API to retrieve all the food ids
                        for fid in self.mdb.get_favorites():
                                # Use each food id to get that food's specific information
                                food = self.mdb.get_favorite(fid)

                                # Create dictionary with the information
                                # Append it to output
                                dfood = {'id':fid, 'name':food[0],'rating':food[1]}
                                output['food'].append(dfood)

                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)

        def POST_INDEX(self):
		#'''when POST for /favorites/ comes in, we take a new name, rating pair and add it to the log of favs'''
                output = {'result':'success'}

                # Load the data from request
                data = json.loads(cherrypy.request.body.read().decode('utf-8'))

                # Construct list of food info from request body
                food = list()
                food.append(data['name'])
                food.append(data['rating'])

                # Iterate through id's to set food_id as the highest
                food_id = 1
                for fid in self.mdb.get_favorites():
                        food_id = fid
                food_id = food_id + 1

                # Utilize API function set_food to add the entry
                self.mdb.set_favorite(food_id, food)
                if self.mdb.get_favorite(food_id) is None:
                        output['result'] = 'error'
                        output['message'] = 'Food was not added'
                else:
                        output['id'] = food_id

                return json.dumps(output)

        def DELETE_INDEX(self):
                #'''when DELETE request for /favorites/ comes in, we delete all the favorites from the log'''
                output = {'result':'success'}

                # Clear each dictioary in the database and check if clear
                # If not cleared, set output result to error
                self.mdb.food_name.clear()
                if self.mdb.food_name:
                        output['result'] = 'error'
                        output['message'] = 'Unable to clear all names'
                        
                self.mdb.food_rating.clear()
                if self.mdb.food_rating:
                        output['result'] = 'error'
                        output['message'] = 'Unable to clear all ratings'



            return json.dumps(output)
