from PySide6.QtWidgets import QDialog, QLabel, QWidget, QLineEdit, QMessageBox
import methods as mets
from PySide6.QtCore import Signal, Qt

class options(QWidget):
    menu_principal_signal = Signal()
    def __init__(self, nombre = "", tareas = 0):
        super().__init__()
        self.setWindowTitle("La Cocinita - Modo Opciones")
        self.resize(1080, 720)
        self.setup_ui(nombre, tareas)
        mets.iconify(self)

    def setup_ui(self, nombre, tareas):
        # region buttons
        btn_guardar = mets.ColoredButton("Guardar datos", self)
        btn_guardar.setObjectName("otros")
        btn_guardar.setFixedSize(160, 60)
        btn_guardar.move(200, 620)
        btn_guardar.clicked.connect(lambda: self.on_btn_guardar_clicked(txt_nombre.text(), txt_tarea.text()))

        btn_salir = mets.ColoredButton("Menú Principal", self)
        btn_salir.setObjectName("otros")
        btn_salir.setFixedSize(160, 60)
        btn_salir.move(500, 620)
        btn_salir.clicked.connect(self.on_btn_salir_clicked)
        # endregion
        
        # region labels
        lbl_titulo = QLabel(self)
        lbl_titulo.setObjectName("tit")
        lbl_titulo.setText("Opciones")
        lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_titulo.setGeometry(300, 0, 500, 120)
        
        lbl_nombre = QLabel(self)
        lbl_nombre.setObjectName("normal")
        lbl_nombre.setText("Nombre del usuario: ")
        lbl_nombre.setGeometry(100,200,255,50)
        
        lbl_tareas = QLabel(self)
        lbl_tareas.setObjectName("normal")
        lbl_tareas.setText("Número de tareas por día: ")
        lbl_tareas.setGeometry(100,300,350,50)
        # endregion
        
        # region entry
        txt_nombre = QLineEdit(self)
        txt_nombre.setObjectName("txt")
        txt_nombre.setText(nombre)
        txt_nombre.setGeometry(400,210,200,35)
        
        txt_tarea = QLineEdit(self)
        txt_tarea.setObjectName("txt")
        txt_tarea.setText(str(tareas))
        txt_tarea.setGeometry(450,310,200,35)
        # endregion

    def on_btn_salir_clicked(self):
        self.menu_principal_signal.emit()
        self.close()
    
    def on_btn_guardar_clicked(self, nombre, tareas):
        # Chequeo de los campos
        if not nombre or not tareas:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese el nombre y las tareas.")
            return
        
        # Crear una cadena con el formato deseado
        datos_a_guardar = f"Nombre: {nombre}\nTareas: {tareas}"

        # Escribir la cadena en el archivo TXT
        with open("src/AdminSoftware/res/options/options.txt", "w") as archivo:
            archivo.write(datos_a_guardar)
        #Mostrar un QMessageBox indicando que los datos se actualizaron correctamente
        QMessageBox.information(self, "Éxito", "Los datos se actualizaron correctamente.")
