import sys
from PyQt5.QtWidgets import QApplication, QWidget


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__() # create default constructor for QWidget
        self.initializeUI()
    

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Empty Window in PyQt')
        self.show()

# Run program
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = EmptyWindow()
   sys.exit(app.exec_())
   
   # Above code is same as
   #app = QApplication(sys.argv)
   #window = QWidget()
   #window.setGeometry(100, 100, 400, 300)
   #window.setWindowTitle('Empty Window in PyQt')
   #window.show()
   #sys.exit(app.exec_())

