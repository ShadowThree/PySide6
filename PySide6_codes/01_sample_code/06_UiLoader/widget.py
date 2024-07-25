from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject

uiLoader = QUiLoader()
class Widget(QObject):
  def __init__(self):
    super().__init__()
    self.ui = uiLoader.load("widget.ui")
    # self.ui.submitBtn.clicked.connect(self.submit_clicked)

  def show(self):
    self.ui.show()

  # def submit_clicked(self):
  #   print(f"{self.ui.nameLineEdit.text()} is a {self.ui.occupationLineEdit.text()}")