import sys
import methods as mets
import main as mn
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)
window = mn.MainWindow()
mets.apply_stylesheet(app)
window.show()
sys.exit(app.exec())