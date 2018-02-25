from flask import Flask, jsonify, request, render_template
import time

app = Flask(__name__)

def ip(request):
	return request.remote_addr

@app.route("/")
@app.route("/v1/logs", methods=["GET", "POST"])
def logs():
	address = ip(request)
	time_stamp = time.time()
	return jsonify({"logs": [{str(time_stamp): str(address)}]})

@app.route("/v1/helloworld", methods=['GET', 'POST'])
@app.route("/v1/helloworld/<name>", methods=['GET', 'POST'])
def helloworld(name=None):
	if name == None:
		address = ip(request)
		print address
		return jsonify({"message": "hello world"})
	elif name == 'logs':
		time_stamp = time.time()
		address = ip(request)
		print address
		# the following is to be modified/sent to redis in near future
		return jsonify({"logset": {"endpoint": "hello-world", "logs": [{str(time_stamp): str(address)}]}})

if __name__ == "__main__":
	app.run()
