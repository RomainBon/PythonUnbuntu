#Met les info sur le navigateur

from linkbdd import Bdd
import json

if __name__ == '__main__':

    data = {"CPU": 44.4, "DISK": "[25668112384, 9942683648, 14397931520, 40.8]", "RAM": "[8243666944, 49.5, 668299264]", "BATTERY": "[100, -1, false]", "INFO": "[[\"romain\", \"tty2\", \"/dev/tty2\", 1256]]"}
    print(data)

    coBdd = Bdd()
    coBdd.createTable()
    coBdd.select()
    coBdd.insert(data)
    coBdd.select()
    coBdd.closeConnection()