# Restaurant Managaement System
# Import necessary modules
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QCheckBox, QGridLayout, QVBoxLayout, QFormLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class RestaurantManagementApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("Restaurant Management App")
        #main_grid = QGridLayout()
        self.mainWindow()
       # self.displayUserInfo()
        #main_grid.addWidget(customerInfo, 0, 0)
        self.showMaximized()
        #self.show()


    def mainWindow(self):
        main_grid = QGridLayout()

        #Customer Details
        customer_grid  = QFormLayout()

        main_title = QLabel("Restaurant Management System")
        main_title.setFont(QFont('Arial', 18))
        main_title.setAlignment(Qt.AlignCenter)
        main_title.resize(10, 10)

        title = QLabel("Customer Details")
        title.setFont(QFont('Arial', 12))
        title.setAlignment(Qt.AlignCenter)

        name = QLineEdit()
        name.resize(100, 100)

        email = QLineEdit()
        email.resize(1000, 100)

        mobile = QLineEdit()

        customer_grid.addRow(title)
        customer_grid.addRow("Name : ", name)
        customer_grid.addRow("Email : ", email)
        customer_grid.addRow("Mobile : ", mobile)

        #Menu Items

        main_grid.addWidget(main_title, 0, 0)
        main_grid.addLayout(customer_grid, 1, 0)
        self.setLayout(main_grid)


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RestaurantManagementApp()
    sys.exit(app.exec_())