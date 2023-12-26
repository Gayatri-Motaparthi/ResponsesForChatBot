# from flask import Flask , render_template , redirect, url_for, request, session, flash
# from application import app

from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from application import app

from application.getBardResponse import getResponse

@app.route("/", methods=[ "POST"])
def home():
    # if request.method == "POST":
    question = request.json.get("question")  # Use request.json to get JSON data
    print (getResponse(question))
    return getResponse(question)
# #
# else:
#     return "This is the GET method"
