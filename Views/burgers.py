from PySide6.QtWidgets import QLabel, QWidget, QMessageBox
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QPixmap
import methods as mets
import connection as conn

# region paths de imagenes
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

orden = []
bebida_actual = []

def mensaje_good():
    msgBox = QMessageBox()
    msgBox.setWindowTitle("¡Listo!")
    pixmap = QPixmap("src/AdminSoftware/res/img/estrella.png")  
    pixmap = pixmap.scaled(120,100)
    msgBox.setIconPixmap(pixmap)
    msgBox.setText("¡Lo hiciste increíble! Te ganaste una estrella.")
    msgBox.exec_()

class burger(QWidget):
    solo_signal = Signal()

    def __init__(self, cliente_id):
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
        self.btn_pan_arriba = mets.ColoredButton(self)
        # endregion

        self.setWindowTitle("La Cocinita - Orden")
        mets.iconify(self)
        self.resize(1200, 900)
        self.setup_ui(cliente_id)
        self.clicker = 0
        orden.clear()
        bebida_actual.clear()

    def setup_ui(self, cliente_id):
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

        self.btn_pan_arriba.setObjectName("hamburguesa")
        self.btn_pan_arriba.setFixedSize(150, 100)
        self.btn_pan_arriba.move(820, 670)
        self.btn_pan_arriba.clicked.connect(self.on_btn_pan_arriba_clicked)
        self.btn_pan_arriba.raise_()
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
        btn_terminar.move(1000, 700)
        btn_terminar.clicked.connect(lambda: self.on_btn_terminar_clicked(cliente_id))

        btn_limpiar = mets.ColoredButton("Limpiar", self)
        btn_limpiar.setObjectName("otros")
        btn_limpiar.setFixedSize(160, 60)
        btn_limpiar.move(1000, 630)
        btn_limpiar.clicked.connect(self.on_btn_limpiar_clicked)
        # endregion

        # region imagenes
        # region comida
        lbl_lechuga = QLabel(self)
        mets.set_image_on_label(lbl_lechuga, lechuga_path, 1.8)
        lbl_lechuga.setFixedSize(150, 100)
        lbl_lechuga.setObjectName("imagen")
        lbl_lechuga.move(20, 670)
        lbl_lechuga.lower()

        lbl_tomate = QLabel(self)
        mets.set_image_on_label(lbl_tomate, tomate_path, 1.8)
        lbl_tomate.setFixedSize(150, 100)
        lbl_tomate.setObjectName("imagen")
        lbl_tomate.move(220, 670)
        lbl_tomate.lower()

        lbl_cebolla = QLabel(self)
        mets.set_image_on_label(lbl_cebolla, cebolla_path, 1.8)
        lbl_cebolla.setFixedSize(150, 100)
        lbl_cebolla.setObjectName("imagen")
        lbl_cebolla.move(420, 670)
        lbl_cebolla.lower()

        lbl_queso = QLabel(self)
        mets.set_image_on_label(lbl_queso, quesito_path, 1.8)
        lbl_queso.setFixedSize(150, 100)
        lbl_queso.setObjectName("imagen")
        lbl_queso.move(620, 670)
        lbl_queso.lower()

        lbl_pan_arriba = QLabel(self)
        mets.set_image_on_label(lbl_pan_arriba, pan_arriba_path, 1.8)
        lbl_pan_arriba.setObjectName("imagen")
        lbl_pan_arriba.setFixedSize(150, 100)
        lbl_pan_arriba.move(820, 670)
        lbl_pan_arriba.lower()
        # endregion

        # region bebidas
        lbl_coca = QLabel(self)
        mets.set_image_on_label(lbl_coca, logo_coca_path, 1.8)
        lbl_coca.setFixedSize(150, 100)
        lbl_coca.setObjectName("imagen")
        lbl_coca.move(20, 60)
        lbl_coca.lower()

        lbl_fanta = QLabel(self)
        mets.set_image_on_label(lbl_fanta, logo_fanta_path, 1.8)
        lbl_fanta.setFixedSize(150, 120)
        lbl_fanta.setObjectName("imagen")
        lbl_fanta.move(20, 170)
        lbl_fanta.lower()

        lbl_fresca = QLabel(self)
        mets.set_image_on_label(lbl_fresca, logo_fresca_path, 1.8)
        lbl_fresca.setFixedSize(150, 120)
        lbl_fresca.setObjectName("imagen")
        lbl_fresca.move(20, 300)
        lbl_fresca.lower()

        lbl_agua = QLabel(self)
        mets.set_image_on_label(lbl_agua, logo_agua_path, 1.8)
        lbl_agua.setFixedSize(150, 100)
        lbl_agua.setObjectName("imagen")
        lbl_agua.move(20, 430)
        lbl_agua.lower()
        # endregion

        # region fijos
        lbl_pan_abajo = QLabel(self)
        mets.set_image_on_label(lbl_pan_abajo, pan_abajo_path, 3)
        lbl_pan_abajo.setObjectName("orden")
        lbl_pan_abajo.setFixedSize(300, 200)
        lbl_pan_abajo.move(220, 450)

        lbl_carne = QLabel(self)
        mets.set_image_on_label(lbl_carne, carne_path, 3)
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
        self.lbl_pos5.move(220, 170)
        self.lbl_pos5.raise_()

        self.lbl_refresco.setObjectName("orden")
        self.lbl_refresco.setFixedSize(200, 500)
        self.lbl_refresco.move(520, 150)
        # endregion
        # endregion
        # endregion

        # region DB
        lbl_nombre = QLabel(self)
        lbl_nombre.setFixedSize(150, 75)
        lbl_nombre.move(1050, 10)
        lbl_nombre.setText(conn.obtener_nombre(cliente_id))  # type: ignore
        lbl_nombre.setObjectName("normal")

        lbl_foto = QLabel(self)
        lbl_foto.setFixedSize(100, 150)
        lbl_foto.move(900, 10)
        lbl_foto.setObjectName("normal")
        mets.set_image_on_label(lbl_foto, conn.obtener_ruta(cliente_id), 1)  # type: ignore

        lbl_ingredientes = QLabel(self)
        lbl_ingredientes.setFixedSize(200, 300)
        lbl_ingredientes.move(950, 180)
        lbl_ingredientes.setObjectName("ticket")
        lista = "\n \n".join(conn.obtener_ingredientes(cliente_id))  # type: ignore
        lbl_ingredientes.setText(lista)

        lbl_chesco = QLabel(self)
        lbl_chesco.setFixedSize(200, 125)
        lbl_chesco.move(950, 480)
        logo = conn.obtener_refresco(cliente_id)  # type: ignore
        if logo == "Coca-Cola":
            mets.set_image_on_label(lbl_chesco, logo_coca_path, 1)
        elif logo == "Fanta":
            mets.set_image_on_label(lbl_chesco, logo_fanta_path, 1)
        elif logo == "Fresca":
            mets.set_image_on_label(lbl_chesco, logo_fresca_path, 1)
        elif logo == "Agua":
            mets.set_image_on_label(lbl_chesco, logo_agua_path, 1)
        # endregion

