"""A blueprint module that groups admin routes."""
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import admin_collection
admin_blueprint = Blueprint('admin_blueprint', __name__)

@admin_blueprint.route('/login', methods=['POST'], strict_slashes=True)
def admin_login():
    """An implementation of admin login feature"""
    #  get login credentials from client
    email = request.form.get('email')
    password_input = request.form.get('password')
    if not email or not password_input:
        return 'email or password is missing', 400
    if '@' not in email:
        return 'invalid email', 400
    user = admin_collection.find_one({ 'email': email}, {'_id': 0})
    if not user:
        return 'invalid credentials', 401
    user_password = user.get('password')
    if not check_password_hash(user_password, password_input):
        return 'invalid credentials', 401
    user_role = user.get('role')
    print(user_role)
    if user_role not in ['SuperAdmin', 'Admin']:
        return 'You are not an admin', 403
    del user['password']  #  removed sensitive data from user
    access_token_cookie = create_access_token(identity=user)
    response = jsonify(user_role=access_token_cookie)
    response.set_cookie('access_token_cookie', access_token_cookie, max_age=60*60)
    return response

@admin_blueprint.route('/logout', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def admin_logout():
    """implement admin logout feature"""
    user = get_jwt_identity()
    role = user['role']
    response = jsonify(role='logged out')
    response.set_cookie('access_token_cookie', '', expires=0)
    return response
