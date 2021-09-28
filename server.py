from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return("<h1>I am alive!</h1>")

def run():
  app.run(host='0.0.0.0',port=8080)

def server_run():
  t = Thread(target=run)
  t.start()