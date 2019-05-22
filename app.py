from flask import Flask, render_template
from config import Confiruration
import json
app = Flask(__name__)
app.config.from_object(Confiruration)


@app.route("/")
def test():
    return render_template("index.html")

@app.route("/bronirovanie", methods = ['POST'])
def ajax_bron():
	return json.dumps(200)
# from users import models, views
