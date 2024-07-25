# @NOTE Overloading Signals and Slots with different types
#       It is actually possible to use signals and slots of the same name
#       with different parameter type lists. This is legacy from Qt5 and
#       NOT recommended for new code. In Qt6, signals have distinct names
#       for different types.

import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Signal, Slot, QObject

class Communicate(QObject):
    # create two signals: one for int, the other for string
    speak = Signal((int,), (str,))

    def __init__(self, parent=None):
        super().__init__(parent)
        self.speak[int].connect(self.say_something)
        self.speak[str].connect(self.say_something)
    
    # define a slot that recv int or str
    @Slot(int)
    @Slot(str)
    def say_something(self, arg):
        if isinstance(arg, int):
            print("This is a number: ", arg)
        elif isinstance(arg, str):
            print("This is a string: ", arg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    someone = Communicate()
    # send signal
    someone.speak[int].emit[10]
    someone.speak[str].emit("Hello")
