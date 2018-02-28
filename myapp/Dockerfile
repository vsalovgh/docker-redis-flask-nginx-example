FROM python:2.7
MAINTAINER Victor Salov "vsalov@yahoo.com"
ADD . /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
