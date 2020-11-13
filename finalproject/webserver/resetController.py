import cherrypy
import re, json
from food_library import _food_database

class ResetController(object):

    # Initialize the database in the constructor
    def __init__(self, mdb=None):
        if mdb is None:
            self.mdb = _food_database()
        else:
            self.mdb = mdb

    def PUT_INDEX(self):
	# when PUT request comes in to /reset/ endpoint, then the movie database is reloaded'''
        output = {'result':'success'}

        # data = json.loads(cherrypy.request.body.read().decode())

        self.mdb.__init__()
        self.mdb.load_food('food_data.dat')

        return json.dumps(output)

    def PUT_KEY(self, food_id):
	 # when PUT request comes in for /reset/food_id endpoint, then that food_id is reloaded and updated in mdb'''
        output = {'result':'success'}
        fid = int(food_id)

        try:

            # In order to only reset one food, need to initialize a new database
            # Retrieve the food_id from that new database
            mdbtmp = _food_database()
            mdbtmp.load_food('food_data.dat')

            # Retrieve the food_id from that new database
            food = mdbtmp.get_food(fid)

            # Set the food in actual database with what was retrieved from original
            self.mdb.set_food(fid, food)

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
