from PySide6.QtWidgets import QLabel, QWidget, QMessageBox, QApplication
import methods as mets
import burgers as burgi
import transition as trs
import main as mn
from PySide6.QtCore import Signal, Qt
import random, connection as con

ruta_txt = "src/AdminSoftware/res/options/options.txt"
max_fondo = mets.obtener_tareas(ruta_txt)
cont_fondo = 1

class solo(QWidget):
    menu_principal_signal = Signal()

    def __init__(self):
        super().__init__()
        label = mets.load_image_fondo(self, "src/AdminSoftware/res/img/fondo_solo.jpg")
        self.setObjectName("solo")
        self.setWindowTitle("La Cocinita - Modo Solitario")
        self.resize(1080, 720)
        mets.iconify(self)
        lista = generar_ordenes()

        # region labels
        lbl_nombre = QLabel(self)
        lbl_nombre.setObjectName("titulo")
        lbl_nombre.setText(mets.obtener_nombre(ruta_txt) + "'s") # type: ignore
        lbl_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_nombre.setGeometry(0, 0, 1080, 120)

        self.lbl_cliente = QLabel(self)
        self.lbl_cliente.setObjectName("test")
        self.lbl_cliente.setFixedSize(240, 270)
        self.lbl_cliente.move(400, 200)
        mets.set_image_on_label(self.lbl_cliente, con.obtener_ruta(lista[0]), 1.2)

        self.lbl_propinas = QLabel(self)
        self.lbl_propinas.setObjectName("titulo")
        self.lbl_propinas.setFixedSize(172,151)
        self.lbl_propinas.move(90, 437)
        mets.set_image_on_label(self.lbl_propinas, "src/AdminSoftware/res/img/tips/p_0.jpg", 1.2)
        # endregion

        # region buttons
        self.btn_tareas = mets.ColoredButton("Atender Cliente", self)
        self.btn_tareas.setObjectName("otros")
        self.btn_tareas.setFixedSize(160, 60)
        self.btn_tareas.move(880, 130)
        self.btn_tareas.clicked.connect(lambda: self.on_btn_tareas_clicked(lista))

        btn_salir = mets.ColoredButton("Menú Principal", self)
        btn_salir.setObjectName("otros")
        btn_salir.setFixedSize(160, 60)
        btn_salir.move(880, 50)
        btn_salir.clicked.connect(self.on_btn_salir_clicked)
        # endregion

    def on_btn_salir_clicked(self):
        main_window = [widget for widget in QApplication.topLevelWidgets() if isinstance(widget, mn.MainWindow)]
        if main_window:
            main_window[0].show()
        self.close()

    def on_btn_tareas_clicked(self, lista):
        global cont_fondo, max_fondo

        # Verificar si todavía hay clientes en la lista
        if len(lista) == 0:
            QMessageBox.information(self, "Terminaste el día", "Ya no hay clientes, ¡buen trabajo!")
            self.close()
            self.transicion = trs.transition()
            self.transicion.burguir_signal.connect(self.transicion.show_solo_window)
            self.transicion.show()
            cont_fondo = 1
            return None
        else:
            # Actualizar la imagen del cliente y las propinas
            if len(lista) == 1:
                mets.set_image_on_label(self.lbl_cliente, "src/AdminSoftware/res/img/cerrado.png", 1.2)
            else:
                mets.set_image_on_label(self.lbl_cliente, con.obtener_ruta(lista[1]), 1.2)

        # Verificar y actualizar la imagen de propinas
        if cont_fondo <= max_fondo: # type: ignore
            background_path = f"src/AdminSoftware/res/img/tips/p_{cont_fondo}.jpg"
            mets.set_image_on_label(self.lbl_propinas, background_path, 1.2)
            cont_fondo += 1
        else:
            # Reiniciar el contador de fondo si excede el número máximo de imágenes
            cont_fondo = 1
            background_path = f"src/AdminSoftware/res/img/tips/p_{cont_fondo}.jpg"
            mets.set_image_on_label(self.lbl_propinas, background_path, 1.2)

        # Mostrar la ventana de las burgers
        self.burgi = burgi.burger(lista.pop(0))
        self.burgi.solo_signal.connect(self.show_burger_window)
        self.burgi.show()
        self.close()

    def show_burger_window(self):
        self.show()

def generar_ordenes(num_elementos = mets.obtener_tareas(ruta_txt)):
    rango = list(range(1, 26))
    random.shuffle(rango)
    lista_generada = rango[:num_elementos]
    return lista_generada