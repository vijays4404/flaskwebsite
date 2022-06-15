#importing flask library
from flask import Blueprint,render_template,jsonify,request,redirect,url_for
#storing a Blueprint instance to a variable
views=Blueprint(__name__,"views")

#using views instance and storing attributes
@views.route('/')
def home():
    #returning home page
    return render_template("index.html",name="Vijay",age=31)

@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html",name=username)

@views.route("/json")
def get_json():
    return jsonify({'name':"Vijay","coolness":10})

@views.route("/data")
def get_data():
    data=request.json
    return jsonify(data)


@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("view.home"))