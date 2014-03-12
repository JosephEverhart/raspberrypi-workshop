from flask import Flask
from flask import request
from subprocess import Popen,PIPE
app = Flask(__name__)

from functools import wraps
from flask import request, Response

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == '1234'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/",methods=['GET', 'POST'])
@requires_auth
def switch():
    move = str(request.args.get('switch'))
    if move == "on":
        print "on"
    elif move == "off":
        print "off"
    return "moved:" + move

@app.route("/uptime")
def uptime():
    temp_command = "uptime"
    return  str(Popen([temp_command], stdout=PIPE).communicate()[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)