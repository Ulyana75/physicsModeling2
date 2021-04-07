"""
Класс диалога, если виноваты егеря.
"""

from PyQt5 import QtWidgets

from ui.dialog_gamekeepers import Ui_Dialog
from utilits.constants import *


class GamekeepersDialog(Ui_Dialog, QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(DIALOG_WITH, DIALOG_HEIGHT)
        self.button_ok.clicked.connect(self.close)
        self.button_ok.setStyleSheet("""
                    QPushButton {font: 14pt "Comfortaa"; }
                    QPushButton:hover { background-color: rgb(0, 225, 0) }
                    QPushButton:!hover { background-color: rgb(0, 170, 0) }
                    QPushButton:pressed { background-color: rgb(0, 131, 0); }
                """)

    """
    Функция добавляет текст о том,
    сколько времени прошло с момента выстрела. 
    """
    def change_text(self, h, m):
        text = STRING_SHOOT_TIME
        text = text.replace('h', str(h))
        text = text.replace('m', str(m))
        self.shoot_time_label_3.setText(text)

