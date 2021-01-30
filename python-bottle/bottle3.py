from bottle import Bottle,route,run,request

@route('/login')
def login():
    return '''
            <form action="/login" method="post">
            Username: <input type="text" name="username">
            Password: <input type="password" name="password">
            <input type="submit" value="Login">
            </form>
            '''

@route('/login',method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username=="admin" and password=="123456":
        return "<p>Tu logueo fue exitoso</p>"
    else:
        return "<p>Tu Login fallo</p>"

run(host="localhost",port=8080)

