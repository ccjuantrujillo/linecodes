from bottle import route,run

@route('/')
def index():
    return "<p>Hellow World</p>"
run(host="localhost",port="8080",debug=True)