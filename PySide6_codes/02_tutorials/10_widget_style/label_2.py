import sys
from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignHCenter)
            menu_widget.addItem(item)
        
        text_widget = QLabel("_placeholder")
        # text_widget.setObjectName("label2")
        button = QPushButton("something")

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Widget()
    w.show()

    with open("style2.qss") as f:
        w.setStyleSheet(f.read())

    sys.exit(app.exec())