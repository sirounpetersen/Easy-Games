# from turbo_flask import Turbo
# from flask import Flask, render_template, url_for, flash, redirect
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'xxxxxxxxxxxx'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

# turbo = Turbo(app)from forms import RegistrationForm

@app.route("/")
def home():
	return render_template("home.html")


@app.route("/trending")
def trending():
	return render_template("trending.html")

# @app.route("/trending")
# def trending():
# 	return render_template("trending.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
	#app.run()

