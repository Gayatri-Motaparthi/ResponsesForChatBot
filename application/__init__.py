from flask import Flask

app = Flask(__name__) #instance of Flask

# app.secret_key = "hello"


from application import routes