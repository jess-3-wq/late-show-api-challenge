from flask import Blueprint, request, jsonify
from ..app import db
from ..models.user import User
from flask_jwt_extended import create_access_token

bp = Blueprint('auth_bp', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data.get('username') or not data.get('password'):
        return {"error": "Username and password required"}, 400

    if User.query.filter_by(username=data['username']).first():
        return {"error": "Username already exists"}, 400

    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()

    return {"message": "User created"}, 201


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if not user or not user.check_password(data['password']):
        return {"error": "Invalid details"}, 401

    access_token = create_access_token(identity=user.id)
    return {"access_token": access_token}, 200
