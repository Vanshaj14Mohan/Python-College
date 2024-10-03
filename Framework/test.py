from flask import Flask

app = Flask("Vanshaj")

#Define a route for the homepage
@app.route("/")
def home():
    return "Hello, welcome to my first web app made by flask tbh!"

#Run the app on the local development server
# if __name__=="__main__":
#     app.run(debug=True)
if __name__=="__main__":
    app.run(debug=True)
    app.run()


    