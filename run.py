import sys
import os

import json

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


WAY_TO_UIS_FILES = "designs\ "


class Controller:
    def __init__(self):
        self.dir = os.getcwd()

    def get_available_projects(self):
        if not os.path.exists("Projects"):
            return []
        os.chdir("Projects")
        projects = []
        for file in os.listdir(path="."):
            if os.path.isfile(file) and file.split(".")[-1] == "json":
                projects = [self.parse_json(file)]
        os.chdir(self.dir)
        return projects

    def parse_json(self, file):
        with open(file, "r") as read_file:
            return json.load(read_file)




class MainWIndow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(WAY_TO_UIS_FILES[:-1] + 'main.ui', self)


class OpenWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        uic.loadUi(WAY_TO_UIS_FILES[:-1] + 'open.ui', self)
        for elem in data:
            self.open.addItem(str(elem["Character"]["Character"]["id"]) + "/" + elem["Character"]["Character"]["editor"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    con = Controller()
    open = OpenWindow(con.get_available_projects())
    open.show()
    sys.exit(app.exec_())
