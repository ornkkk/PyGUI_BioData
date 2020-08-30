import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setGeometry(100, 100, 400, 300)
    window.setWindowTitle('Test GUI')
    text = QLabel(window)
    text.setText("Testing")
    text.move(105, 15)
    window.show()
    sys.exit(app.exec_())

