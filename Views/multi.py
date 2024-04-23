from PySide6.QtWidgets import QLabel, QWidget
import methods as mets
from PySide6.QtCore import Signal, Qt

class multi(QWidget):
    menu_principal_signal = Signal()
    def __init__(self, nombre = ""):
        super().__init__()

        self.setWindowTitle("La Cocinita - Modo Multijugador")
        self.resize(1080, 720)
        label = mets.load_image_label(self, "src/AdminSoftware/res/img/fondo_multi.jpg")
        mets.iconify(self)
        self.setup_ui()
        
        lbl_nombre = QLabel(self)
        lbl_nombre.setObjectName("titulo")
        lbl_nombre.setText(nombre + "'s")
        lbl_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_nombre.setGeometry(0, 0, 1080, 120)
        
        btn_salir = mets.ColoredButton("Menú Principal", self)
        btn_salir.setObjectName("otros")
        btn_salir.setFixedSize(160, 60)
        btn_salir.move(880, 50)
        btn_salir.clicked.connect(self.on_btn_salir_clicked)

    def setup_ui(self):
        # region buttons
        # region mesas
        btn_m1 = mets.ColoredButton("1", self)
        btn_m1.setObjectName("mesa")
        btn_m1.setFixedSize(120, 120)
        btn_m1.move(385, 195)

        btn_m2 = mets.ColoredButton("2", self)
        btn_m2.setObjectName("mesa")
        btn_m2.setFixedSize(120, 120)
        btn_m2.move(600, 195)

        btn_m3 = mets.ColoredButton("3", self)
        btn_m3.setObjectName("mesa")
        btn_m3.setFixedSize(120, 120)
        btn_m3.move(385, 480)

        btn_m4 = mets.ColoredButton("4", self)
        btn_m4.setObjectName("mesa")
        btn_m4.setFixedSize(120, 120)
        btn_m4.move(600, 480)
        # endregion

        # region otros
        btn_tareas = mets.ColoredButton("Tarea Pendiente", self)
        btn_tareas.setObjectName("otros")
        btn_tareas.setFixedSize(160, 60)
        btn_tareas.move(880, 130)
        # endregion
        # endregion

    def on_btn_salir_clicked(self):
        self.menu_principal_signal.emit()
        self.close()
