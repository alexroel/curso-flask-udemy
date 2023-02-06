#cofiguración file

# SECRET_KEY='dev'
# SQLALCHEMY_DATABASE_URI="sqlite:///project.db"


# SQLITE = "sqlite:///project.db"
# POSTGRESQL = "postgresql+psycopg2://postgres:123456@localhost:5432/myblog_db"

class Config:
    DEBUG = True
    TESTING = True

    #Configuración de base dedatos 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

class DevConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING = True

class ProConfig(Config):
    DEBUG = False