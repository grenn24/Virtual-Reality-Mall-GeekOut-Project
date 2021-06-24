from flask import Flask
from flask import render_template
from flask import request
import model


app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")
  
@app.route("/entrance")
def entrance():
  return render_template("entrance.html")

@app.route("/fashion")
def fashion():
  return render_template("fashion.html")

@app.route("/fnb")
def fnb():
  return render_template("fnb.html")
  
if __name__ == "__main__":
  app.run()
