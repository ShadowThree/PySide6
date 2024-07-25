from PySide6.QtWidgets import QWidget, QCheckBox, QRadioButton, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup

class Widget(QWidget):
  def __init__(self):
    super().__init__()

    os = QGroupBox("Choose operating system")
    win = QCheckBox("Windows")
    win.clicked.connect(self.win_checked)
    win.setChecked(True)
    linux = QCheckBox("Linux")
    mac = QCheckBox("Mac")

    os_layout = QVBoxLayout()
    os_layout.addWidget(win)
    os_layout.addWidget(linux)
    os_layout.addWidget(mac)
    os.setLayout(os_layout)

    drink = QGroupBox("Choose your favorite drink")
    beer = QCheckBox("Beer")
    beer.toggled.connect(self.beer_checked)
    juice = QCheckBox("Juice")
    coffee = QCheckBox("Coffee")
    beer.setChecked(True)

    exclusive_btn = QButtonGroup(self)  # must self
    exclusive_btn.addButton(beer)
    exclusive_btn.addButton(juice)
    exclusive_btn.addButton(coffee)
    exclusive_btn.setExclusive(True)
    # exclusive_btn.buttonClicked.connect(self.exclusive_checked)
    
    drink_layout = QVBoxLayout()
    drink_layout.addWidget(beer)
    drink_layout.addWidget(juice)
    drink_layout.addWidget(coffee)
    drink.setLayout(drink_layout)

    answer = QGroupBox("Answer")
    answerA = QRadioButton("A")
    answerA.clicked.connect(self.answerA_checked)
    answerB = QRadioButton("B")
    answerC = QRadioButton("C")
    answer_layout = QVBoxLayout()
    answer_layout.addWidget(answerA)
    answer_layout.addWidget(answerB)
    answer_layout.addWidget(answerC)
    answer.setLayout(answer_layout)

    h_layout = QHBoxLayout()
    h_layout.addWidget(os)
    h_layout.addWidget(drink)
    
    v_layout = QVBoxLayout()
    v_layout.addLayout(h_layout)
    v_layout.addWidget(answer)

    self.setLayout(v_layout)

  def win_checked(self):
    if self.sender().isChecked():
      print("Windows is checked")

  def beer_checked(self):
    if self.sender().isChecked():
      print(self.sender().text() + " is checked")

  def answerA_checked(self):
    if self.sender().isChecked():
      print(self.sender().text() + " is checked")

  def exclusive_checked(self):
    print(self.sender())