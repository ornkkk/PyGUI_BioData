# Restaurant Managaement System
# Import necessary modules
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton,
                             QCheckBox, QGridLayout, QVBoxLayout, QHBoxLayout, QSpinBox, QFormLayout, QComboBox)
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
        #self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("Restaurant Management App")
        #main_grid = QGridLayout()
        self.mainWindow()
       # self.displayUserInfo()
        #main_grid.addWidget(customerInfo, 0, 0)
        self.showMaximized()
        #self.show()


    def mainWindow(self):
        #self.setStyleSheet("background-color: cyan")
        main_grid = QGridLayout()
        main_grid.setContentsMargins(25, 25, 25, 25)

        main_title = QLabel("Restaurant Management System")
        main_title.setFont(QFont('Arial', 18))
        main_title.setAlignment(Qt.AlignCenter)
        main_title.resize(10, 10)
        main_title.setFixedHeight(75)
        main_title.setStyleSheet("background-color: white")


         #-------------------Customer Details----------------------------------------------
        customer_layout = QFormLayout()

        customer_layout.setFormAlignment(Qt.AlignCenter)
        title = QLabel("Customer Details")
        title.setFont(QFont('Arial', 12))
        title.setAlignment(Qt.AlignCenter)

        name = QLineEdit()
        name.setFixedWidth(500)

        email = QLineEdit()
        email.setFixedWidth(500)

        mobile = QLineEdit()
        mobile.setFixedWidth(250)

        table_num = QComboBox()
        table_num.addItems([str(i) for i in range(1,11)])
        table_num.setFixedWidth(50)

        customer_layout.addRow(title)
        customer_layout.addRow("Name : ", name)
        customer_layout.addRow("Email : ", email)
        customer_layout.addRow("Mobile : ", mobile)
        customer_layout.addRow("Table Number : ", table_num)

        #------------------------------ Display Bill ------------------------------------------------------------
        display_bill = QLabel("Bill")
        display_bill.setFont(QFont('Arial', 12))
        display_bill.setAlignment(Qt.AlignCenter)
        display_bill.setFixedWidth(1000)
        display_bill.setStyleSheet("background-color: White")

        #---------------------------- Menu Items -----------------------------------
        menu_layout=QVBoxLayout()
        self.items = {"item 1":[0,0], "item 2":[0,0], "item 3":[0,0], "item 4":[0,0], "item 5":[0,0], 
                      "item 6":[0,0], "item 7":[0,0], "item 8":[0,0], "item 9":[0,0], "item 10":[0,0]}
        for key in self.items.keys():
            menuItems_layout=QHBoxLayout()
            item_label = QLabel(key)
            self.items[key][1]=QSpinBox()
            self.items[key][1].setFixedWidth(75)
            self.items[key][1].setRange(0,20)
            self.items[key][1].setPrefix("Qty : ")
            menuItems_layout.addWidget(item_label)
            menuItems_layout.addWidget(self.items[key][1])
            menu_layout.addLayout(menuItems_layout)

        #----------------------------- Buttons ----------------------------------------
        buttons_layout=QHBoxLayout()
        print_button = QPushButton('Print Bill', self)
        #print_button.clicked.connect(self.buttonClicked)
        email_button = QPushButton('Email Bill', self)
        #print_button.clicked.connect(self.buttonClicked)
        sms_button = QPushButton('SMS Bill', self)
        #print_button.clicked.connect(self.buttonClicked)
        reset_button = QPushButton('Reset', self)
        #print_button.clicked.connect(self.buttonClicked)
        buttons_layout.addWidget(print_button)
        buttons_layout.addWidget(email_button)
        buttons_layout.addWidget(sms_button)
        buttons_layout.addWidget(reset_button)

        #------------------------------ Main Grid -------------------------------------
        main_grid.addWidget(main_title, 0, 0, 1, 2)
        main_grid.addLayout(customer_layout, 1, 0)
        main_grid.addWidget(display_bill, 1, 1, 2, 1)
        main_grid.addLayout(menu_layout, 2, 0)
        main_grid.addLayout(buttons_layout, 3, 1)
        self.setLayout(main_grid)


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RestaurantManagementApp()
    sys.exit(app.exec_())