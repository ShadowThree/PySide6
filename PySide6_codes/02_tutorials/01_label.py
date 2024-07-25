import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label1 = QLabel("<font color=red size=40>Hello World</font>")
label2 = QLabel(sys.argv[0] + (sys.argv[1] if len(sys.argv) >= 2 else "") + "<font> size=40>Hello World</font>")
label1.show()
label2.show()
app.exec()