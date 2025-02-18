import os
import subprocess
from InquirerPy import prompt
from .utils import create_folder, create_file, install_requirements
from .templates import (
    PYTHON_MAIN_COGS, PYTHON_MAIN_NO_COGS, CONFIG_PY, ENV_FILE, COG_EXAMPLE,
    SQLITE_SETUP, POSTGRES_SETUP, MONGODB_SETUP,
)

def generate_bot():
    questions = [
        {"type": "list", "name": "language", "message": "Select programming language:", "choices": ["Python"]},
        {"type": "list", "name": "config_type", "message": "Select configuration method:", "choices": ["config.py", ".env"]},
        {"type": "confirm", "name": "use_cogs", "message": "Use cogs (modular command files)?", "default": True},
        {"type": "list", "name": "database", "message": "Select database:", "choices": ["None", "SQLite", "PostgreSQL", "MongoDB"]},
    ]

    answers = prompt(questions)
    lang = answers["language"]
    config_type = answers["config_type"]
    use_cogs = answers["use_cogs"]
    database = answers["database"]

    if lang == "Python":
        create_python_bot(config_type, use_cogs, database)

def create_python_bot(config_type, use_cogs, database):
    project_name = prompt({"type": "input", "name": "project_name", "message": "Enter your bot project name:"})["project_name"]
    base_path = os.path.join(os.getcwd(), project_name)
    create_folder(base_path)

    requirements = ["discord"]
    
    if config_type == "config.py":
        token_line = "from config import TOKEN, PREFIX"
        create_file(os.path.join(base_path, "config.py"), CONFIG_PY)
    else:
        token_line = "from dotenv import load_dotenv\nimport os\nload_dotenv()\nTOKEN = os.getenv('TOKEN')\nPREFIX = os.getenv('PREFIX')"
        create_file(os.path.join(base_path, ".env"), ENV_FILE)
        requirements.append("python-dotenv")

    db_imports, db_setup_code, db_on_ready = "", "", ""

    if database == "SQLite":
        db_imports = "import sqlite3\nfrom database import setup_db"
        db_setup_code = SQLITE_SETUP
        db_on_ready = "setup_db()"
    elif database == "PostgreSQL":
        db_imports = "import psycopg2\nfrom database import setup_db"
        db_setup_code = POSTGRES_SETUP
        db_on_ready = "setup_db()"
        requirements.append("psycopg2")
    elif database == "MongoDB":
        db_imports = "from pymongo import MongoClient\nfrom database import setup_db"
        db_setup_code = MONGODB_SETUP
        db_on_ready = "setup_db()"
        requirements.append("pymongo")

    if db_setup_code:
        create_file(os.path.join(base_path, "database.py"), db_setup_code)

    if use_cogs:
        create_folder(os.path.join(base_path, "cogs"))
        create_file(os.path.join(base_path, "cogs", "__init__.py"), "")
        create_file(os.path.join(base_path, "cogs", "example.py"), COG_EXAMPLE)
        main_content = PYTHON_MAIN_COGS.format(token_line=token_line, db_imports=db_imports, db_on_ready=db_on_ready)
    else:
        main_content = PYTHON_MAIN_NO_COGS.format(token_line=token_line, db_imports=db_imports, db_on_ready=db_on_ready)

    create_file(os.path.join(base_path, "main.py"), main_content)
    
    install_requirements(requirements, base_path)

    print(f"✅ QuickBot '{project_name}' created successfully!")
