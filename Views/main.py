import sys
import methods as mets
import solo as solo
import multi as multi
import options as op
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

ruta_txt = "src/AdminSoftware/res/options/options.txt"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("La Cocinita")
        self.resize(1080, 720)
        self.setup_buttons()
        mets.iconify(self)

        # Create the title label
        label = QLabel(self)
        label.setObjectName("titulo")
        label.setText(" La Cocinita")
        label.setGeometry(325, 50, 500, 120)

    def setup_buttons(self):
        # region buttons
        btn_solo = mets.ColoredButton("Jugar en \nsolitario", self)
        btn_solo.setObjectName("btn_inicio")
        btn_solo.setFixedSize(200, 200)
        btn_solo.move(200, 200)
        btn_solo.clicked.connect(self.on_btn_solo_clicked)

        btn_multi = mets.ColoredButton("Jugar en \nmultijugador", self)
        btn_multi.setObjectName("btn_inicio")
        btn_multi.setFixedSize(200, 200)
        btn_multi.move(600, 200)
        btn_multi.clicked.connect(self.on_btn_multi_clicked)

        btn_opciones = mets.ColoredButton("Opciones", self)
        btn_opciones.setObjectName("btn_inicio")
        btn_opciones.setFixedSize(200, 200)
        btn_opciones.move(400, 450)
        btn_opciones.clicked.connect(self.on_btn_opciones_clicked)
        # endregion

    # region button functions
    def on_btn_solo_clicked(self):
        self.close()
        nombre_extraido = obtener_nombre(ruta_txt)
        nombre = nombre_extraido if nombre_extraido is not None else ""
        self.solo = solo.solo(nombre=nombre)
        self.solo.menu_principal_signal.connect(self.show_main_window)
        self.solo.show()

    def on_btn_multi_clicked(self):
        self.close()
        nombre_extraido = obtener_nombre(ruta_txt)
        nombre = nombre_extraido if nombre_extraido is not None else ""
        self.multi = multi.multi(nombre=nombre)
        self.multi.menu_principal_signal.connect(self.show_main_window)
        self.multi.show()

    def on_btn_opciones_clicked(self):
        self.close()
        nombre = obtener_nombre(ruta_txt)
        tareas = mets.obtener_tareas(ruta_txt)
        self.opciones = op.options(nombre or "", tareas or 0)
        self.opciones.menu_principal_signal.connect(self.show_main_window)
        self.opciones.show()

    def show_main_window(self):
        self.show()
    # endregion

def obtener_nombre(ruta_archivo):
    try:
        # Abrir el archivo en modo lectura
        with open(ruta_archivo, 'r') as archivo:
            # Leer todas las líneas del archivo
            lineas = archivo.readlines()

            # Buscar la línea que contiene "Nombre:"
            for linea in lineas:
                if "Nombre:" in linea:
                    # Extraer el nombre después de "Nombre:"
                    nombre = linea.split(":")[1].strip()
                    return nombre

    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None


app = QApplication(sys.argv)
window = MainWindow()
mets.apply_stylesheet(app)
window.show()
sys.exit(app.exec())