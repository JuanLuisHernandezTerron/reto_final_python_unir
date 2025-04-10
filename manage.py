import os

from app import create_app, db
from app.models import Data

env_name = os.getenv("FLASK_ENV", "development")
print(f"==> ENV_NAME: {env_name}", flush=True) 

app = create_app(env_name)

with app.app_context():
    db.create_all()
    print("Entrando para crear las tablas")
    sample_data = Data(name="SQL Test User")
    db.session.add(sample_data)
    db.session.commit()

print("Database tables created.")
