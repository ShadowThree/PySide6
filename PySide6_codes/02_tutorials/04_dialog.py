import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QDialog, QVBoxLayout

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("MyForm")

        self.edit = QLineEdit("Write my name here...")
        self.button = QPushButton("Show Greeting")

        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.greetings)
    
    def greetings(self):
        print(f"Hello {self.edit.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec())

