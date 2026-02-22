# Import Flask from flask package
from flask import Flask

# Create a Flask app
app = Flask(__name__)

# This is the home page route ("/" means main page)
@app.route("/")
def index():
    # This message will show in the browser
    return "<h1>Hello User Welcome to site.</h1>"

# This makes sure the app runs only when we run this file directly
if __name__ == "__main__":
    # Start the server
    # host="0.0.0.0" allows others on the same network to access it
    # debug=True shows errors and auto reloads when code changes
    app.run(host="0.0.0.0", debug=True)