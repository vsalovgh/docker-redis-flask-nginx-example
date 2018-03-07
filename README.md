# docker-redis-flask-nginx-example
A simple version of app which logs timestamp/IP address to back-end API, with front-end view showing logs in a table.

1. To begin, have docker and docker-compose installed. 

2. On Linux, install docker-compose instructions:
https://docs.docker.com/compose/install/#install-compose

3. Go to repo folder, under /myapp, run commands:

            $ sudo docker-compose stop

            $ sudo docker-compose build

            $ sudo docker-compose up

4. Run ifconfig and find your machines IP address e.g. inet addr: example-ip

5. Open the app in your browser, url: example-ip:8084/
