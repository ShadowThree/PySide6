# python 虚拟环境使用
```bash
python -m venv .                # 在当前目录创建虚拟环境
./Scripts/activate              # 激活虚拟环境
deactivate                      # 退出虚拟环境
pip freeze > Requestments.txt   # 生成当前虚拟环境安装的依赖包
pip install -r Requestments.txt # 按指定包设置当前虚拟环境
```

# PySide6 指令
```bash
pyside6-designer                                    # edit or create a .ui file
pyside6-uic -i form.ui -o ui_form.py                # compile .ui to .py
pyside6-rcc -i resources.qrc -o rc_resources.py     # compile .qrc to .py
```