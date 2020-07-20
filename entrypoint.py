import os

from app import create_app
#Cargo a la variable settings_module el valor que le asigné a la 
#variable global APP_SETTINGS_MODULE en Activate.bat
settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)