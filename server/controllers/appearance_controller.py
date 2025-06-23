from flask import Blueprint, request, jsonify
from ..models.appearance import Appearance
from ..models.episode import Episode
from ..models.guest import Guest
from ..app import db
from flask_jwt_extended import jwt_required

bp = Blueprint('appearance_bp', __name__)

@bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()

    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    if not all([rating, guest_id, episode_id]):
        return {"error": "All fields are required"}, 400

    
    guest = Guest.query.get(guest_id)
    episode = Episode.query.get(episode_id)
    if not guest or not episode:
        return {"error": "Guest or Episode not found"}, 404

    try:
        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

    return {
        "id": appearance.id,
        "rating": appearance.rating,
        "guest_id": appearance.guest_id,
        "episode_id": appearance.episode_id
    }, 201
