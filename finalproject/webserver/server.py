import cherrypy
from foodController import FoodController
## from favoritesController import FavoritesController
## from dataController import DataController
from food_library import _food_database


def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()


    mdb = _food_database()

    foodController     = FoodController(mdb=mdb)
    resetController     = ResetController(mdb=mdb)
    ## favoritesController     = FavoritesController(mdb=mdb)
    ## dataController     = DataController(mdb=mdb)


    ## dispatcher.connect('favorites_put', '/favorites/:key', controller=favoriteController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    ## dispatcher.connect('favorites_post', '/favorites', controller=favoriteController, action = 'POST_KEY', conditions=dict(method=['POST']))
    ## dispatcher.connect('favorites_get', '/favorites', controller=favoriteController, action = 'GET_KEY', conditions=dict(method=['GET']))
    ## dispatcher.connect('favorites_delete', '/favorites/:key', controller=favoritesController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))

    dispatcher.connect('food_name_get', '/food_name/:food_id', controller=foodController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('food_name_set', '/food_name/:food_id', controller=foodController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('food_name_delete', '/food_name', controller=foodController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('food_index_get', '/food_name/', controller=foodController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('food_index_post', '/food_name/', controller=foodController, action = 'POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('food_index_delete', '/food_name/', controller=foodController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

    dispatcher.connect('reset_put', '/reset/:food_id', controller=resetController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('reset_index_put', '/reset/', controller=resetController, action = 'PUT_INDEX', conditions=dict(method=['PUT']))

    ## dispatcher.connect('data_get', '/data', controller=dataController, action = 'GET_KEY', conditions=dict(method=['GET']))


    conf = {
	'global': {
        'server.thread_pool': 5, # optional argument
	    'server.socket_host': 'student10.cse.nd.edu', #
	    'server.socket_port': 51077, #change port number to your assigned
	    },
	'/': {
	    'request.dispatch': dispatcher,
	    }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# end of start_service


if __name__ == '__main__':
    start_service()