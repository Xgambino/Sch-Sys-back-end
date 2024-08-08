from app import create_app
from models import db, Message

app = create_app()

with app.app_context():
    db.create_all()
    
    # Seed the database with some initial messages
    if Message.query.count() == 0:
        messages = [
            Message(content='Hello, world!'),
            Message(content='Welcome to the chat!'),
        ]
        db.session.bulk_save_objects(messages)
        db.session.commit()

    print('Database seeded!')
