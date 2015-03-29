__author__ = 'Stuart'
import bottle
import pymongo

# this is the handler for the default path of the web server

# @bottle.route('/')
# def index():  # nothing special about this name, and can in fact call it something else
#
#     # connect to mongoDB
#     connection = pymongo.MongoClient('localhost',27017)  # 27017 is default port mongod listens on
#     # attach to test db
#     db = connection.test
#     # get handle for names collection
#     name = db.names
#     # find a single document
#     item = name.find_one()
#
#     return '<b>Hello {}!</b>'.format(item['name'])

@bottle.route('/')
def home_page():
    mythings = ["apple","orange","banana","peach"]
    #return bottle.template('hello_world', username = "Stu", things = mythings)  #hello_world.tpl
    return bottle.template('hello_world', {'username':'stu',# can use dict too, since python always sends var as dict
                                           'things': mythings})

@bottle.route('/testpage')
def test_page():
    return "this is a test page"

@bottle.route('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get('fruit')
    if (fruit == None or fruit == ""):
        fruit="No Fruit Selected"
    return bottle.template('fruit_selection_tool', {'fruit': fruit})


bottle.debug(True)  # this way we don't need to restart the server every time we make a change to views
bottle.run(host='localhost',port=8082)