FROM python:3.10

RUN apt-get update

COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip3 install -r requirements.txt

COPY . /api
WORKDIR /

CMD ["gunicorn", "-w", "2", "-b", ":5000", "-t", "8", "api.wsgi:app"]
