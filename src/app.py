from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)


@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, little human ! ❤️❤️',
        'deployed_on': 'kubernetes'
        'app_name' : 'python-app', 
        'env_name' : 'dev'
    })

@app.route('/api/v1/healthz')
def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

@app.route("/data")
@app.route("/data/<name>")
def data(name: str="himanshu"):
    return f"<h1> This page is invoked by {name} </h1>" 

# you can invoke this data using /data/randomName 


if __name__ == '__main__':

    app.run(host="0.0.0.0")

