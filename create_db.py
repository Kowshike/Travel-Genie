from app import app, db  # Import your Flask app and db instance

# Use the application context
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
