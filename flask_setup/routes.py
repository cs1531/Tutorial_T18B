from server import app

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/login')
def myfunc():
    return '<h1>login page</h1>'
