import flask
import slack
import os

app = flask.Flask("Api Test")

#Funky time!
@app.route("/Test")

def TestFunc():
	num1 = flask.request.args.get("num1")
	num2 = flask.request.args.get("num2")
	regularDict = {"variable1" : int(num1), "variable2" : int(num2)}
	return regularDict
	
# def PrintStuff():
# 	return "'ello Mate!"


# @app.route("/bob")	
# def NewFunc():
# 	lat = flask.request.args.get("lat")
# 	lon = flask.request.args.get("long")
# 	return "You're at {0} and {1}".format(lat, lon)


# @app.route("/willy/<variableName>")	
# def CreativeFunc(variableName):
# 	return variableName + " an some more stuff"

app.run()