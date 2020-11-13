import cherrypy
import re, json
from food_library import _food_database

class FoodController(object):

        # Initialize by calling the API constructor and defining a self.fdb database
        def __init__(self, mdb=None):
                if mdb is None:
                        self.mdb = _food_database()
                else:
                        self.mdb = mdb

                # Load the data
                self.mdb.load_food('food_data.dat')

        def GET_KEY(self, food_id):
		'''when GET request for /food_name/food_id comes in, then we respond with json string'''
                output = {'result':'success'}

                food_id = int(food_id)
                try:
                        # Utilize API function to get food under the endpoint food_id
                        food = self.mdb.get_food(food_id)

                        # If food_id is not in database, food will be None
                        if food is not None:
                                # Populate the output with new data
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
		'''when PUT request for /food_name/food_id comes in, then we change that food entry according to message body'''
                output = {'result':'success'}

                # Load the data and initialize the food_id
                food_id = int(food_id)
                data = json.loads(cherrypy.request.body.read().decode('utf-8'))

                # Create list with request body data
                food = list()
                food.append(data['name'])
                food.append(data['group'])
                food.append(data['kcal'])
                food.append(data['prot'])
                food.append(data['fat'])
                food.append(data['carb'])

                # Call set_food API to update the information at id = food_id
                self.mdb.set_food(food_id, food)
                return json.dumps(output)

        def DELETE_KEY(self, food_id):
		'''when DELETE request for /food_name/food_id comes in, then we remove that food_id from database'''
                output = {'result':'success'}
                food_id = int(food_id)

                try:
                        # First try to get the food_id
                        food = self.mdb.get_food(food_id)

                        # If food not None, food_id is present can be deleted
                        if food is not None:

                                # Proceed to delete
                                self.mdb.delete_food(food_id)
                        # Any errors
                        else:
                                output['result'] = 'error'
                                output['message'] = 'food not found'
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)


        def GET_INDEX(self):
		'''when GET request for /food_name/ comes in, we respond with all the food information in a json str'''

                output = {'result':'success'}
                output['food'] = []

                try:
                        # Use get_foods() to retrieve all the food ids
                        for fid in self.mdb.get_foods():
                                # Use each food id to get that food's specific information
                                food = self.mdb.get_food(fid)

                                # Create dictionary with the information
                                # Append it to output
                                dfood = {'id':fid, 'name':food[0],'group':food[1],'kcal':food[2],'protein':food[3],'fat':food[4],'carb':food[5]}
                                output['food'].append(dfood)
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)

        def POST_INDEX(self):
		'''when POST for /food_name comes in, we take request body with new food information and add it to the database'''
                output = {'result':'success'}

                # Load the data from request
                data = json.loads(cherrypy.request.body.read().decode('utf-8'))

                # Construct list of food info from request body
                food = list()
                food.append(data['name'])
                food.append(data['group'])
                food.append(data['kcal'])
                food.append(data['prot'])
                food.append(data['fat'])
                food.append(data['carb'])

                # Iterate through id's to set food_id as the highest
                food_id = 1
                for fid in self.mdb.get_foods():
                    food_id = fid
                food_id = food_id + 1

                # Utilize API function set_food to add the entry
                self.mdb.set_food(food_id, food)
                if self.mdb.get_food(food_id) is None:
                    output['result'] = 'error'
                    output['message'] = 'Food was not added'
                else:
                    output['id'] = food_id

                return json.dumps(output)

        def DELETE_INDEX(self):
                '''when DELETE for /food_name/ comes in, we clear every entry from the database'''
                output = {'result':'success'}

                # Clear each dictioary in the database and check if clear
                # If not cleared, set output result to error
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
                if self.mdb.food_fat:
                        output['result'] = 'error'
                        output['message'] = 'Unable to clear all fat'

                self.mdb.food_carb.clear()
                if self.mdb.food_carb:
                        output['result'] = 'error'
                        output['message'] = 'Unable to clear all carb'


                return json.dumps(output)
