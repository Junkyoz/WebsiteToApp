import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Specify the full path to the files
        script_dir = os.path.dirname(os.path.abspath(__file__))
        website_path = os.path.join(script_dir, 'website.txt')
        name_path = os.path.join(script_dir, 'name.txt')

        window_title = "Default Title"  # Assign a default value

        try:
            with open(website_path, 'r') as file:
                website_url = file.read()
        except FileNotFoundError:
            print(f'Error: {website_path} not found')

        try:
            with open(name_path, 'r') as file:
                window_title = file.read()
        except FileNotFoundError:
            print(f'Error: {name_path} not found')
            
        self.browser = QWebEngineView()
        if website_url:
            self.browser.setUrl(QUrl(website_url))
        self.setCentralWidget(self.browser)

        self.setGeometry(100, 100, 800, 600)

        # Set the window title based on the content of name.txt
        self.setWindowTitle(window_title)

        # Show the main window
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())