# region button functions

    def on_btn_lechuga_clicked(self):
        self.clicker += 1
        orden.append("Lechuga")
        self.btn_lechuga.setDisabled(True)
        if self.clicker == 1:
            mets.set_image_on_label(self.lbl_pos1, lechuga_path, .8)
        elif self.clicker == 2:
            mets.set_image_on_label(self.lbl_pos2, lechuga_path, .8)
        elif self.clicker == 3:
            mets.set_image_on_label(self.lbl_pos3, lechuga_path, .8)
        elif self.clicker == 4:
            mets.set_image_on_label(self.lbl_pos4, lechuga_path, .8)
        elif self.clicker == 5:
            mets.set_image_on_label(self.lbl_pos5, lechuga_path, .8)

    def on_btn_tomate_clicked(self):
        self.clicker += 1
        orden.append("Tomate")
        self.btn_tomate.setDisabled(True)
        if self.clicker == 1:
            mets.set_image_on_label(self.lbl_pos1, tomate_path, 1)
        elif self.clicker == 2:
            mets.set_image_on_label(self.lbl_pos2, tomate_path, 1)
        elif self.clicker == 3:
            mets.set_image_on_label(self.lbl_pos3, tomate_path, 1)
        elif self.clicker == 4:
            mets.set_image_on_label(self.lbl_pos4, tomate_path, 1)
        elif self.clicker == 5:
            mets.set_image_on_label(self.lbl_pos5, tomate_path, 1)

    def on_btn_cebolla_clicked(self):
        self.clicker += 1
        orden.append("Cebolla")
        self.btn_cebolla.setDisabled(True)
        if self.clicker == 1:
            mets.set_image_on_label(self.lbl_pos1, cebolla_path, .8)
        elif self.clicker == 2:
            mets.set_image_on_label(self.lbl_pos2, cebolla_path, .8)
        elif self.clicker == 3:
            mets.set_image_on_label(self.lbl_pos3, cebolla_path, .8)
        elif self.clicker == 4:
            mets.set_image_on_label(self.lbl_pos4, cebolla_path, .8)
        elif self.clicker == 5:
            mets.set_image_on_label(self.lbl_pos5, cebolla_path, .8)

    def on_btn_queso_clicked(self):
        self.clicker += 1
        orden.append("Queso")
        self.btn_queso.setDisabled(True)
        if self.clicker == 1:
            mets.set_image_on_label(self.lbl_pos1, quesito_path, 1)
        elif self.clicker == 2:
            mets.set_image_on_label(self.lbl_pos2, quesito_path, 1)
        elif self.clicker == 3:
            mets.set_image_on_label(self.lbl_pos3, quesito_path, 1)
        elif self.clicker == 4:
            mets.set_image_on_label(self.lbl_pos4, quesito_path, 1)
        elif self.clicker == 5:
            mets.set_image_on_label(self.lbl_pos5, quesito_path, 1)

    def on_btn_coca_clicked(self):
        mets.set_image_on_label(self.lbl_refresco, coca_path, 1)
        bebida_actual.clear()
        bebida_actual.append("Coca-Cola")

    def on_btn_fresca_clicked(self):
        mets.set_image_on_label(self.lbl_refresco, fresca_path, 1)
        bebida_actual.clear()
        bebida_actual.append("Fresca")

    def on_btn_agua_clicked(self):
        mets.set_image_on_label(self.lbl_refresco, agua_path, 1.5)
        bebida_actual.clear()
        bebida_actual.append("Agua")

    def on_btn_fanta_clicked(self):
        mets.set_image_on_label(self.lbl_refresco, fanta_path, .8)
        bebida_actual.clear()
        bebida_actual.append("Fanta")

    def on_btn_pan_arriba_clicked(self):
        self.clicker += 1
        orden.append("Pan")
        self.btn_pan_arriba.setDisabled(True)
        if self.clicker == 1:
            mets.set_image_on_label(self.lbl_pos1, pan_arriba_path, 1)
        elif self.clicker == 2:
            mets.set_image_on_label(self.lbl_pos2, pan_arriba_path, 1)
        elif self.clicker == 3:
            mets.set_image_on_label(self.lbl_pos3, pan_arriba_path, 1)
        elif self.clicker == 4:
            mets.set_image_on_label(self.lbl_pos4, pan_arriba_path, 1)
        elif self.clicker == 5:
            mets.set_image_on_label(self.lbl_pos5, pan_arriba_path, 1)

    def on_btn_limpiar_clicked(self):
        self.lbl_pos1.clear()
        self.lbl_pos2.clear()
        self.lbl_pos3.clear()
        self.lbl_pos4.clear()
        self.lbl_pos5.clear()
        self.lbl_refresco.clear()
        self.clicker = 0
        self.btn_lechuga.setDisabled(False)
        self.btn_tomate.setDisabled(False)
        self.btn_cebolla.setDisabled(False)
        self.btn_queso.setDisabled(False)
        self.btn_pan_arriba.setDisabled(False)
        orden.clear()
        bebida_actual.clear()

    def on_btn_terminar_clicked(self, cliente_id):
        base = conn.obtener_ingredientes(cliente_id)
    
        if orden[-1] != "Pan":
            QMessageBox.warning(self, "¡Cuidado!", "Recuerda que el pan debe ir al final.")
            return False
    
        if not bebida_actual:
            QMessageBox.warning(self, "¡Cuidado!", "Por favor selecciona una bebida.")
            return False
    
        if bebida_actual[0] != conn.obtener_refresco(cliente_id): # type: ignore
            QMessageBox.warning(self, "¡Cuidado!", "Oops, parece que te equivocaste de bebida. \n"
                            + "No pasa nada, solo hay que intentarlo otra vez. ¡Ánimo!")
            return False
    
        if set(base) == set(orden[:-1]): # type: ignore
            mensaje_good()
            self.close()
            self.solo_signal.emit()
            return True
        else:
            ingredientes_diff = set(base) - set(orden[:-1]) # type: ignore
            QMessageBox.warning(self, "¡Cuidado!", f"Parece que te equivocaste o te faltaron algunos ingredientes: \n {ingredientes_diff}."
                            + "No te preocupes, solo tienes que intentarlo otra vez. ¡Ánimo!")
            return False

    # endregion