from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QPixmap
import methods as mets

# region paths de imagenes
# region comida
lechuga_path = "src/AdminSoftware/res/img/food/lechuga.png"
agua_path = "src/AdminSoftware/res/img/food/agua.png"
carne_path = "src/AdminSoftware/res/img/food/carne.png"
cebolla_path = "src/AdminSoftware/res/img/food/cebolla.png"
coca_path = "src/AdminSoftware/res/img/food/coca.png"
fanta_path = "src/AdminSoftware/res/img/food/fanta.png"
fresca_path = "src/AdminSoftware/res/img/food/fresca.png"
pan_abajo_path = "src/AdminSoftware/res/img/food/pan_abajo.png"
pan_arriba_path = "src/AdminSoftware/res/img/food/pan_arriba.png"
quesito_path = "src/AdminSoftware/res/img/food/queso.png"
tomate_path = "src/AdminSoftware/res/img/food/tomate.png"
logo_coca_path = "src/AdminSoftware/res/img/food/logo_coca.png"
logo_fanta_path = "src/AdminSoftware/res/img/food/logo_fanta.jpg"
logo_fresca_path = "src/AdminSoftware/res/img/food/logo_fresca.jpg"
logo_agua_path = "src/AdminSoftware/res/img/food/logo_agua.jpg"
# endregion

# region clientes
c1_path = "src/AdminSoftware/res/img/costumers/1.png"
c2_path = "src/AdminSoftware/res/img/costumers/2.png"
c3_path = "src/AdminSoftware/res/img/costumers/3.png"
c4_path = "src/AdminSoftware/res/img/costumers/4.png"
c5_path = "src/AdminSoftware/res/img/costumers/5.png"
c6_path = "src/AdminSoftware/res/img/costumers/6.png"
c7_path = "src/AdminSoftware/res/img/costumers/7.png"
c8_path = "src/AdminSoftware/res/img/costumers/8.png"
c9_path = "src/AdminSoftware/res/img/costumers/9.png"
c10_path = "src/AdminSoftware/res/img/costumers/10.png"
c11_path = "src/AdminSoftware/res/img/costumers/11.png"
c12_path = "src/AdminSoftware/res/img/costumers/12.png"
c13_path = "src/AdminSoftware/res/img/costumers/13.png"
c14_path = "src/AdminSoftware/res/img/costumers/14.png"
c15_path = "src/AdminSoftware/res/img/costumers/15.png"
c16_path = "src/AdminSoftware/res/img/costumers/16.png"
c17_path = "src/AdminSoftware/res/img/costumers/17.png"
c18_path = "src/AdminSoftware/res/img/costumers/18.png"
c19_path = "src/AdminSoftware/res/img/costumers/19.png"
c20_path = "src/AdminSoftware/res/img/costumers/20.png"
c21_path = "src/AdminSoftware/res/img/costumers/21.png"
c22_path = "src/AdminSoftware/res/img/costumers/22.png"
c23_path = "src/AdminSoftware/res/img/costumers/23.png"
c24_path = "src/AdminSoftware/res/img/costumers/24.png"
c25_path = "src/AdminSoftware/res/img/costumers/25.png"
# endregion
# endregion


