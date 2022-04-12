from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def base_route():
    return "Welcome to q3"

@app.route('/<user_name>')
def print_name(user_name):
    return f"welcome {user_name}"

if __name__ == "_main_":
    app.run(host = "0.0.0.0",port = 8080, debug = True)