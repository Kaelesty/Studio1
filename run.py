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

    def openProject(self, project):
        studio = MainWIndow(project)
        studio.show()




class MainWIndow(QMainWindow):
    def __init__(self, project):
        super().__init__()
        uic.loadUi(WAY_TO_UIS_FILES[:-1] + 'main.ui', self)
        self.project = project

        self.loadProject()

    def loadProject(self):
        self.inp_id.setText(str(project["Character"]["Character"]["id"]))
        self.inp_editor.setText(str(project["Character"]["Character"]["editor"]))
        self.inp_game.setText(str(project["Character"]["Character"]["game"]))

        self.inp_hat.setText(str(project["Character"]["Clothes"]["hat"]))
        self.inp_mask.setText(str(project["Character"]["Clothes"]["mask"]))
        self.inp_glasses.setText(str(project["Character"]["Clothes"]["glasses"]))
        self.inp_vest.setText(str(project["Character"]["Clothes"]["vest"]))
        self.inp_pants.setText(str(project["Character"]["Clothes"]["pants"]))
        self.inp_shirt.setText(str(project["Character"]["Clothes"]["shirt"]))

        self.inp_primary.setText(str(project["Character"]["Behavior"]["primary"]))
        self.inp_secondary.setText(str(project["Character"]["Behavior"]["secondary"]))

        poses = ["Stand", "Sit", "Asleep", "Rest"]

        for pose in poses:
            self.inp_pose.addItem(pose)

        if project["Character"]["Behavior"]["pose"] in poses:
            self.inp_pose.setCurrentIndex(poses.index(project["Character"]["Behavior"]["pose"]))

        equips = ["Primary", "Secondary", "None"]

        for equip in equips:
            self.inp_equipped.addItem(equip)

        if project["Character"]["Behavior"]["equipped"] in poses:
            self.inp_pose.setCurrentIndex(poses.index(project["Character"]["Behavior"]["equipped"]))




class OpenWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        uic.loadUi(WAY_TO_UIS_FILES[:-1] + 'open.ui', self)
        for i in range(len(data)):
            self.open.addItem(str(i) + " / " + str(data[i]["Character"]["Character"]["id"]) + " / " + data[i]["Character"]["Character"]["editor"])

        self.projects = data

        self.openButton.clicked.connect(self.openProject)

    def openProject(self):
        global project
        project = self.projects[self.open.currentIndex()]
        self.hide()
        self.studio = MainWIndow(project)
        self.studio.show()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    con = Controller()
    project = []
    open = OpenWindow(con.get_available_projects())
    open.show()
    sys.exit(app.exec_())
