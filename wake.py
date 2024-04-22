import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

class FullscreenWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загрузка пользовательского интерфейса из файла desktop.ui
        loadUi('desktop.ui', self)

        # Установка изображения в метке label из файла wallpaper.png
        self.label.setPixmap(QPixmap("wallpaper.png"))

        # Установка окна в полноэкранный режим
        self.showFullScreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FullscreenWindow()
    sys.exit(app.exec_())
