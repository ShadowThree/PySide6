# HOW TO USE
## Generate python class by UI file
```bash
pyside6-designer.exe ./mainwindow.ui                    # edit the UI
pyside6-uic.exe ./mainwindow.ui -o ui_mainwindow.py     # generate the python class
python ./07_ui_designer_1.py
```

## Load the UI file directly
```bash
pyside6-designer.exe ./mainwindow.ui                    # edit the UI
python ./07_ui_designer_2.py
```