from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout

class ButtonHolder(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Button Holder")
    button = QPushButton("Click Me")
    button.setCheckable(True)   # must for triggering toggled
    button.clicked.connect(self.on_click1)
    button.clicked.connect(self.on_click2)
    button.pressed.connect(self.on_press)
    button.released.connect(self.on_release)
    button.toggled.connect(self.on_toggled)   
    self.setCentralWidget(button)
  
  def on_click1(self):
    print("Button clicked")
  
  def on_click2(self, state: bool):  # seems same with toggled
    print("Button clicked:", state)

  def on_press(self):
    print("Button pressed")
  
  def on_release(self):
    print("Button released")
  
  def on_toggled(self, state: bool):  # only triggered by checkable button
    print("Button toggled:", state)