import sys
from PyQt5.QtWidgets import QApplication
from run import windows

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = windows()    # 子的方法
    w.show()

    sys.exit(app.exec())