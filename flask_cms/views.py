from flask_cms import app

@app.route('/')
def index():
  return 'Hi, I am Ahmed Sallam :)'