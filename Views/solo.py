from PySide6.QtWidgets import QLabel, QWidget, QMessageBox
import methods as mets
import burgers as burgi
from PySide6.QtCore import Signal, Qt
import random, connection as con

ruta_txt = "src/AdminSoftware/res/options/options.txt"
class solo(QWidget):
    menu_principal_signal = Signal()
    
    def __init__(self, nombre = ""):
        super().__init__()

        self.setWindowTitle("La Cocinita - Modo Solitario")
        self.resize(1080, 720)
        label = mets.load_image_label(self, "src/AdminSoftware/res/img/fondo_solo.jpg")
        mets.iconify(self)
        lista = generar_ordenes()
        
        # region labels
        lbl_nombre = QLabel(self)
        lbl_nombre.setObjectName("titulo")
        lbl_nombre.setText(nombre + "'s")
        lbl_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_nombre.setGeometry(0, 0, 1080, 120)
        
        self.lbl_cliente = QLabel(self)
        self.lbl_cliente.setObjectName("test")
        self.lbl_cliente.setFixedSize(200, 270)
        self.lbl_cliente.move(400, 200)
        mets.set_image_on_label(self.lbl_cliente, con.obtener_ruta(lista[0]), 1.2)
        # endregion

        # region buttons
        self.btn_tareas = mets.ColoredButton("Tarea Pendiente", self)
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
        self.menu_principal_signal.emit()
        self.close()

    def on_btn_tareas_clicked(self, lista):
        if len(lista) == 0:
            QMessageBox.information(self, "Terminaste el día", "Ya no hay clientes, ¡buen trabajo!")
            return None
        else:
            print(lista)
            if len(lista) == 1:
                self.lbl_cliente.clear()
            else:
                mets.set_image_on_label(self.lbl_cliente, con.obtener_ruta(lista[1]), 1.2)
        
        self.burgi = burgi.burger(lista.pop(0)) # type: ignore
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

