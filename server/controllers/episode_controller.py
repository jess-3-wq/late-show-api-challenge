from flask import Blueprint, jsonify, request
from ..models.episode import Episode
from ..models.appearance import Appearance
from ..models.guest import Guest
from ..app import db
from flask_jwt_extended import jwt_required

bp = Blueprint('episode_bp', __name__)

@bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    episode_list = [{"id": e.id, "date": e.date.isoformat(), "number": e.number} for e in episodes]
    return jsonify(episode_list), 200


@bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [
        {
            "id": a.id,
            "rating": a.rating,
            "guest": {
                "id": a.guest.id,
                "name": a.guest.name,
                "occupation": a.guest.occupation
            }
        }
        for a in episode.appearances
    ]
    return {
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": appearances
    }, 200


@bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return {"message": f"Episode {id} deleted"}, 200
