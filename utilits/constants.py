from PyQt5.QtGui import QFontDatabase

STRING_SHOOT_TIME = "Время выстрела:\nh часов m минут назад"
STRING_IMPOSSIBLE = "Невозможно рассчитать\n время выстрела!"
STRING_INVALID_DATA = "Невозможные данные!\nПроверьте\nвведенные числа!"


MAIN_WINDOW_WIDTH = 889
MAIN_WINDOW_HEIGHT = 787

DIALOG_WITH = 400
DIALOG_HEIGHT = 388


def init_font():
    QFontDatabase.addApplicationFont(":/Comfortaa.ttf")
