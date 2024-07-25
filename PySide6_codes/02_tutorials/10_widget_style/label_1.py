import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QFontDatabase

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # print(QFontDatabase.families())       # print the system fonts
    label = QLabel("This is a placeholder text")
    label.setAlignment(Qt.AlignCenter)
    # set stylesheet by CSS
    label.setStyleSheet("""
        background-color: #262626;
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 18px;""")
    label.show()
    sys.exit(app.exec())
