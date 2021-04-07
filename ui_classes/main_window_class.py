"""
Класс для сбора данных и вывода диалоговых окон с ответом.
"""

import sys
from math import log

from PyQt5 import QtWidgets
from PyQt5.QtCore import QLocale
from PyQt5.QtGui import QDoubleValidator

from ui.main_window import Ui_MainWindow
from ui_classes.error_dialog_class import ErrorDialog
from utilits.constants import *
from ui_classes.gamekeepers_dialog_class import GamekeepersDialog
from ui_classes.poachers_dialog_class import PoachersDialog
from utilits.my_error_class import MyError


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)
        self.button_get_answer.setStyleSheet("""
            QPushButton:hover { background-color: rgb(177, 194, 142) }
            QPushButton:!hover { background-color: rgb(153, 167, 88) }
            QPushButton:pressed { background-color: rgb(63, 71, 31); }
        """)

        self.temperature0_lineEdit.setValidator(self.get_validator())
        self.temperature1_lineEdit.setValidator(self.get_validator())
        self.temperature2_lineEdit.setValidator(self.get_validator())
        self.a_lineEdit.setValidator(self.get_validator())
        self.wt_lineEdit.setValidator(self.get_validator())

        self.poachers_dialog = PoachersDialog()
        self.gamekeepers_dialog = GamekeepersDialog()
        self.error_dialog = ErrorDialog()

        self.button_get_answer.clicked.connect(self.error_dialog.close)
        self.button_get_answer.clicked.connect(self.poachers_dialog.close)
        self.button_get_answer.clicked.connect(self.gamekeepers_dialog.close)
        self.button_get_answer.clicked.connect(self.make_conclusion)

    """
    Делаем так, чтобы можно было вводить только числа
    """
    def get_validator(self):
        v = QDoubleValidator(-100, 100, 5, self)
        v.setLocale(QLocale(QLocale.English))
        return v

    """
    Возвращает текст со всех lineEdit-ов
    """
    def get_data(self):
        x0 = self.temperature0_lineEdit.text()
        x1 = self.temperature1_lineEdit.text()
        x2 = self.temperature2_lineEdit.text()
        a = self.a_lineEdit.text()
        wt = self.wt_lineEdit.text()
        return x0, x1, x2, a, wt

    """
    Проверка на корректность введенных данных
    """
    def check_data(self, x0, x1, x2, a, wt):
        if len(str(x0 + x1 + x2 + a + wt)) < 5 or \
                (a > x0 and (x1 > x2 or x1 < x0)) or (a < x0 and (x1 < x2 or x1 > x0)) or (a == x0 and x1 != x2 != x0):
            return False
        return True

    """
    Считаем время выстрела.
    Бросается исключение, если данные оказались некорректны.
    """
    def get_answer(self):
        lst = self.get_data()
        if not self.check_data(*lst):
            raise MyError("Invalid data")
        x0, x1, x2, a, wt = list(map(float, lst))
        t = log(abs(x0 - a) / abs(x1 - a)) / log(abs(x1 - a) / abs(x2 - a))
        return t, wt

    """
    Вызываем диалог в соответствии с результатом.
    """
    def make_conclusion(self):
        try:
            t, wt = self.get_answer()
            h = int(t)
            m = int(60 * (t - int(t)))
            if t <= wt:
                self.gamekeepers_dialog.change_text(h, m)
                self.gamekeepers_dialog.show()
            else:
                self.poachers_dialog.change_text(h, m)
                self.poachers_dialog.show()
        except MyError:
            self.error_dialog.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
