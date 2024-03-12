from PySide6.QtWidgets import QLabel, QPushButton
from PySide6.QtGui import QPixmap, QIcon
import connection as con
import random, time

class ColoredButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

def load_image_label(window, image_path):
    label = QLabel(window)
    pixmap = QPixmap(image_path)
    label.setPixmap(pixmap)
    return label

def apply_stylesheet(app):
    with open("src/AdminSoftware/res/style/style.qss", "r") as file:
        app.setStyleSheet(file.read())

def iconify(window):
    window.setWindowIcon(QIcon("src/AdminSoftware/res/img/icono.ico"))

def temporizador(segundos):
    for segundo_actual in range(segundos, 0, -1):
        time.sleep(1)
        return True
