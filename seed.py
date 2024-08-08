from app import app, db
from models import User
from flask_bcrypt import generate_password_hash

def seed_data():
    user1 = User(
        username="User1",
        password=generate_password_hash("password123").decode('utf-8')
    )
    user2 = User(
        username="User2",
        password=generate_password_hash("password123").decode('utf-8')
    )

    db.session.add_all([user1, user2])
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if User.query.count() == 0:
            seed_data()
            print("Database seeded successfully!")
