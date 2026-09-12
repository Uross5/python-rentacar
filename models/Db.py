import pymysql
import os
from dotenv import load_dotenv
load_dotenv()
class Db:
    def __init__(self):
        self.__connection=pymysql.connect(
            host=os.environ["DB_HOST"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            database=os.environ["DB_NAME"],
            port=int(os.environ["DB_PORT"])
    )

    def _get_connection(self):
        return self.__connection



