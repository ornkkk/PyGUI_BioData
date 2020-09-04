# Restaurant Managaement System

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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
        self.setStyleSheet("background-color: lightblue; color: black")
        self.mainWindow()
        self.showMaximized()
        #self.show()


    def mainWindow(self):
        self.main_grid = QGridLayout()
        self.main_grid.setContentsMargins(25, 25, 25, 25)
        self.setLayout(self.main_grid)

        #----------------------- Main Title ----------------------------------------
        self.title()
        #----------------------- Customer Details ----------------------------------
        self.customer()
        #----------------------- Display Bill --------------------------------------
        self.bill()
        #----------------------- Menu Items ----------------------------------------
        self.menu()
        #----------------------- Buttons -------------------------------------------
        self.buttons()


    def title(self):
        main_title = QLabel("Restaurant Management System")
        main_title.setFont(QFont('Arial', 18))
        main_title.setAlignment(Qt.AlignCenter)
        main_title.resize(10, 10)
        main_title.setFixedHeight(75)
        self.main_grid.addWidget(main_title, 0, 0, 1, 2)


    def customer(self):
        customer_frame = QFrame()
        customer_frame.setObjectName("customerFrame")
        customer_frame.setStyleSheet("""QFrame#customerFrame{border-style: outset;
                                        border-width: 1px;
                                        border-radius: 5px;
                                        background-color: white;
                                        color: black;}""")
        customer_layout = QFormLayout(customer_frame)

        name = QLineEdit()
        email = QLineEdit()
        mobile = QLineEdit()

        name.setFixedWidth(500)
        email.setFixedWidth(500)
        mobile.setFixedWidth(250)

        table_num = QComboBox()
        table_num.addItems([str(i) for i in range(1,11)])
        table_num.setFixedWidth(50)

        customer_layout.addRow("Customer Name : ", name)
        customer_layout.addRow("Customer Email : ", email)
        customer_layout.addRow("Customer Mobile : ", mobile)
        customer_layout.addRow("Table Number : ", table_num)
        for wdgt in [name, email, mobile, table_num]:
            customer_layout.labelForField(wdgt).setStyleSheet("""font: 20px 'Times New Roman';
                                                                background-color: white;
                                                                color: black;""")
            wdgt.setStyleSheet("""font: 17px 'Times New Roman';
                                background-color: white;
                                color: black;
                                border-style: outset;
                                border-width: 1px;
                                border-radius: 5px;""")

        self.main_grid.addWidget(customer_frame, 1, 0)


    def bill(self):
        display_bill = QTextBrowser()
        display_bill.setFont(QFont('Arial', 12))
        #display_bill.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        display_bill.setFixedWidth(1000)
        display_bill.setStyleSheet("background-color: white")
        display_bill.setText("Display Bill")
        self.main_grid.addWidget(display_bill, 1, 1, 2, 1)


    def menu(self):
        menu_frame = QFrame()
        menu_frame.setObjectName("menuFrame")
        menu_frame.setStyleSheet("""QFrame#menuFrame{border-style: outset;
                                        border-width: 1px;
                                        border-radius: 5px;
                                        background-color: white;
                                        color: black;}""")
        menu_tab_layout = QHBoxLayout(menu_frame)

        self.menu_tabs=QTabWidget()
        self.menu_tabs.setObjectName("2")
        self.menu_tabs.setStyleSheet("""border-style: solid;
                                        border-width: 1px;
                                        border-radius: 5px;
                                        background-color: white;
                                        color: black;""")
        menu_tab_layout.addWidget(self.menu_tabs)

        self.menu1_tab = QWidget()
        self.menu_tabs.addTab(self.menu1_tab, "Menu 1")
        self.menu1_tab.setStyleSheet("""border-color: white;
                                        background-color: white;
                                        color: black;""")

        self.menu2_tab = QWidget()
        self.menu_tabs.addTab(self.menu2_tab, "Menu 2")
        self.menu2_tab.setStyleSheet("""border-color: white;
                                        background-color: white;
                                        color: black;""")

        self.menu1_items = {"item 1":[100,0], "item 2":[100,0], "item 3":[100,0], "item 4":[100,0], "item 5":[100,0],
                            "item 6":[100,0], "item 7":[100,0], "item 8":[100,0], "item 9":[100,0], "item 10":[100,0]}
        self.menu2_items = {"item 11":[200,0], "item 12":[200,0], "item 13":[200,0], "item 14":[200,0], "item 15":[200,0],
                            "item 16":[200,0], "item 17":[200,0], "item 18":[200,0], "item 19":[200,0], "item 20":[200,0]}

        self.display_menu(self.menu1_items, self.menu1_tab)
        self.display_menu(self.menu2_items, self.menu2_tab)

        self.main_grid.addWidget(menu_frame, 2, 0)


    def buttons(self):
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
        self.main_grid.addLayout(buttons_layout, 3, 1)


    def display_menu(self, menu_items, menu_tab):
        menu_layout=QVBoxLayout()
        for key in menu_items.keys():
            menuItems_layout=QHBoxLayout()
            item_name = QLabel(key)
            item_price = QLabel(u"\u20B9 " + str(menu_items[key][0]) + ".00")
            menu_items[key][1]=QSpinBox()
            menu_items[key][1].setFixedWidth(75)
            menu_items[key][1].setRange(0,20)
            menu_items[key][1].setPrefix("Qty : ")
            menuItems_layout.addWidget(item_name)
            menuItems_layout.addWidget(item_price)
            menuItems_layout.addWidget(menu_items[key][1])
            menu_layout.addLayout(menuItems_layout)
        menu_tab.setLayout(menu_layout)


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RestaurantManagementApp()
    sys.exit(app.exec_())