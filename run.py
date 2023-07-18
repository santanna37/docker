from flask import Flask
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_word():
    return 'ola mundo'

if __name__ == '__main__':
    app.run(debug=True)



# syntax=docker/dockerfile:1

# FROM python:3.8-slim-buster

# WORKDIR /app
# ENV FLASK_APP run.py

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .

# CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" , "--port=5000"]

