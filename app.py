from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

from flask_cors import CORS

current_dir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = 'static/'


app=Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "database.sqlite3")
#used for file upload
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
#limit max_size of uploaded files to 16 MB   
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024     
db = SQLAlchemy()
#from model import *
db.init_app(app)
#ensures that application context sets correctly for the database
app.app_context().push() 
#secret key generated & then assigned  to app.secret_key  
app.secret_key=os.urandom(24)   

from auth import *
from API import *


#script run as main module
if __name__== "__main__":
    #host & port no. on which flask application started in debug mode    
    #app.run(host='0.0.0.0', port=8080, debug=True)
    #db.create_all()   
    app.run(host='0.0.0.0', port=8080)    
 

