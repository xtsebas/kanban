import os
from dotenv import load_dotenv

load_dotenv()

# URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Error al conectarse a la base de datos")
