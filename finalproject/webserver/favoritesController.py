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
		#'''when GET request for /movies/movie_id comes in, then we respond with json string'''
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
		#'''when PUT request for /movies/movie_id comes in, then we change that movie in the mdb'''
                output = {'result':'success'}
                food_id = int(food_id)

                data = json.loads(cherrypy.request.body.read().decode('utf-8'))

                food = list()
                food.append(data['name'])
                food.append(data['rating'])

                self.mdb.set_favorite(food_id, food)

                return json.dumps(output)

        def DELETE_KEY(self, food_id):
		#'''when GET request for /movies/movie_id comes in, then we respond with json string'''
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
		#'''when GET request for /movies/ comes in, we respond with all the movie information in a json str'''
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
		#'''when POST for /movies/ comes in, we take title and genres from body of request, and respond with the new movie_id and more'''
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
