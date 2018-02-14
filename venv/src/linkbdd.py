# object BDD permet de faire tous les traitements sur la bdd qui lui est relatif

import mysql.connector
import json


class Bdd(object):

    def __init__(self):

        self.conn = mysql.connector.connect(host="localhost", user="root", password="root", database="ProPy")
        self.cursor = self.conn.cursor()

    def createTable(self):

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `metrics_composant` (
        `id` int(5) NOT NULL,
        `CPU` text,
        `DISK` text,
        `RAM` text,
        `BATTERY` text,
        `INFO` text NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;""")

    def insert(self, data):

        for key, value in data.items():
            if isinstance(value, list):
                value = json.dumps(value)
            data[key] = value

        self.cursor.execute("""INSERT INTO `metrics_composant`(`CPU`, `DISK`, `RAM`, `BATTERY`, `INFO`) VALUES(%(CPU)s, %(DISK)s, %(RAM)s, %(BATTERY)s, %(INFO)s)""",  data)
        self.conn.commit()

    def select(self):

        data = {}

        self.cursor.execute("""SELECT * FROM metrics_composant ORDER BY id DESC LIMIT 1 """)
        rows = self.cursor.fetchall()

        for row in rows:
            print('{0} : {1} / {2} / {3} / {4} / {5}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))

            data = {"id": row[0]}
            data = {"CPU": row[1]}
            data = {"DISK": row[2]}
            data = {"RAM": row[2]}
            data = {"BATTERY": row[4]}
            data = {"INFO": row[5]}

        return data

    def closeConnection(self):

        self.conn.close()
