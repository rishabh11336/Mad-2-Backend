from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from datetime import timedelta
from app import app, db
from model import User
from flask import request, jsonify

jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def UserRegister():
    data = request.get_json()
    name = data['name']
    password = data['password']
    email = data['email']
    contact_no = data['contact_no']
    sex = data['sex']
    address = data['address']

    if not email or not password:
        return {'message': 'email and password required'}, 400
    if User.query.filter_by(email=email).first():
        return {'message': 'email already exists'}, 400
    
    new_user = User(name=name, password=password, email=email, contact_no=contact_no, sex=sex, address=address)
    db.session.add(new_user)
    db.session.commit()
    return {'message': 'User created successfully'}, 201

@app.route('/login', methods=['POST'])
def UserLogin():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email, password=password).first()
    if not user:
        return {'message': 'Invalid credentials'}, 401

    expiry = timedelta(days=1)
    access_token = create_access_token(identity=user.id, expires_delta=expiry)
    return {'message': 'Logged in successfully', 'access_token': access_token}, 200