class burger(QWidget):
    solo_signal = Signal()

    def __init__(self):
        super().__init__()
        
        # region Variables de instancia
        self.lbl_pos1 = QLabel(self)
        self.lbl_pos2 = QLabel(self)
        self.lbl_pos3 = QLabel(self)
        self.lbl_pos4 = QLabel(self)
        self.lbl_pos5 = QLabel(self)
        self.lbl_refresco = QLabel(self)
        self.btn_lechuga = mets.ColoredButton(self)
        self.btn_tomate = mets.ColoredButton(self)
        self.btn_cebolla = mets.ColoredButton(self)
        self.btn_queso = mets.ColoredButton(self)
        # endregion

        self.setWindowTitle("La Cocinita - Orden")
        mets.iconify(self)
        self.resize(1200, 900)
        self.setup_ui()
        self.clicker = 0

    def set_image_on_label(self, label, image_path, number):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(label.width() * number)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def setup_ui(self):
        # region buttons
        # region hamburguesas
        # region comida
        self.btn_lechuga.setObjectName("hamburguesa")
        self.btn_lechuga.setFixedSize(150, 100)
        self.btn_lechuga.move(20, 670)
        self.btn_lechuga.clicked.connect(self.on_btn_lechuga_clicked)
        self.btn_lechuga.raise_()

        self.btn_tomate.setObjectName("hamburguesa")
        self.btn_tomate.setFixedSize(150, 100)
        self.btn_tomate.move(220, 670)
        self.btn_tomate.clicked.connect(self.on_btn_tomate_clicked)
        self.btn_tomate.raise_()

        self.btn_cebolla.setObjectName("hamburguesa")
        self.btn_cebolla.setFixedSize(150, 100)
        self.btn_cebolla.move(420, 670)
        self.btn_cebolla.clicked.connect(self.on_btn_cebolla_clicked)
        self.btn_cebolla.raise_()

        self.btn_queso.setObjectName("hamburguesa")
        self.btn_queso.setFixedSize(150, 100)
        self.btn_queso.move(620, 670)
        self.btn_queso.clicked.connect(self.on_btn_queso_clicked)
        self.btn_queso.raise_()
        # endregion

        # region bebidas
        btn_coca = mets.ColoredButton(self)
        btn_coca.setObjectName("hamburguesa")
        btn_coca.setFixedSize(150, 100)
        btn_coca.move(20, 60)
        btn_coca.clicked.connect(self.on_btn_coca_clicked)
        btn_coca.raise_()
        
        btn_fanta = mets.ColoredButton(self)
        btn_fanta.setObjectName("hamburguesa")
        btn_fanta.setFixedSize(150, 120)
        btn_fanta.move(20, 170)
        btn_fanta.clicked.connect(self.on_btn_fanta_clicked)
        btn_fanta.raise_()
        
        btn_fresca = mets.ColoredButton(self)
        btn_fresca.setObjectName("hamburguesa")
        btn_fresca.setFixedSize(150, 120)
        btn_fresca.move(20, 300)
        btn_fresca.clicked.connect(self.on_btn_fresca_clicked)
        btn_fresca.raise_()
        
        btn_agua = mets.ColoredButton(self)
        btn_agua.setObjectName("hamburguesa")
        btn_agua.setFixedSize(150, 100)
        btn_agua.move(20, 430)
        btn_agua.clicked.connect(self.on_btn_agua_clicked)
        btn_agua.raise_()
        # endregion
        # endregion

        # region otros
        btn_terminar = mets.ColoredButton("Terminar orden", self)
        btn_terminar.setObjectName("otros")
        btn_terminar.setFixedSize(160, 60)
        btn_terminar.move(870, 700)
        # endregion

        # region imagenes
        # region comida
        lbl_lechuga = QLabel(self)
        self.set_image_on_label(lbl_lechuga, lechuga_path, 1.8)
        lbl_lechuga.setFixedSize(150, 100)
        lbl_lechuga.setObjectName("imagen")
        lbl_lechuga.move(20, 670)
        lbl_lechuga.lower()
        
        lbl_tomate = QLabel(self)
        self.set_image_on_label(lbl_tomate, tomate_path, 1.8)
        lbl_tomate.setFixedSize(150, 100)
        lbl_tomate.setObjectName("imagen")
        lbl_tomate.move(220, 670)
        lbl_tomate.lower()
        
        lbl_cebolla = QLabel(self)
        self.set_image_on_label(lbl_cebolla, cebolla_path, 1.8)
        lbl_cebolla.setFixedSize(150, 100)
        lbl_cebolla.setObjectName("imagen")
        lbl_cebolla.move(420, 670)
        lbl_cebolla.lower()
        
        lbl_queso = QLabel(self)
        self.set_image_on_label(lbl_queso, quesito_path, 1.8)
        lbl_queso.setFixedSize(150, 100)
        lbl_queso.setObjectName("imagen")
        lbl_queso.move(620, 670)
        lbl_queso.lower()
        # endregion
        
        # region bebidas
        lbl_coca = QLabel(self)
        self.set_image_on_label(lbl_coca, logo_coca_path, 1.8)
        lbl_coca.setFixedSize(150, 100)
        lbl_coca.setObjectName("imagen")
        lbl_coca.move(20, 60)
        lbl_coca.lower()
        
        lbl_fanta = QLabel(self)
        self.set_image_on_label(lbl_fanta, logo_fanta_path, 1.8)
        lbl_fanta.setFixedSize(150, 120)
        lbl_fanta.setObjectName("imagen")
        lbl_fanta.move(20, 170)
        lbl_fanta.lower()
        
        lbl_fresca = QLabel(self)
        self.set_image_on_label(lbl_fresca, logo_fresca_path, 1.8)
        lbl_fresca.setFixedSize(150, 120)
        lbl_fresca.setObjectName("imagen")
        lbl_fresca.move(20, 300)
        lbl_fresca.lower()
        
        lbl_agua = QLabel(self)
        self.set_image_on_label(lbl_agua, logo_agua_path, 1.8)
        lbl_agua.setFixedSize(150, 100)
        lbl_agua.setObjectName("imagen")
        lbl_agua.move(20, 430)
        lbl_agua.lower()
        # endregion
        
        # region fijos
        lbl_pan_abajo = QLabel(self)
        self.set_image_on_label(lbl_pan_abajo, pan_abajo_path, 3)
        lbl_pan_abajo.setObjectName("orden")
        lbl_pan_abajo.setFixedSize(300, 200)
        lbl_pan_abajo.move(220, 450)
        
        lbl_carne = QLabel(self)
        self.set_image_on_label(lbl_carne, carne_path, 3)
        lbl_carne.setObjectName("orden")
        lbl_carne.setFixedSize(300, 200)
        lbl_carne.move(220, 360)
        
        self.lbl_pos1.setObjectName("orden")
        self.lbl_pos1.setFixedSize(300, 200)
        self.lbl_pos1.move(220, 290)
        self.lbl_pos1.raise_()
        
        self.lbl_pos2.setObjectName("orden")
        self.lbl_pos2.setFixedSize(300, 200)
        self.lbl_pos2.move(220, 280)
        self.lbl_pos2.raise_()

        self.lbl_pos3.setObjectName("orden")
        self.lbl_pos3.setFixedSize(300, 200)
        self.lbl_pos3.move(220, 260)
        self.lbl_pos3.raise_()
        
        self.lbl_pos4.setObjectName("orden")
        self.lbl_pos4.setFixedSize(300, 200)
        self.lbl_pos4.move(220, 200)
        self.lbl_pos4.raise_()
        
        self.lbl_pos5.setObjectName("orden")
        self.lbl_pos5.setFixedSize(300, 200)
        self.lbl_pos5.move(220, 150)
        self.lbl_pos5.raise_()
        
        self.lbl_refresco.setObjectName("orden")
        self.lbl_refresco.setFixedSize(200, 500)
        self.lbl_refresco.move(520, 150)
        # endregion
        # endregion
        # endregion

    # region button functions

    def on_btn_lechuga_clicked(self):
        self.clicker += 1
        self.btn_lechuga.setDisabled(True)
        if self.clicker == 1:
            self.set_image_on_label(self.lbl_pos1, lechuga_path, .8)
        elif self.clicker == 2:
            self.set_image_on_label(self.lbl_pos2, lechuga_path, .8)
        elif self.clicker == 3:
            self.set_image_on_label(self.lbl_pos3, lechuga_path, .8)
        elif self.clicker == 4:
            self.set_image_on_label(self.lbl_pos4, lechuga_path, .8)
        elif self.clicker == 5:
            self.set_image_on_label(self.lbl_pos5, lechuga_path, .8)

    def on_btn_tomate_clicked(self):
        self.clicker += 1
        self.btn_tomate.setDisabled(True)
        if self.clicker == 1:
            self.set_image_on_label(self.lbl_pos1, tomate_path, 1)
        elif self.clicker == 2:
            self.set_image_on_label(self.lbl_pos2, tomate_path, 1)
        elif self.clicker == 3:
            self.set_image_on_label(self.lbl_pos3, tomate_path, 1)
        elif self.clicker == 4:
            self.set_image_on_label(self.lbl_pos4, tomate_path, 1)
        elif self.clicker == 5:
            self.set_image_on_label(self.lbl_pos5, tomate_path, 1)

    def on_btn_cebolla_clicked(self):
        self.clicker += 1
        self.btn_cebolla.setDisabled(True)
        if self.clicker == 1:
            self.set_image_on_label(self.lbl_pos1, cebolla_path, .8)
        elif self.clicker == 2:
            self.set_image_on_label(self.lbl_pos2, cebolla_path, .8)
        elif self.clicker == 3:
            self.set_image_on_label(self.lbl_pos3, cebolla_path, .8)
        elif self.clicker == 4:
            self.set_image_on_label(self.lbl_pos4, cebolla_path, .8)
        elif self.clicker == 5:
            self.set_image_on_label(self.lbl_pos5, cebolla_path, .8)

    def on_btn_queso_clicked(self):
        self.clicker += 1
        self.btn_queso.setDisabled(True)
        if self.clicker == 1:
            self.set_image_on_label(self.lbl_pos1, quesito_path, 1)
        elif self.clicker == 2:
            self.set_image_on_label(self.lbl_pos2, quesito_path, 1)
        elif self.clicker == 3:
            self.set_image_on_label(self.lbl_pos3, quesito_path, 1)
        elif self.clicker == 4:
            self.set_image_on_label(self.lbl_pos4, quesito_path, 1)
        elif self.clicker == 5:
            self.set_image_on_label(self.lbl_pos5, quesito_path, 1)

    def on_btn_coca_clicked(self):
        self.set_image_on_label(self.lbl_refresco, coca_path, 1)

    def on_btn_fresca_clicked(self):
        self.set_image_on_label(self.lbl_refresco, fresca_path, 1)

    def on_btn_agua_clicked(self):
        self.set_image_on_label(self.lbl_refresco, agua_path, 1.5)

    def on_btn_fanta_clicked(self):
        self.set_image_on_label(self.lbl_refresco, fanta_path, .8)
    # endregion