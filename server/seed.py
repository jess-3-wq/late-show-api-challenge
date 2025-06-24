from server.app import create_app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username="admin")
    user1.password = "password123"
    db.session.add(user1)

    guest1 = Guest(name="Jesse Yegon", occupation="Software Engineer")
    guest2 = Guest(name="Sandra Naisoi", occupation="Data Analyst")
    db.session.add_all([guest1, guest2])

    episode1 = Episode(date="2007-06-26", number=1)
    episode2 = Episode(date="2007-08-31", number=2)
    db.session.add_all([episode1, episode2])

    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode2)
    db.session.add_all([appearance1, appearance2])

    db.session.commit()

    print("Clean Database seeded!")
