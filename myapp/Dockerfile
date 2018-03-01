FROM python:2.7
MAINTAINER Victor Salov "vsalov@yahoo.com"
ADD . /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app"]
