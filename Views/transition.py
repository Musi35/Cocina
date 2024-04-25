from PySide6.QtWidgets import QLabel, QWidget
import methods as mets
import solo as solo
from PySide6.QtCore import Signal, Qt

class transition(QWidget):
    burguir_signal = Signal()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("La Cocinita - Transición de día")
        self.resize(1080, 720)
        mets.iconify(self)

        lbl_anuncio = QLabel(self)
        lbl_anuncio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_anuncio.setFixedSize(500, 500)
        lbl_anuncio.move(300, 0)
        mets.set_image_on_label(lbl_anuncio, "src/AdminSoftware/res/img/abierto.png", 1)
        
        btn_iniciar = mets.ColoredButton("Iniciar nuevo día", self)
        btn_iniciar.setObjectName("llamada")
        btn_iniciar.setFixedSize(160, 60)
        btn_iniciar.move(500, 550)
        btn_iniciar.clicked.connect(self.on_btn_iniciar_clicked)
        
    def on_btn_iniciar_clicked(self):
        self.burguir_signal.emit()
        self.close()
        
    def show_solo_window(self):
        self.solo_window = solo.solo()
        self.solo_window.show()