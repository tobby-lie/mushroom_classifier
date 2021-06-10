FROM python:3

ADD requirements.txt /app/
WORKDIR /app

RUN pip install -r requirements.txt

ADD . /app

EXPOSE 5000

RUN pip3 install --no-cache-dir tensorflow

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]