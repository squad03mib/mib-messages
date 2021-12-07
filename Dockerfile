FROM python:3.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY requirements.prod.txt /usr/src/app/

# installing all requirements
RUN ["pip", "install", "-r", "requirements.prod.txt"]

COPY . /usr/src/app

EXPOSE 8080

# Main command
CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]