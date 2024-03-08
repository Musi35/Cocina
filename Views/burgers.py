from PySide6.QtWidgets import QLabel, QWidget, QGraphicsDropShadowEffect
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

        self.setWindowTitle("La Cocinita - Orden")
        mets.iconify(self)
        self.resize(1080, 720)
        self.setup_ui()

    def set_image_on_label(self, label, image_path):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaledToWidth(label.width() * 1.8)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def setup_ui(self):
        # region labels
        lbl_nombre = QLabel(self)
        lbl_nombre.setObjectName("titulo")
        lbl_nombre.setText("Cocina")
        lbl_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_nombre.setGeometry(0, 0, 1080, 120)
        # endregion

        # region buttons
        # region hamburguesas
        # region comida
        btn_lechuga = mets.ColoredButton(self)
        btn_lechuga.setObjectName("hamburguesa")
        btn_lechuga.setFixedSize(150, 100)
        btn_lechuga.move(50, 600)
        btn_lechuga.clicked.connect(self.on_btn_lechuga_clicked)
        btn_lechuga.raise_()

        btn_tomate = mets.ColoredButton(self)
        btn_tomate.setObjectName("hamburguesa")
        btn_tomate.setFixedSize(150, 100)
        btn_tomate.move(250, 600)
        btn_tomate.clicked.connect(self.on_btn_tomate_clicked)
        btn_tomate.raise_()

        btn_cebolla = mets.ColoredButton(self)
        btn_cebolla.setObjectName("hamburguesa")
        btn_cebolla.setFixedSize(150, 100)
        btn_cebolla.move(450, 600)
        btn_cebolla.clicked.connect(self.on_btn_cebolla_clicked)
        btn_cebolla.raise_()

        btn_queso = mets.ColoredButton(self)
        btn_queso.setObjectName("hamburguesa")
        btn_queso.setFixedSize(150, 100)
        btn_queso.move(650, 600)
        btn_queso.clicked.connect(self.on_btn_queso_clicked)
        btn_queso.raise_()
        # endregion

        # region bebidas
        btn_coca = mets.ColoredButton(self)
        btn_coca.setObjectName("hamburguesa")
        btn_coca.setFixedSize(150, 100)
        btn_coca.move(50, 60)
        btn_coca.clicked.connect(self.on_btn_coca_clicked)
        btn_coca.raise_()
        
        btn_fanta = mets.ColoredButton(self)
        btn_fanta.setObjectName("hamburguesa")
        btn_fanta.setFixedSize(150, 120)
        btn_fanta.move(50, 170)
        btn_fanta.clicked.connect(self.on_btn_fanta_clicked)
        btn_fanta.raise_()
        
        btn_fresca = mets.ColoredButton(self)
        btn_fresca.setObjectName("hamburguesa")
        btn_fresca.setFixedSize(150, 120)
        btn_fresca.move(50, 300)
        btn_fresca.clicked.connect(self.on_btn_fresca_clicked)
        btn_fresca.raise_()
        
        btn_agua = mets.ColoredButton(self)
        btn_agua.setObjectName("hamburguesa")
        btn_agua.setFixedSize(150, 100)
        btn_agua.move(50, 430)
        btn_agua.clicked.connect(self.on_btn_agua_clicked)
        btn_agua.raise_()
        # endregion
        # endregion

        # region otros
        btn_terminar = mets.ColoredButton("Terminar orden", self)
        btn_terminar.setObjectName("otros")
        btn_terminar.setFixedSize(160, 60)
        btn_terminar.move(870, 630)
        # endregion

        # region imagenes
        # region comida
        lbl_lechuga = QLabel(self)
        self.set_image_on_label(lbl_lechuga, lechuga_path)
        lbl_lechuga.setFixedSize(150, 100)
        lbl_lechuga.setObjectName("imagen")
        lbl_lechuga.move(50, 600)
        lbl_lechuga.lower()
        
        lbl_tomate = QLabel(self)
        self.set_image_on_label(lbl_tomate, tomate_path)
        lbl_tomate.setFixedSize(150, 100)
        lbl_tomate.setObjectName("imagen")
        lbl_tomate.move(250, 600)
        lbl_tomate.lower()
        
        lbl_cebolla = QLabel(self)
        self.set_image_on_label(lbl_cebolla, cebolla_path)
        lbl_cebolla.setFixedSize(150, 100)
        lbl_cebolla.setObjectName("imagen")
        lbl_cebolla.move(450, 600)
        lbl_cebolla.lower()
        
        lbl_queso = QLabel(self)
        self.set_image_on_label(lbl_queso, quesito_path)
        lbl_queso.setFixedSize(150, 100)
        lbl_queso.setObjectName("imagen")
        lbl_queso.move(650, 600)
        lbl_queso.lower()
        # endregion
        
        # region bebidas
        lbl_coca = QLabel(self)
        self.set_image_on_label(lbl_coca, logo_coca_path)
        lbl_coca.setFixedSize(150, 100)
        lbl_coca.setObjectName("imagen")
        lbl_coca.move(50, 60)
        lbl_coca.lower()
        
        lbl_fanta = QLabel(self)
        self.set_image_on_label(lbl_fanta, logo_fanta_path)
        lbl_fanta.setFixedSize(150, 120)
        lbl_fanta.setObjectName("imagen")
        lbl_fanta.move(50, 170)
        lbl_fanta.lower()
        
        lbl_fresca = QLabel(self)
        self.set_image_on_label(lbl_fresca, logo_fresca_path)
        lbl_fresca.setFixedSize(150, 120)
        lbl_fresca.setObjectName("imagen")
        lbl_fresca.move(50, 300)
        lbl_fresca.lower()
        
        lbl_agua = QLabel(self)
        self.set_image_on_label(lbl_agua, logo_agua_path)
        lbl_agua.setFixedSize(150, 100)
        lbl_agua.setObjectName("imagen")
        lbl_agua.move(50, 430)
        lbl_agua.lower()
        # endregion
        # endregion
        # endregion

    # region button functions
    def on_btn_lechuga_clicked(self):
        print("Lechuga")

    def on_btn_tomate_clicked(self):
        print("Tomate")

    def on_btn_cebolla_clicked(self):
        print("Cebolla")

    def on_btn_queso_clicked(self):
        print("Queso")

    def on_btn_coca_clicked(self):
        print("Coca-Cola")

    def on_btn_fresca_clicked(self):
        print("Fresca")

    def on_btn_agua_clicked(self):
        print("Agua")

    def on_btn_fanta_clicked(self):
        print("Fanta")

    # endregion