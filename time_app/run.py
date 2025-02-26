from flask import Flask
from datetime import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    time = datetime.now()
    return time.strftime("%H:%M:%S")


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
