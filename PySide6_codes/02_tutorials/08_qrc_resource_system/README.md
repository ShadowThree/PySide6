# NOTE
Because the QMediaPlaylist was removed from QtMultimedia, the tutorial's code should be updated, see details [HERE](https://codereview.qt-project.org/c/pyside/pyside-setup/+/579365/2/sources/pyside6/doc/tutorials/basictutorial/qrcfiles.rst).

# How to use
## write the UI by python code
```bash
pyside6-rcc icons.qrc -o icons_rc.py    # according the qrc file, compiler the resource
python 08_qrc_main_1.py
```
## designer the UI by pyside6-designer
```bash
pyside6-rcc icons.qrc -o icons_rc.py    # according the qrc file, compiler the resource
pyside6-designer mainwindow.ui          # design the UI
pyside6-uic mainwindow.ui -o ui_mainwindow.py   # compiler the UI file to python code
python 08_qrc_main_2.py
```