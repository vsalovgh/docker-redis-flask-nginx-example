from flask import Flask, jsonify, request, render_template
import time
import datetime

app = Flask(__name__)

def time_ip(request):
	time_stamp = datetime.datetime.utcnow()
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
