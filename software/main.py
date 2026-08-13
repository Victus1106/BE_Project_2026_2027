import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer

from gui.main_window import MainWindow
from core.app_controller import ApplicationController


app = QApplication(sys.argv)

window = MainWindow()

controller = ApplicationController(window)

timer = QTimer()

timer.timeout.connect(controller.update)

timer.start(16)      # ~60 FPS GUI update

window.show()

sys.exit(app.exec())