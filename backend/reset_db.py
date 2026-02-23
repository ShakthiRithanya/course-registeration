import os
from db.database import create_db_and_tables, seed_data

db_path = "database.db"
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Deleted {db_path}")

create_db_and_tables()
seed_data()
print("Database reset and seeded successfully!")
