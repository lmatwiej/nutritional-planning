import cherrypy
from foodController import FoodController
from resetController import ResetController
from favoritesController import FavoritesController
from food_library import _food_database
from favorites_library import _favorites_log
# Implement CORS security feature
class optionsController:
    def OPTIONS(self, *args, **kwargs):
        return ""

# Define CORS
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"

# Define what happens when service started
def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()


    fdb = _food_database()
    log = _favorites_log()

    foodController     = FoodController(fdb)
    resetController     = ResetController(fdb, log)
    favoritesController     = FavoritesController(log)

    # Connect endpoints to the foodController
    # JSON Specification in the README
    dispatcher.connect('food_name_get', '/food_name/:food_id', controller=foodController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('food_name_set', '/food_name/:food_id', controller=foodController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('food_name_delete', '/food_name/:food_id', controller=foodController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('food_index_get', '/food_name/', controller=foodController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('food_index_post', '/food_name/', controller=foodController, action = 'POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('food_index_delete', '/food_name/', controller=foodController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

    # Connect endpoints to the favoritesController
    # JSON Specification in the README
    dispatcher.connect('favorites_get', '/favorites/:food_id', controller=favoritesController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('favorites_set', '/favorites/:food_id', controller=favoritesController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('favorites_delete', '/favorites/:food_id', controller=favoritesController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('favorites_get', '/favorites/', controller=favoritesController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('favorites_post', '/favorites/', controller=favoritesController, action = 'POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('favorites_delete', '/favorites/', controller=favoritesController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

    # Connect endpoints to the resetController
    # JSON Specification in the README
    dispatcher.connect('reset_put', '/reset/:food_id', controller=resetController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('reset_index_put', '/reset/', controller=resetController, action = 'PUT_INDEX', conditions=dict(method=['PUT']))

    # CORS related options connections
    dispatcher.connect('food_key_options', '/food_name/:food_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('food_options', '/food_name/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('food_key_options', '/reset/:food_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('food_options', '/reset/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('food_options', '/favorites/:food_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))


    conf = {
	'global': {
        'server.thread_pool': 5, # optional argument
	    'server.socket_host': '127.0.0.1', # Input host here
	    'server.socket_port': 7777, # Input port here
	    },
	'/': {
	    'request.dispatch': dispatcher,
        'tools.CORS.on':True,
	    }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# end of start_service


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
