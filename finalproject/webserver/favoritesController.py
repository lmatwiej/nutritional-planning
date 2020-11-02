import cherrypy
import re, json
from ../ooapi/favorites_library import _favorites_log

class favoritesController(object):

        def __init__(self, log=None):
            if log is None:
                self.log = _favorites_log()
            else:
                self.log = log

        def GET_INDEX(self):
		'''when GET request for /favorites comes in, then respond with json string of all favorites'''
            output = {'result':'success'}

            try:
                ratings = self.log.get_all_favs()
                if ratings is not None:
                    output["favorites"] = ratings
                else:
                    output["favorites"] = "No favorites"
            except Exception as ex:
                output['result'] = 'error'
                output['message'] = str(ex)

            return json.dumps(output)

        def GET_FILTERED(self, rating):
        '''when GET request for /favorites/rating comes in, then respond with json string of all favorites that meet the rating cutoff'''
            output = {'result:'success'}

            result = self.log.get_filtered_ratings(rating)

            if (not result):
                output['favorites']= 'No favorites match the criteria'
            else:
                output['favorites'] = result

            return json.dumps(output)

        def PUT_KEY(self, name, rating):
		'''when PUT request for /favorites/:name comes in, then we change the rating for that food'''
            output = {'result':'success'}
            data = json.loads(cherrypy.request.body.read().decode('utf-8'))
            rating = data['rating']
            if (self.log.update_rating(name, rating) == 1):
                output['result'] = 'failure: name not found'
            return json.dumps(output)

        def DELETE_INDEX(self, name):
		'''when DELETE for /favorites/name comes in, we remove just that favorite food from the log of ratings'''
            self.log.delete_favorite(name)

        def POST_INDEX(self):
		'''when POST for /favorites comes in, we take food name and rating from body of request, and respond with status'''
            data = json.loads(cherrypy.request.body.read().decode('utf-8'))
            name = data['key']
            rating = data['value']
            self.log.add_favorite(name, rating)

