import cherrypy
import re, json
from favorites_library import _favorites_log


class FavoritesController(object):

        def __init__(self, mdb=None):
                if mdb is None:
                        self.mdb = _favorites_log()
                else:
                        self.mdb = mdb

                self.mdb.load_favorites('favorites.dat')

        def GET_KEY(self, food_id):
		#'''when GET request for /favorites/food_id comes in, then we respond with json string'''
                output = {'result':'success'}
                food_id = int(food_id)

                try:
                        food = self.mdb.get_favorite(food_id)
                        if food is not None:
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
		#'''when PUT request for /favorites/food_id comes in, then we change that favorite'''
                output = {'result':'success'}
                food_id = int(food_id)

                data = json.loads(cherrypy.request.body.read().decode('utf-8'))

                food = list()
                food.append(data['name'])
                food.append(data['rating'])

                self.mdb.set_favorite(food_id, food)

                return json.dumps(output)

        def DELETE_KEY(self, food_id):
		#'''when GET request for /favorites/food_id comes in, then we delete that specific favorite'''
                output = {'result':'success'}
                food_id = int(food_id)

                try:
                        food = self.mdb.get_favorite(food_id)
                        if food is not None:
                                self.mdb.delete_favorite(food_id)
                        else:
                                output['result'] = 'error'
                                output['message'] = 'food not found'
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)


        def GET_INDEX(self):
		#'''when GET request for /favorites/ comes in, we respond with all the favorites and their ratings'''
                output = {'result':'success'}
                output['food'] = []

                try:
                    for fid in self.mdb.get_favorites():
                        food = self.mdb.get_favorite(fid)
                        dfood = {'id':fid, 'name':food[0],'rating':food[1]}
                        output['food'].append(dfood)
                except Exception as ex:
                    output['result'] = 'error'
                    output['message'] = str(ex)

                return json.dumps(output)

        def POST_INDEX(self):
		#'''when POST for /favorites/ comes in, we add the data to the favorites'''
                output = {'result':'success'}
                data = json.loads(cherrypy.request.body.read().decode('utf-8'))
                food = list()
                food_id = data['id']
                food.append(data['name'])
                food.append(data['rating'])

                self.mdb.set_favorite(food_id, food)
                if self.mdb.get_favorite(food_id) is None:
                    output['result'] = 'error'
                    output['message'] = 'Food was not added'
                else:
                    output['id'] = food_id

                return json.dumps(output)

        def DELETE_INDEX(self):
            #'''when DELETE for /favorites/ comes in, we delete all the favorites'''
            output = {'result':'success'}

            self.mdb.food_name.clear()
            if self.mdb.food_name:
                output['result'] = 'error'
                output['message'] = 'Unable to clear all names'
            self.mdb.food_rating.clear()
            if self.mdb.food_rating:
                output['result'] = 'error'
                output['message'] = 'Unable to clear all ratings'



            return json.dumps(output)
