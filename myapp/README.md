A simple example of dockerized flask API, which uses redis to store timestamp and IP logs to the API, and nginx to
serve static content through gunicorn WSGI HTTP server.

ip_of_docker_machine:8084 - View shows static page with log of all API endpoint visits
ip_of_docker_machine:8084/v1 - View shows static page with log of all API vists to web:8080/v1/helloworld/logs
ip_of_docker_machine:8084/v1/logs - API endpoint which returns json of all API endpoint visits
ip_of_docker_machine:8084/v1/helloworld - returns json with "message": "hello world" key/value pair
ip_of_docker_machine:8084/v1/helloworld/logs - returns all logs to /v1/helloworld