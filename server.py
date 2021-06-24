from flask import Flask
from flask import render_template
from flask import request
import model


app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
  if request.method == 'POST' and len(dict(request.form)) > 0:
    userdata = dict(request.form)
    print(userdata)
    book = userdata["book"][0]
    character = model.get_character(book)
    gif_url = model.get_gif(character)
    return render_template("result.html", character=character, gif_url=gif_url)
  else:
    return "Sorry, there was an error."
  
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
