import os
from database import Base, sync_engine
from models import ContactMessage 

if __name__ == "__main__":    
    try:    
        print("Створення таблиць...")
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        print("Таблиці успішно створені!")
    except Exception as e:
        print(f"Помилка: {e}")