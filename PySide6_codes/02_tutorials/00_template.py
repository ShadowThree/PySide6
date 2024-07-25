import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QDialog

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("MyForm")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())

