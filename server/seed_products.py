from app import create_app
from models import db
from utils.database_seeder import DatabaseSeeder

app = create_app()
with app.app_context():
    seeder = DatabaseSeeder(db)
    seeder.seed_products()