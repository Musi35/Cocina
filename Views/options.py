from PySide6.QtWidgets import QDialog, QLabel, QWidget, QVBoxLayout
import methods as mets
from PySide6.QtCore import Signal, Qt

class options(QWidget):
    menu_principal_signal = Signal()
    def __init__(self, nombre = ""):
        super().__init__()
        self.setWindowTitle("La Cocinita - Modo Opciones")
        self.resize(1080, 720)
        self.setup_ui()
        mets.iconify(self)
        # region labels
        lbl_titulo = QLabel(self)
        lbl_titulo.setObjectName("tit")
        lbl_titulo.setText("Opciones")
        lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_titulo.setGeometry(200, 0, 500, 120)
        # endregion

    def setup_ui(self):
        # region buttons
        btn_guardar = mets.ColoredButton("Guardar datos", self)
        btn_guardar.setObjectName("otros")
        btn_guardar.setFixedSize(160, 60)
        btn_guardar.move(200, 220)

        btn_salir = mets.ColoredButton("Menú Principal", self)
        btn_salir.setObjectName("otros")
        btn_salir.setFixedSize(160, 60)
        btn_salir.move(300, 40)
        btn_salir.clicked.connect(self.on_btn_salir_clicked)
        # endregion

    def on_btn_salir_clicked(self):
        self.menu_principal_signal.emit()
        self.close()
