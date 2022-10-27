
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route


@route('/')
def hello_world():
    return 'Hello from nihash'

@route('/hi')
def hi_world():
    return 'Hi from nihash'

@route('/bye')
def bye_world():
    return 'bye from nihash'

application = default_app()

