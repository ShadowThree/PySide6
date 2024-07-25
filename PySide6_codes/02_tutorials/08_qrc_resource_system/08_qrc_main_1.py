# @NOTE     The QMediaPlaylist was removed from QtMultimedia.
#           So this tutorial is NOT working now.
#           But you should notice how to using the icon from this tutorial.
#           First, you should add your icon in .qrc file;
#           Then, convert the icon to py file by "pyside-rcc icons.qrc -o rc_icons.py";
#           Last, using the Icon in py file: "icon = QIcon(QPixmap(":/icons/play.png"))",
#           Or, import the Icon in pyside-designer.

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QIcon, QKeySequence, QPixmap, QAction
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import icons_rc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._playlist = []
        self._playlist_index = -1
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        self._player.errorOccurred.connect(self._player_error)

        tool_bar = QToolBar()
        self.addToolBar(tool_bar)

        file_menu = self.menuBar().addMenu("&File")
        icon = QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen)
        open_action = QAction(icon, "&Open...", self, shortcut=QKeySequence.Open,
                             triggered=self.open)
        file_menu.addAction(open_action)
        tool_bar.addAction(open_action)

        exit_action = QAction(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit), "E&xit",
                             self, shortcut="Ctrl+Q", triggered=self.close)
        file_menu.addAction(exit_action)

        play_menu = self.menuBar().addMenu("&Play")
        playIcon = QIcon(QPixmap(":/icons/play.png"))
        self._play_action = tool_bar.addAction(playIcon, "Play")
        self._play_action.triggered.connect(self._player.play)
        play_menu.addAction(self._play_action)

        previousIcon = QIcon(QPixmap(":/icons/previous.png"))
        self._previous_action = tool_bar.addAction(previousIcon, "Previous")
        self._previous_action.triggered.connect(self.previous_clicked)
        play_menu.addAction(self._previous_action)

        pauseIcon = QIcon(QPixmap(":/icons/pause.png"))
        self._pause_action = tool_bar.addAction(pauseIcon, "Pause")
        self._pause_action.triggered.connect(self._player.pause)
        play_menu.addAction(self._pause_action)

        nextIcon = QIcon(QPixmap(":/icons/forward.png"))
        self._next_action = tool_bar.addAction(nextIcon, "Next")
        self._next_action.triggered.connect(self.next_clicked)
        play_menu.addAction(self._next_action)

        stopIcon = QIcon(QPixmap(":/icons/stop.png"))
        self._stop_action = tool_bar.addAction(stopIcon, "stop")
        self._stop_action.triggered.connect(self._ensure_stopped)
        play_menu.addAction(self._stop_action)
    
    def _player_error(param):
        print("player error", param)
    
    def open(param):
        print("open", param)
    
    def previous_clicked(param):
        print("previous clicked", param)

    def next_clicked(param):
        print("next clicked", param)

    def _ensure_stopped(param):
        print("stop", param)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())