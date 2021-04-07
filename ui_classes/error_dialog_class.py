"""
Класс диалога для некорректных данных
"""

from PyQt5 import QtWidgets

from ui.error_dialog import Ui_Dialog
from utilits.constants import *


class ErrorDialog(Ui_Dialog, QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(DIALOG_WITH, DIALOG_HEIGHT)
        self.button_ok.clicked.connect(self.close)
        self.button_ok.setStyleSheet("""
                    QPushButton {font: 14pt "Comfortaa"; }
                    QPushButton:hover { background-color: rgb(252, 84, 0) }
                    QPushButton:!hover { background-color: rgb(204, 68, 0) }
                    QPushButton:pressed { background-color: rgb(180, 43, 0); }
                """)
