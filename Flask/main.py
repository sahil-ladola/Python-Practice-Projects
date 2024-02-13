from flask import Flask
app = Flask(__name__)
# flask --app main run terminal command


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!!!!</h1>'

@app.route("/bye")
def bye():
    return "Bye!"

# @app.route("/username/<name>")
# def greet(name):
#     return f"Hello {name}!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name} & you are {number} years old!"

# run
if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
