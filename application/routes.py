# from flask import Flask , render_template , redirect, url_for, request, session, flash
# from application import app

# from application.getMatch import getMatch 

# @app.route("/", methods=["GET", "POST"])
# def home():

#     if(request.method == "POST"):
#         question = request.form.question

#         return ("post method")
#     else:
#         return ("this is get method")

from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from application import app

from application.getMatch import getMatch

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        question = request.json.get("question")  # Use request.json to get JSON data
        print (getMatch(question))
        return getMatch(question)
    
    else:
        return "This is the GET method"
