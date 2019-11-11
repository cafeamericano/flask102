import flask
import os

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Hello World</h1><p>Sent to you by a server running Flask.</p>"

@app.route('/json', methods=['GET'])
def makeJSON():
    return flask.jsonify(name='Matthew', favoriteColor='Orage')

@app.route('/htmlfile', methods=['GET'])
def sendHTMLFile():
    return flask.current_app.send_static_file('index.html')

@app.route('/pngfile', methods=['GET'])
def sendPNGFile():
    return flask.current_app.send_static_file('catnose.png')

# Below pulled from https://stackoverflow.com/questions/17260338/deploying-flask-with-heroku
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
