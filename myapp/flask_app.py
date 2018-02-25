from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
import datetime
import redis

app = Flask(__name__)

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def time_ip(request):
	time_stamp = datetime.datetime.utcnow()
	r.set(str(time_stamp), str(request.remote_addr))
	return time_stamp, request.remote_addr

@app.route("/")
@app.route("/v1/logs", methods=["GET", "POST"])
def logs():
	time_stamp, address = time_ip(request)
	# the following is to be modified/sent to redis in near future
	return jsonify({"logset": {"endpoint": "hello-world", "logs": [{str(time_stamp): str(address)}]}})

@app.route("/v1/helloworld", methods=['GET', 'POST'])
@app.route("/v1/helloworld/<name>", methods=['GET', 'POST'])
def helloworld(name=None):
	if name == None:
		address = time_ip(request)
		return jsonify({"message": "hello world"})
	elif name == 'logs':
		time_stamp, address = time_ip(request)
		return jsonify({"logs": [{str(time_stamp): str(address)}]})

if __name__ == "__main__":
	app.run()
