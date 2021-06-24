from flask import Flask
from flask import render_template
from flask import request
import model


app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/mall")
def mall():
  return render_template("mall.html")

@app.route("/cart")
def cart():
  return render_template("cart.html")
  
@app.route("/entrance")
def entrance():
  return render_template("entrance.html")

@app.route("/fashion")
def fashion():
  return render_template("fashion.html")
  
if __name__ == "__main__":
  app.run()
