from db import DB_Manager
from config import DATABASE

if __name__ == "__main__":
    manager = DB_Manager(DATABASE)
    
    manager.create_tables()
    manager.default_insert()

    manager.insert_project((
        1,
        "Бот-портфолио",
        "https://github.com/USERNAME/telegram-portfolio-bot",
        1
    ))

    print(manager.get_projects(1))
    print(manager.get_project_info(1, "Бот-портфолио"))
