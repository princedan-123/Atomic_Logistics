"""The entry point of the application."""
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """The landing page for atomic logistics."""
    return render_template('index.html')


app.run(host='localhost', port=5500, debug=True)
