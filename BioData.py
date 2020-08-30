import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont

class BioDataWindow(QWidget):
    """[summary]

    Args:
        QWidget ([type]): [description]
    """


    def __init__(self):
        super().__init__()
        self.initialize_ui()


    def initialize_ui(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle('Bio Data')
        self.display_images()
        self.display_info()
        self.show()


    def display_images(self):
        """
        Set Backgroud Color and Profile Image using QLabels.
        Check to see if image files exist, if not throw an
        exception.
        """
        bg_image = "./images/skyblue.png"
        dp_image = "./images/profile_image.png"
        bg = QLabel(self)
        dp = QLabel(self)
        try:
            with open(bg_image):
                pixmap = QPixmap(bg_image)
                bg.setPixmap(pixmap)
        except FileNotFoundError:
            bg.setText("BG Image Load Error")

        try:
            with open(dp_image):
                pixmap = QPixmap(dp_image)
                dp.setPixmap(pixmap)
                dp.move(70, 20)
        except FileNotFoundError:
            dp.setText("DP Image Load Error")
            dp.move(70, 20)


    def display_info(self):
        """
        Create the labels to be displayed for the User Profile.
        """
        user_name = QLabel(self)
        user_name.setText("Koushik Kiran Kumar")
        user_name.move(20, 140)
        user_name.setFont(QFont('Arial', 14))
        bio_title = QLabel(self)
        bio_title.setText("Biography")
        bio_title.move(15, 175)
        bio_title.setFont(QFont('Arial', 10))
        about = QLabel(self)
        about.setText("I'm a MS research scholar in CSE Department at IIT Madras")
        about.setWordWrap(True)
        about.move(15, 200)
        skills_title = QLabel(self)
        skills_title.setText("Skills")
        skills_title.move(15, 245)
        skills_title.setFont(QFont('Arial', 10))
        skills = QLabel(self)
        skills.setText("Python | C++ | SQL | JavaScript")
        skills.move(15, 270)
        experience_title = QLabel(self)
        experience_title.setText("Experience")
        experience_title.move(15, 305)
        experience_title.setFont(QFont('Arial', 10))
        experience = QLabel(self)
        experience.setText("Research Scholar")
        experience.move(15, 330)
        dates = QLabel(self)
        dates.setText("June 2019 - Present")
        dates.move(15, 345)


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BioDataWindow()
    sys.exit(app.exec_())