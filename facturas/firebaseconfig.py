import configparser

import pyrebase
from pyrebase.pyrebase import Database, Storage, Firebase

from djangoProject.settings import PROJECT_SETTINGS_ROOT

config = configparser.ConfigParser()
config.read(PROJECT_SETTINGS_ROOT)


class FirebaseConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, firebase_config=None):
        default_conf = {
            'databaseURL': config.get('Firebase', 'databaseURL'),
            'apiKey': config.get('Firebase', 'apiKey'),
            'authDomain': config.get('Firebase', 'authDomain'),
            'projectId': config.get('Firebase', 'projectId'),
            'storageBucket': config.get('Firebase', 'storageBucket'),
            'messagingSenderId': config.get('Firebase', 'messagingSenderId'),
            'appId': config.get('Firebase', 'appId'),
            'measurementId': config.get('Firebase', 'measurementId')
        }

        firebase_config = firebase_config if firebase_config else default_conf
        self._firebase_config = firebase_config
        self._firebase: Firebase = pyrebase.initialize_app(self._firebase_config)

    def auth(self):
        self._firebase.auth()

    def get_database(self) -> Database:
        database: Database = self._firebase.database()
        return database

    def get_storage(self) -> Storage:
        storage: Storage = self._firebase.storage()
        return storage

