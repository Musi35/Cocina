from PySide6.QtWidgets import QLabel, QPushButton
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt

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

def obtener_tareas(ruta_archivo):
    try:
        # Abrir el archivo en modo lectura
        with open(ruta_archivo, 'r') as archivo:
            # Leer todas las líneas del archivo
            lineas = archivo.readlines()

            # Buscar la línea que contiene "Tareas:"
            for linea in lineas:
                if "Tareas:" in linea:
                    # Extraer el número de tareas después de "Tareas:"
                    tareas = int(linea.split(":")[1].strip())
                    return tareas

    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None

def set_image_on_label(label, image_path, number):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(label.width() * number)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)