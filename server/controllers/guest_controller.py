from flask import Blueprint, jsonify
from ..models.guest import Guest

bp = Blueprint('guest_bp', __name__)

@bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    guest_list = [{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests]
    return jsonify(guest_list), 200
