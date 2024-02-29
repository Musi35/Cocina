from PySide6.QtWidgets import QLabel, QWidget
import methods as mets
from PySide6.QtCore import Signal, Qt

class burger(QWidget):
    regresar = Signal()
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("La Cocinita - Orden")
        mets.iconify(self)
        self.resize(1080, 720)