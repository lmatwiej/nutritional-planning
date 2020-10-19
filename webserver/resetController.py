import cherrypy
import re, json
from food_library import _food_database

class ResetController(object):

    def __init__(self, mdb=None):
        if mdb is None:
            self.mdb = _food_database()
        else:
            self.mdb = mdb


    def PUT_INDEX(self):
	#'''when PUT request comes in to /reset/ endpoint, then the movie database is reloaded'''
        output = {'result':'success'}

        # data = json.loads(cherrypy.request.body.read().decode())

        self.mdb.__init__()
        self.mdb.load_food('food_data.dat')

        return json.dumps(output)

    def PUT_KEY(self, food_id):
	#'''when PUT request comes in for /reset/movie_id endpoint, then that movie is reloaded and updated in mdb'''
        output = {'result':'success'}
        fid = int(food_id)

        try:
            # data = json.loads(cherrypy.request.body.read().decode())

            mdbtmp = _food_database()
            mdbtmp.load_food('food_data.dat')

            food = mdbtmp.get_food(fid)

            self.mdb.set_food(fid, food) #TODO remember to reset genre also


        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
