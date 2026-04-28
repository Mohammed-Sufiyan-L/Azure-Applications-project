import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey2004'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstorage2004'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'IE3NMElmE8NhPe8iBT4ViKwGGTLP9S9sUq+eGBND9kXFRaFJIj7T+8kLkAMG4tR3pR57ePiW7OPN+AStEglgOA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsprojectserver2004.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Accenture2004!'

  SQLALCHEMY_DATABASE_URI = (
    'mssql+pyodbc://' + 
    (os.environ.get('SQL_USER_NAME') or 'cmsadmin') + ':' +
    (os.environ.get('SQL_PASSWORD') or 'Accenture2004!') + '@' +
    (os.environ.get('SQL_SERVER') or 'cmsprojectserver2004.database.windows.net') + ':1433/' +
    (os.environ.get('SQL_DATABASE') or 'cms') +
    '?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no&Connection+Timeout=30'
)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'Mx88Q~qxejQvp_PcsnX1-mZXWhvUq67t5FnO6b4N'
    AUTHORITY = "https://login.microsoftonline.com/common"
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'c593863b-3e72-44a3-b408-5338653f6496'
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
