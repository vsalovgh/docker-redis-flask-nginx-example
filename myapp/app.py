from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
import datetime
import redis
import json

app = Flask(__name__)

r = redis.StrictRedis(host='redis', port=6379, db=0)

def time_ip(request, endpoint):
    '''Takes timestamp, creates json and sets into redis. Returns timestamp and IP address.'''
    time_stamp = datetime.datetime.utcnow()
    log = json.dumps({str(time_stamp): str(request.remote_addr)})
    r.set(endpoint, log)
    r.set(log, endpoint)
    return time_stamp, request.remote_addr

def return_logs():
    '''Takes out all of the redies queued keys and returns everything via json.'''
    logs_list = []
    helloworld_list = []
    helloworldlogs_list = []
    for key in r.keys():
        if key != 'logs'.encode('utf-8') and key != 'hello-world/logs'.encode('utf-8') and key != 'hello-world'.encode('utf-8'):
            print key, r[key]
            if r[key] == 'logs'.encode('utf-8'):
                logs_list.append(key)
            if r[key] == 'hello-world'.encode('utf-8'):
                helloworld_list.append(key)
            if r[key] == 'hello-world/logs'.encode('utf-8'):
                helloworldlogs_list.append(key)
            api = {"logset": [{"endpoint": "hello-world", "logs": sorted(helloworld_list)},
            {"endpoint": "logs", "logs": sorted(logs_list)},
            {"endpoint": "hello-world/logs", "logs": sorted(helloworldlogs_list)}]}
    return api

@app.route("/")
def index():
    '''View which pass all logs to all endpoints to template.'''
    logs = return_logs()
    return render_template("logs.html", logs=logs)

@app.route("/v1")
def helloworld_logs():
    '''View which passes only the helloworld/logs endpoint logs to template.'''
    logs = return_logs()
    helloworld_logs = logs["logset"][-1]
    return render_template("logshw.html", logs=helloworld_logs)

@app.route("/v1/logs", methods=["GET", "POST"])
def logs():
    '''Queues log via time_ip then returns the logs for all API endpoings via return_logs.'''
    time_stamp, address = time_ip(request, 'logs')
    logs = return_logs()
    return jsonify(logs)

@app.route("/v1/helloworld", methods=['GET', 'POST'])
@app.route("/v1/helloworld/<name>", methods=['GET', 'POST'])
def helloworld(name=None):
    '''Checks for endpoint, queues log, and either returns helloworld json or json for endpoint helloworld/logs.'''
    if name == None:
        address = time_ip(request, 'hello-world')
        return jsonify({"message": "hello world"})
    elif name == 'logs':
        time_stamp, address = time_ip(request, 'hello-world/logs')
        logs = return_logs()
        helloworld_logs = logs["logset"][-1]
        return jsonify({"logs": helloworld_logs["logs"]})

if __name__ == "__main__":
    app.run(debug='True', host='0.0.0.0', port=8080)
