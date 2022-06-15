#importing Flask
from flask import Flask
#importing views from view python file
from view import views
#storing Flask instance to a variable
app=Flask(__name__)
app.register_blueprint(views,url_prefix="/views")



if __name__=='__main__':
    app.run(debug=True,port=8000)
    