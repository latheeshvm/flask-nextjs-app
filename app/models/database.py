import os

from pymongo import MongoClient


class Database():

    def __init__(self, type: str, username: str, password: str, url: str, laodfromenv: bool, database: str, table: str) -> None:
        self.type = type
        self.table = table
        self.database = database
        if (type == 'mongodb'):
            self.url = self._mongodb_url_gen(
                username, password, url, laodfromenv)
            self.client = self._mongodb_init()

    def _mongodb_url_gen(self, username: str, password: str, url: str, loadfromenv: bool) -> str:
        if (loadfromenv):
            _username = os.environ.get(username)
            _password = os.environ.get(password)
            _url = os.environ.get(url)
        else:
            _username = username,
            _password = password
            _url = url

        return 'mongodb+srv://%s:%s@%s/?retryWrites=true&w=majority' % (
            _username, _password, _url)

    def _mongodb_init(self):
        try:
            print(self.url)
            client = MongoClient(self.url)
            client.server_info()
            print("Succesfully connected to database")
            return client
        except:
            print("Error in connecting database up database")

    def mongodb_load(self):
        try:
            loaddb = self.client[self.database]
            db = loaddb[self.table]
            print("Succesfully loaded db instance")
            return db
        except Exception:
            print(f"Error in loading the table : {Exception}")
