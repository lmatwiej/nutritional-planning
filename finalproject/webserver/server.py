import cherrypy
from foodController import FoodController
from resetController import ResetController
from favoritesController import FavoritesController
from food_library import _food_database
from favorites_library import _favorites_log


class optionsController:
    def OPTIONS(self, *args, **kwargs):
        return ""

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()


    mdb = _food_database()
    mdd = _favorites_log()

    foodController     = FoodController(mdb=mdb)
    resetController     = ResetController(mdb=mdb)
    favoritesController     = FavoritesController(mdb=mdd)
    ## dataController     = DataController(mdb=mdb)


    ## dispatcher.connect('favorites_put', '/favorites/:key', controller=favoriteController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    ## dispatcher.connect('favorites_get', '/favorites/:key', controller=favoriteController, action = 'GET_KEY', conditions=dict(method=['GET']))
    ## dispatcher.connect('favorites_delete', '/favorites/:key', controller=favoritesController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))

    dispatcher.connect('food_name_get', '/food_name/:food_id', controller=foodController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('food_name_set', '/food_name/:food_id', controller=foodController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('food_name_delete', '/food_name/:food_id', controller=foodController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('food_index_get', '/food_name/', controller=foodController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('food_index_post', '/food_name/', controller=foodController, action = 'POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('food_index_delete', '/food_name/', controller=foodController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

    dispatcher.connect('favorites_get', '/favorites/:food_id', controller=favoritesController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('favorites_set', '/favorites/:food_id', controller=favoritesController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('favorites_delete', '/favorites/:food_id', controller=favoritesController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('favorites_get', '/favorites/', controller=favoritesController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('favorites_post', '/favorites/', controller=favoritesController, action = 'POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('favorites_delete', '/favorites/', controller=favoritesController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

    dispatcher.connect('reset_put', '/reset/:food_id', controller=resetController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('reset_index_put', '/reset/', controller=resetController, action = 'PUT_INDEX', conditions=dict(method=['PUT']))

    ## dispatcher.connect('data_get', '/data', controller=dataController, action = 'GET_KEY', conditions=dict(method=['GET']))

    # CORS related options connections
    dispatcher.connect('food_key_options', '/food_name/:food_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('food_options', '/food_name/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('food_key_options', '/reset/:food_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('food_options', '/reset/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('food_options', '/favorites/:food_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))


    conf = {
	'global': {
        'server.thread_pool': 5, # optional argument
	    'server.socket_host': 'student10.cse.nd.edu', #
	    'server.socket_port': 51077, #change port number to your assigned
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
