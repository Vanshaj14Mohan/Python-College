from flask import Flask

app = Flask(__name__)

#Define a route for the homepage
@app.route("/")
def home():
    return "Hello, welcome to my first web app!"

#Run the app on the local development server
# if __name__=="__main__":
    