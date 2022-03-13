
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtCore import QSize
import sys


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

    # Override method for class MainWindow.
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        old_size = event.oldSize()
        new_size = QSize(self.geometry().width(), self.geometry().height())
        print("old_size = {0}, new_size = {1}".format(old_size, new_size))
        QMainWindow.resizeEvent(self, event)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Resize Event')
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




