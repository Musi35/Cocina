from PySide6.QtWidgets import QLabel, QWidget, QInputDialog, QMessageBox
import methods as mets
from PySide6.QtCore import Signal, Qt
import multi_burger as mb

class multi(QWidget):
    menu_principal_signal = Signal()
    
    def __init__(self, nombre = ""):
        super().__init__()

        self.setWindowTitle("La Cocinita - Modo Multijugador")
        self.resize(1080, 720)
        label = mets.load_image_fondo(self, "src/AdminSoftware/res/img/fondo_multi.jpg")
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
        btn_m1 = mets.ColoredButton("1", self)
        btn_m1.setObjectName("mesa")
        btn_m1.setFixedSize(120, 120)
        btn_m1.move(385, 195)
        btn_m1.clicked.connect(self.on_btn_mesa_clicked)

        btn_m2 = mets.ColoredButton("2", self)
        btn_m2.setObjectName("mesa")
        btn_m2.setFixedSize(120, 120)
        btn_m2.move(600, 195)
        btn_m2.clicked.connect(self.on_btn_mesa_clicked)

        btn_m3 = mets.ColoredButton("3", self)
        btn_m3.setObjectName("mesa")
        btn_m3.setFixedSize(120, 120)
        btn_m3.move(385, 480)
        btn_m3.clicked.connect(self.on_btn_mesa_clicked)

        btn_m4 = mets.ColoredButton("4", self)
        btn_m4.setObjectName("mesa")
        btn_m4.setFixedSize(120, 120)
        btn_m4.move(600, 480)
        btn_m4.clicked.connect(self.on_btn_mesa_clicked)

        # endregion

    def on_btn_salir_clicked(self):
        self.menu_principal_signal.emit()
        self.close()
    
    def on_btn_mesa_clicked(self):
        nombre = self.open_dialog()
        if nombre is None:
            return  # No hacer nada si se cancela el diálogo
        elif not nombre:
            QMessageBox.warning(self, "¡Cuidado!", "Parece que no has ingresado un nombre. Por favor, intenta de nuevo.")
        else:
            self.mb = mb.multi_burger(nombre)
            self.mb.multi_signal.connect(self.show_multi_window)
            self.mb.show()
            self.close()
    
    def show_multi_window(self):
        self.show()

    def open_dialog(self):
        text, ok = QInputDialog.getText(self, 'Cliente', 'Escribe el nombre del cliente:')
        if ok:
            return text.strip()
        else:
            return None